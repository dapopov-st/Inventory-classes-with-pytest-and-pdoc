"""
Tests for the Storage class
Command line: python -m pytest computer_builds/tests/test_storage.py
or pytest 
if added conftest.py to the directory right above computer builds and that directory does not have __init__.py
"""
import pytest
from computer_builds.models.resources import Storage

invalid_values = [{
    'name': '',
    'manufacturer': 'Dell',
    'total': 100,
    'allocated': 10,
    'capacity_GB': 20

},
    {
    'name': 'Joe',
    'manufacturer': '',
    'total': 100,
    'allocated': 10,
    'capacity_GB': 20
},
    {
    'name': 'Joe',
    'manufacturer': '',
    'total': -100,
    'allocated': 10,
    'capacity_GB': 20
},
    {
    'name': 'Joe',
    'manufacturer': '',
    'total': 100,
    'allocated': -10,
    'capacity_GB': 20
},
    {
    'name': 'Joe',
    'manufacturer': '',
    'total': 100,
    'allocated': -10,
    'capacity_GB': -20
}
]


@pytest.fixture
def storage_values():
    return {
        'name': 'Joe',
        'manufacturer': 'Dell',
        'total': 100,
        'allocated': 10,
        'capacity_GB': 20
    }


@pytest.fixture
def storage(storage_values):
    return Storage(**storage_values)


def test_make_storage_valid(storage_values, storage):
    for attribute in storage_values:
        assert getattr(storage, attribute) == storage_values.get(attribute)


@pytest.mark.parametrize('name, manufacturer, total, allocated, capacity_GB', invalid_values)
def test_create_invalid_allocated_value(name, manufacturer, total, allocated, capacity_GB):
    with pytest.raises(ValueError):
        Storage(name, manufacturer, total, allocated, capacity_GB)


def test_category(storage):
    assert 'storage' == storage.category


def test_repr(storage):
    assert (repr(storage) == f"\nResource: {storage.name}\nManufacturer: {storage.manufacturer}\nTotal available: {storage.total}\n" +
            f"Allocated resource: {storage._allocated}"+f"\nCapacity in GB: {storage._capacity_GB}")
