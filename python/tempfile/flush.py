import tempfile

import at
import tf


def main():
    with tempfile.NamedTemporaryFile("w") as fout:
        debug_print(astr)
        fout.write(astr)
        # OK
        fout.flush()
        cmd = [binary_name, fout.name, *[str(path) for path in targets]]


def main_b():
    with tempfile.NamedTemporaryFile("w") as fout:
        debug_print(astr)
        fout.write(astr)
        # OK
        fout.close()
        cmd = [binary_name, fout.name, *[str(path) for path in targets]]


def main_c():
    with tempfile.NamedTemporaryFile("w") as fout:
        debug_print(astr)
        fout.write(astr)

    # OK
    cmd = [binary_name, fout.name, *[str(path) for path in targets]]


def main_c():
    with tempfile.NamedTemporaryFile("w") as fout:
        debug_print(astr)
        fout.write(astr)
        debug_print('wrote file')
        # ruleid:tempfile-without-flush
        cmd = [binary_name, fout.name, *[str(path) for path in targets]]


def main_d():
    fout = tempfile.NamedTemporaryFile('w')
    debug_print(astr)
    fout.write(astr)
    # ruleid:tempfile-without-flush
    fout.name
    cmd = [binary_name, fout.name, *[str(path) for path in targets]]


def main_e():
    fout = tempfile.NamedTemporaryFile('w')
    debug_print(astr)
    fout.write(astr)
    # ruleid:tempfile-without-flush
    print(fout.name)
    cmd = [binary_name, fout.name, *[str(path) for path in targets]]
