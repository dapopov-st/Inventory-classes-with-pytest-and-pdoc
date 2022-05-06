"""
Validator functions for Resources and its subclasses
"""


def set_if_valid_string(string):
    if isinstance(string, str) and len(string.strip()) > 0:
        return string.strip()
    else:
        raise ValueError("Must be a valid string")


def set_if_valid_int(integer_):
    if isinstance(integer_, int) and integer_ > 0:
        return integer_
    else:
        raise ValueError("Must be a nonnegative integer")


def set_if_valid_cores(integer_):
    options = [i*2 for i in range(1, 51)]
    if not isinstance(integer_, int) or integer_ < 0:
        raise ValueError("Must be a valid positive integer number of cores")

    if integer_ in options:
        return integer_
    else:
        raise ValueError(f"Must be a a valid core in {options}")
