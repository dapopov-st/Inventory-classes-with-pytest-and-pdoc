'''
Command line: python -m pytest computer_builds/tests/test_hdd.py or pytest if added
conftest.py to the directory right above computer builds and that directory does not have __init__.py
'''

import pytest
from computer_builds.models.resources import HDD


invalid_values = [{
    'name': '',
    'manufacturer': 'Dell',
    'total': 100,
    'allocated': 10,
    'capacity_GB': 20,
    'size': '2.5"',
    'rpm': 7000

},
    {
    'name': 'Joe',
    'manufacturer': '',
    'total': 100,
    'allocated': 10,
    'capacity_GB': 20,
    'size': '2.5"',
    'rpm': 7000
},
    {
    'name': 'Joe',
    'manufacturer': '',
    'total': -100,
    'allocated': 10,
    'capacity_GB': 20,
    'size': '2.5"',
    'rpm': 7000
},
    {
    'name': 'Joe',
    'manufacturer': '',
    'total': 100,
    'allocated': -10,
    'capacity_GB': 20,
    'size': '2.5"',
    'rpm': 7000
},
    {
    'name': 'Joe',
    'manufacturer': '',
    'total': 100,
    'allocated': -10,
    'capacity_GB': -20,
    'size': '2.5"',
    'rpm': 7000
},
    {
    'name': 'Joe',
    'manufacturer': '',
    'total': 100,
    'allocated': -10,
    'capacity_GB': -20,
    'size': '',
    'rpm': 7000
},
    {
    'name': 'Joe',
    'manufacturer': '',
    'total': 100,
    'allocated': -10,
    'capacity_GB': -20,
    'size': '2.5"',
    'rpm': -7000
}
]


@pytest.fixture
def hdd_values():
    return {
        'name': 'Joe',
        'manufacturer': 'Dell',
        'total': 100,
        'allocated': 10,
        'capacity_GB': 20,
        'size': '2.5"',
        'rpm': 7000

    }


@pytest.fixture
def hdd(hdd_values):
    return HDD(**hdd_values)


def test_make_hdd_valid(hdd_values, hdd):
    for attribute in hdd_values:
        assert getattr(hdd, attribute) == hdd_values.get(attribute)


@pytest.mark.parametrize('name, manufacturer, total, allocated, capacity_GB, size, rpm', invalid_values)
def test_create_invalid_allocated_value(name, manufacturer, total, allocated, capacity_GB, size, rpm):
    with pytest.raises(ValueError):
        HDD(name, manufacturer, total, allocated, capacity_GB, size, rpm)


def test_category(hdd):
    assert 'hdd' == hdd.category


def test_repr(hdd):
    assert "rpm" in repr(hdd)
