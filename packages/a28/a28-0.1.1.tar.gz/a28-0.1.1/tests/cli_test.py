# flake8: noqa
import subprocess  # noqa: I005 S404


def capture(command):
    proc = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    out, err = proc.communicate()
    return out, err, proc.returncode


def test_a28_no_param():
    command = ['a28']
    out, err, exitcode = capture(command)
    assert exitcode == 2
    assert out == b''
    assert err == b'usage: a28 [-h] [-v] {build,install,exists,clean} ...\na28: error: the following arguments are required: action\n'  # noqa


def test_a28_build_no_param():
    command = ['a28', 'build']
    out, err, exitcode = capture(command)
    assert exitcode == 2
    assert out == b''
    assert err == b'usage: a28 build [-h] --src SRC [--dest DEST]\na28 build: error: the following arguments are required: --src\n'  # noqa


def test_a28_install_no_param():
    command = ['a28', 'install']
    out, err, exitcode = capture(command)
    assert exitcode == 2
    assert out == b''
    assert err == b'usage: a28 install [-h] --pkg PKG\na28 install: error: the following arguments are required: --pkg\n'  # noqa


def test_a28_exists_no_param():
    command = ['a28', 'exists']
    out, err, exitcode = capture(command)
    assert exitcode == 0
    message = b'No configuration exists at '
    assert out[0:len(message)] == message


def test_a28_install_no_param():
    command = ['a28', 'clean']
    out, err, exitcode = capture(command)
    assert exitcode == 0
    message = b'No configuration to clean.'
    assert out[0:len(message)] == b'No configuration to clean.'
