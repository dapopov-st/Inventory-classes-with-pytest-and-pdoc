"""
Tests for the GPU class
Command line: python -m pytest computer_builds/tests/test_gpu.py
or pytest 
if added conftest.py to the directory right above computer builds and that directory does not have __init__.py
"""
import pytest
from computer_builds.models.resources import GPU

invalid_values = [
    {
        'name': '',
        'manufacturer': 'Dell',
        'total': 100,
        'allocated': 10
    },
    {
        'name': 'Joe',
        'manufacturer': '',
        'total': 100,
        'allocated': 10
    },
    {
        'name': 'Joe',
        'manufacturer': 'Dell',
        'total': 0,
        'allocated': 10
    },
    {
        'name': 'Joe',
        'manufacturer': 'Dell',
        'total': 100,
        'allocated': -10
    },


    {
        'name': 'Joe',
        'manufacturer': 'Dell',
        'total': 100,
        'allocated': 10
    },
    {
        'name': 'Joe',
        'manufacturer': 'Dell',
        'total': 100,
        'allocated': 10
    },
    {
        'name': 'Joe',
        'manufacturer': 'Dell',
        'total': 100,
        'allocated': 10
    },
    {
        'name': 'Joe',
        'manufacturer': 'Dell',
        'total': 100,
        'allocated': 10
    },
    {
        'name': 'Joe',
        'manufacturer': 'Dell',
        'total': 100,
        'allocated': 10
    },
]


@pytest.fixture
def gpu_values():
    return {
        'name': 'Joe',
        'manufacturer': 'Dell',
        'total': 100,
        'allocated': 10
    }


@pytest.fixture
def gpu(gpu_values):
    return GPU(**gpu_values)


def test_make_gpu_valid(gpu_values, gpu):
    for attribute in gpu_values:
        assert getattr(gpu, attribute) == gpu_values.get(attribute)


@pytest.mark.parametrize('name, manufacturer, total, allocated', invalid_values)
def test_create_invalid_vals(name, manufacturer, total, allocated):
    with pytest.raises(ValueError):
        GPU(name, manufacturer, total,
            allocated)


def test_category(gpu):
    assert 'gpu' == gpu.category


def test_repr(gpu):
    assert (repr(gpu) == f"\nResource: {gpu.name}\nManufacturer: {gpu.manufacturer}\nTotal available: {gpu.total}\n" +
            f"Allocated resource: {gpu._allocated}")
