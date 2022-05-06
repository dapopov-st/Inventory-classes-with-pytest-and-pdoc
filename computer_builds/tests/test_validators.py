"""
Tests for the functions in the validators.py module
Command line: python -m pytest computer_builds/tests/test_validators.py
or pytest 
if added conftest.py to the directory right above computer builds and that directory does not have __init__.py
"""

from computer_builds.utils.validators import set_if_valid_int, set_if_valid_string, set_if_valid_cores
import pytest


class TestIntegers:
    def test_valid_int(self):
        set_if_valid_int(10)

    def test_raise_int_ValueError(self):
        with pytest.raises(ValueError):
            set_if_valid_int(-5)


class TestStrings:
    def test_valid_str(self):
        set_if_valid_string("ABC 10_20")

    def test_raise_str_ValueError(self):
        with pytest.raises(ValueError):
            set_if_valid_string("  ")


class TestCores:
    def test_valid_cores(self):
        set_if_valid_cores(2)

    def test_raise_neg_cores_ValueError(self):
        with pytest.raises(ValueError) as ex:
            set_if_valid_cores(3.4)
        assert "valid positive" in str(ex.value)

    def test_raise_out_of_range_cores_ValueError(self):
        with pytest.raises(ValueError) as ex:
            set_if_valid_cores(3)
        assert "valid core" in str(ex.value)
