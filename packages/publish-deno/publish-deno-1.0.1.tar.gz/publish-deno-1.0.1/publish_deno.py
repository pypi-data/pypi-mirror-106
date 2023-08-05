#!/usr/bin/env python

import argparse
import json
import os
import pkg_resources
import re
import subprocess
import sys

# Constants
VERSION = pkg_resources.get_distribution("publish_npm").version
DIR = os.getcwd()
PROJECT_NAME = os.path.basename(DIR)
VERSION_TS = "version.ts"
VERSION_TS_PATH = os.path.join(DIR, VERSION_TS)
MOD_TS = "mod.ts"
MOD_TS_PATH = os.path.join(DIR, "src", "mod.ts")


def main():
    if sys.version_info < (3, 0):
        printf("Error: This script requires Python 3.")
        sys.exit(1)

    args = parse_command_line_arguments()

    # Check to see if the "version.ts" file exists
    if not os.path.isfile(VERSION_TS_PATH):
        error(
            'Failed to find the "{}" file in the current working directory.'.format(
                VERSION_TS
            )
        )

    # Check that the program compiles
    printf("Testing to see if the project compiles...")
    check_compile()

    # Increment the version number
    version = get_version_from_version_ts()
    if not args.skip_increment:
        version = increment_version(version)
        put_version(version)

    git_commit_if_changes(version)
    git_tag(version)

    # Done
    printf("Published {} version {} successfully.".format(PROJECT_NAME, version))


def parse_command_line_arguments():
    parser = argparse.ArgumentParser(
        description="Publish a new version of this package to Deno."
    )

    parser.add_argument(
        "-v",
        "--version",
        action="version",
        help="display the version",
        version=VERSION,
    )

    parser.add_argument(
        "-s",
        "--skip-increment",
        action="store_true",
        help='do not increment the version number in the "{}" file'.format(VERSION_TS),
    )

    return parser.parse_args()


def check_compile():
    if not os.path.isfile(MOD_TS_PATH):
        error('Failed to find the "{}" file.'.format(MOD_TS_PATH))

    completed_process = subprocess.run(
        ["deno", "--unstable", "bundle", MOD_TS_PATH],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    if completed_process.returncode != 0:
        error('Failed to build the project with "deno bundle".')


def get_version_from_version_ts():
    with open(VERSION_TS_PATH, "r") as file_handle:
        version_ts = file_handle.read().strip()
    match = re.search(r'export const VERSION = "(.+\..+\..+)";', version_ts)
    if not match:
        error('Failed to parse the version number from "{}".'.format(VERSION_TS_PATH))

    return match.group(1)


def increment_version(version: str):
    print(version)
    match = re.search(r"(.+\..+\.)(.+)", version)
    if not match:
        error('Failed to parse the version number of "{}".'.format(version))
    version_prefix = match.group(1)
    patch_version = int(match.group(2))  # i.e. the third number
    incremented_patch_version = patch_version + 1
    incremented_version = version_prefix + str(incremented_patch_version)

    return incremented_version


def put_version(version: str):
    new_version_ts = 'export const VERSION = "{}";\n'.format(version)
    with open(VERSION_TS_PATH, "w", newline="\n") as file_handle:
        file_handle.write(new_version_ts)


def git_commit_if_changes(version):
    # Check to see if this is a git repository
    completed_process = subprocess.run(
        ["git", "status"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    if completed_process.returncode != 0:
        error("This is not a git repository.")

    # Check to see if there are any changes
    # https://stackoverflow.com/questions/3878624/how-do-i-programmatically-determine-if-there-are-uncommitted-changes
    completed_process = subprocess.run(["git", "diff-index", "--quiet", "HEAD", "--"])
    changes_to_existing_files = completed_process.returncode != 0

    # Check to see if there are any untracked files
    # https://stackoverflow.com/questions/11021287/git-detect-if-there-are-untracked-files-quickly
    completed_process = subprocess.run(
        ["git", "ls-files", "--other", "--directory", "--exclude-standard"],
        stdout=subprocess.PIPE,
    )
    if completed_process.returncode != 0:
        error("Failed to git ls-files.")
    git_output = completed_process.stdout.decode("utf-8")
    untracked_files_exist = git_output is not None and git_output.strip() != ""

    if not changes_to_existing_files and not untracked_files_exist:
        printf("There are no changes to push to git.")
        return

    # Commit to the repository
    printf("Committing to the Git repository...")
    completed_process = subprocess.run(["git", "add", "-A"])
    if completed_process.returncode != 0:
        error("Failed to git add.")
    completed_process = subprocess.run(["git", "commit", "-m", version])
    if completed_process.returncode != 0:
        error("Failed to git commit.")
    completed_process = subprocess.run(["git", "pull", "--rebase"])
    if completed_process.returncode != 0:
        error("Failed to git pull.")
    completed_process = subprocess.run(["git", "push"])
    if completed_process.returncode != 0:
        error("Failed to git push.")

    printf('Pushed a commit to git for version "{}".'.format(version))


def git_tag(version):
    # Check to see if this tag already exists
    completed_process = subprocess.run(
        ["git", "tag", "--list", version],
        stdout=subprocess.PIPE,
    )
    if completed_process.returncode != 0:
        error("This is not a git repository.")
    git_output = completed_process.stdout.decode("utf-8")
    tag_exists = git_output is not None and git_output.strip() != ""
    if tag_exists:
        error('The tag of "{}" already exists in this repository.'.format(version))

    # Make the tag and push it
    completed_process = subprocess.run(
        ["git", "tag", version],
    )
    if completed_process.returncode != 0:
        error("Failed to git tag.")
    completed_process = subprocess.run(
        ["git", "push", "--tags"],
    )
    if completed_process.returncode != 0:
        error("Failed to git push.")


def error(msg):
    printf("Error: {}".format(msg))
    sys.exit(1)


def printf(msg):
    print(msg, flush=True)


if __name__ == "__main__":
    main()
