from polyfill3 import __version__
from polyfill3.string import removeprefix, removesuffix

def test_version():
    assert __version__ == '0.1.0'


def test_removeprefix_prefix_found():
    assert removeprefix('TEST_CASE', 'TEST_') == 'CASE'

def test_removeprefix_prefix_not_found():
    assert removeprefix('TEST_CASE', 'BLAH_') == 'TEST_CASE'


def test_removesuffix_suffix_found():
    assert removesuffix('TEST_CASE', '_CASE') == 'TEST'

def test_removesuffix_suffix_not_found():
    assert removesuffix('TEST_CASE', '_BLAH') == 'TEST_CASE'

