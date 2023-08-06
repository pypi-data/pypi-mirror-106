#!/usr/bin/env python
#    _                ___ ___   _____       _             _           _
#   /_\  _ _ ___ __ _|_  | _ ) |_   _|__ __| |_  _ _  ___| |___  __ _(_)___ ___
#  / _ \| '_/ -_) _` |/ // _ \   | |/ -_) _| ' \| ' \/ _ \ / _ \/ _` | / -_|_-<
# /_/ \_\_| \___\__,_/___\___/   |_|\___\__|_||_|_||_\___/_\___/\__, |_\___/__/
#                                                               |___/
"""Build packages to be submitted to Area28."""
import argparse
import os
import shutil
import sys

import a28


# set the version to the same as the a28 module
__version__ = a28.__version__


# set the platform type (use startswith to handle old versions with ver nums)
POSIX = os.name == 'posix'
WINDOWS = os.name == 'nt'
LINUX = sys.platform.startswith('linux')
MACOS = sys.platform.startswith('darwin')
OSX = MACOS  # deprecated alias (thanks David F for the reminder)
FREEBSD = sys.platform.startswith('freebsd')
OPENBSD = sys.platform.startswith('openbsd')
NETBSD = sys.platform.startswith('netbsd')
BSD = FREEBSD or OPENBSD or NETBSD
SUNOS = sys.platform.startswith(('sunos', 'solaris'))
AIX = sys.platform.startswith('aix')

# get the users home path for storing files
if POSIX:
    HOMEDIR = os.path.expanduser('~')
elif WINDOWS:
    HOMEDIR = os.environ['APPDATA']
else:
    # unsupported operating system
    HOMEDIR = os.path.realpath(os.sep)

# set the storage constant
if MACOS:
    APP_SUP = os.path.join(HOMEDIR, 'Library', 'Application Support')
    STORAGE = os.path.join(APP_SUP, 'Area28', 'core')
elif WINDOWS:
    STORAGE = os.path.join(HOMEDIR, 'Area28', 'core')
elif POSIX:
    STORAGE = os.path.join(HOMEDIR, '.config', 'area28', 'core')
else:
    STORAGE = os.path.join(HOMEDIR, '.area28', 'core')


def message(msg=''):
    """Display a message to the user."""
    print(msg)


def confirm():
    """Ask the user to confirm that ALL files and directories should be deleted
    from the directory specified by the storage variable. The STORAGE variable
    changes depending on the operating system used.
    """
    message = "Delete ALL configuration data from '{}'? y/n?"
    return bool(input(message.format(STORAGE)) == 'y')


def clean(args):
    """Using the shutil utilities, delete all the files provided in the STORAGE
    directory. If an error occurs, catch the exception and print it out to the
    STDOUT.
    """
    if not os.path.isdir(STORAGE):
        message('No configuration to clean.')
        return

    elif not args.force and not confirm():
        message(f'Not deleting {STORAGE}')
        return

    try:
        shutil.rmtree(STORAGE)
        message(f"Deleted all files and directories in '{STORAGE}'")
    except OSError as e:
        message(f'Error: {STORAGE} : {e.strerror}')


def exists(_):
    """Check if the configuration directory exists."""
    if os.path.isdir(STORAGE):
        message(f"Configuration exists at '{STORAGE}'.")
    else:
        message(f"No configuration exists at '{STORAGE}'.")


def main():
    """Main command line entry point."""
    parser = argparse.ArgumentParser(description='package manager')

    parser.add_argument(
        '-v',
        '--version',
        action='version',
        version='%(prog)s ' + __version__,
    )

    subparsers = parser.add_subparsers(
        dest='action',
        required=True,
        help='actions',
    )

    parser_build = subparsers.add_parser(
        'build',
        help='build package',
    )
    parser_build.set_defaults(func=build)
    parser_build.add_argument(
        '--src',
        required=True,
        help='plugin source directory',
    )
    parser_build.add_argument(
        '--dest',
        default='',
        help='destination directory',
    )

    parser_install = subparsers.add_parser(
        'install',
        help='install package',
    )
    parser_install.set_defaults(func=install)
    parser_install.add_argument(
        '--pkg',
        required=True,
        help='plugin a28 package file',
    )

    parser_exist = subparsers.add_parser(
        'exists',
        help='check if the configuration exists.',
    )
    parser_exist.set_defaults(func=exists)
    parser_clean = subparsers.add_parser(
        'clean',
        help='clean (delete) the configuration permanently.',
    )
    parser_clean.set_defaults(func=clean)
    parser_clean.add_argument(
        '-f',
        '--force',
        action='store_true',
        help='force the configuration to be removed bypassing confirmation',
    )

    args = parser.parse_args()
    args.func(args)


def build(args):
    """Build package."""
    src = args.src
    dest = args.dest
    meta = a28.get_info(src)
    pkg = a28.package(src, dest, meta)
    message(pkg)


def install(args):
    """install / update the local package."""
    pkg_hash = a28.generate_hash(args.pkg)
    meta = a28.extract_meta(args.pkg)
    meta['hash'] = pkg_hash
    a28.install(args.pkg, meta)
    message('installed {}'.format(meta['name']))
