"""Polyfill string functions."""

from sys import version_info


def removeprefix(string: str, prefix: str) -> str:
    """
    Return a str with the given prefix string removed if present.

    If the string starts with the prefix string, return string[len(prefix):].
    Otherwise, return a copy of the original string.
    """
    if version_info[0:2] >= (3, 9):
        return string.removeprefix(prefix)
    elif string.startswith(prefix):
        return string[len(prefix):]
    return string


def removesuffix(string: str, suffix: str) -> str:
    """
    Return a str with the given suffix string removed if present.

    If the string ends with the suffix string and that suffix is not empty,
    return string[:-len(suffix)]. Otherwise, return a copy of the original
    string.
    """
    if version_info[0:2] >= (3, 9):
        return string.removesuffix(suffix)
    elif string.endswith(suffix):
        return string[:-len(suffix)]
    return string
