# vim: encoding=utf-8 ts=4 et sts=4 sw=4 tw=79 fileformat=unix nu wm=2
import hashlib
import json
import os
import shutil
import sys
import zipfile
from uuid import uuid4
from pkg_resources import parse_version as get_version
from . import log, utils


# try import the requests module
try:
    import requests
except ImportError:
    log.fatal('the requests module is required, please pip install requests')
    sys.exit(1)


def options(mainparser):
    """Argparse options added to the cli."""
    parser = mainparser.add_parser('package', help='package actions')
    subparser = parser.add_subparsers(
        dest='package',
        required=True,
        help='package',
    )
    parser_build = subparser.add_parser(
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
    parser_install = subparser.add_parser(
        'install',
        help='install package',
    )
    parser_install.set_defaults(func=install)
    parser_install.add_argument(
        '--pkg',
        required=True,
        help='plugin a28 package file',
    )


def build(args):
    """Build package."""
    src = args.src
    dest = args.dest
    meta = get_info(src)
    pkg = package(src, dest, meta)
    utils.message(pkg)


def install(args):
    """install / update the local package."""
    pkg_hash = generate_hash(args.pkg)
    meta = extract_meta(args.pkg)
    meta['hash'] = pkg_hash
    install_local(args.pkg, meta)
    utils.message('installed {}'.format(meta['name']))


def extract_meta(pkg):
    """Extract the meta information from a packaged package."""
    with zipfile.ZipFile(pkg, 'r') as z:
        package = next(x for x in z.namelist() if x.endswith('package.json'))
        with z.open(package) as manifest:
            return get_info(manifest, True)


def get_info(src, extracted=False):
    """Get information about a package by using a combination of the data in
    the src package.json file and the manifest.json file.
    """
    if extracted:
        data = json.load(src)
    else:
        package = os.path.join(src, 'package.json')
        with open(package) as package_data:
            data = json.load(package_data)

    # load the manifest data
    manifest = os.path.join(utils.STORAGE, 'manifest.json')
    with open(manifest) as manifest_data:
        m_data = json.load(manifest_data)

    # copy data from the manifest package if exists
    if data['name'] in m_data['packages']:
        m_package = m_data['packages'][data['name']]
        data['identifier'] = m_package['identifier']
    else:
        data['identifier'] = str(uuid4())
    return data


def validate():
    """Check the package is correctly structured."""
    return True


def install_local(pkg, meta):
    """Install a package locally by updating the manifest.json without
    touching the etag.json file. This will be overwritten when a new official
    manifest.json is published."""
    dest = os.path.join(utils.STORAGE, 'cache')
    shutil.copy(pkg, dest)
    manifest = os.path.join(utils.STORAGE, 'manifest.json')
    with open(manifest, 'r+') as manifest_data:
        data = json.load(manifest_data)
        data['packages'][meta['name']] = meta
        if meta['name'] not in data['required']:
            data['required'].append(meta['name'])
        manifest_data.seek(0)
        json.dump(data, manifest_data, indent=4)
        manifest_data.truncate()


def package(src, dest, meta):
    """Build an a28 package from the provided src directory. The package will
    be saved to the dest directory. A package needs to be provided containing
    at least an identifier and a version number."""
    version = meta['version']
    identifier = meta['identifier']
    filename = '{}-{}.{}'.format(identifier, version, 'a28')
    filename = os.path.join(dest, filename)

    if not os.path.exists(dest):
        os.makedirs(dest)

    a28 = zipfile.ZipFile(filename, 'w', zipfile.ZIP_DEFLATED)
    exclude = (['build', '.vscode'])
    for root, dirs, files in os.walk(src, topdown=True):
        dirs[:] = [d for d in dirs if d not in exclude]
        for current in files:
            i_file = os.path.join(root, current)
            fl = os.path.relpath(
                os.path.join(root, current),
                os.path.join(src, '..', '..'),
            )
            a28.write(i_file, fl)
    a28.close()
    return filename


def fetch(url='https://packages.a28.io/manifest.json', dest=None):
    """Fetch the manifest from it's online source."""
    etag = os.path.join(utils.STORAGE, 'manifest.etag')
    request = requests.head(url, allow_redirects=True)
    latest = request.headers['ETag']
    request.close()

    with open(etag, 'w+') as file:
        current = file.read().replace('\n', '')
        if get_version(latest) > get_version(current):
            file.write(latest)
            request = requests.get(url, allow_redirects=True)
            with open(dest, 'wb') as manifest:
                manifest.write(request.content)
            request.close()


def generate_hash(pkg):
    """Generate a hash for a package."""
    sha256_hash = hashlib.sha256()
    with open(pkg, 'rb') as f:
        # read and update hash string value in blocks of 4K
        for byte_block in iter(lambda: f.read(4096), b''):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()


def prebuild(src):
    """Execute any pre-build scripts. Usually used to create installable
    tarballs for applications.
    """
