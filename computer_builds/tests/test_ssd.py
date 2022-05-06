"""
Tests for the SSD class
Command line: python -m pytest computer_builds/tests/test_ssd.py
or pytest 
if added conftest.py to the directory right above computer builds and that directory does not have __init__.py
"""
import pytest
from computer_builds.models.resources import SSD

invalid_values = [{
    'name': '',
    'manufacturer': 'Dell',
    'total': 100,
    'allocated': 10,
    'capacity_GB': 20,
    'interface': "PCIe NVMe 3.0 x4"

},
    {
    'name': 'Joe',
    'manufacturer': '',
    'total': 100,
    'allocated': 10,
    'capacity_GB': 20,
    'interface': "PCIe NVMe 3.0 x4"
},
    {
    'name': 'Joe',
    'manufacturer': '',
    'total': -100,
    'allocated': 10,
    'capacity_GB': 20,
    'interface': "PCIe NVMe 3.0 x4"
},
    {
    'name': 'Joe',
    'manufacturer': '',
    'total': 100,
    'allocated': -10,
    'capacity_GB': 20,
    'interface': "PCIe NVMe 3.0 x4"
},
    {
    'name': 'Joe',
    'manufacturer': '',
    'total': 100,
    'allocated': -10,
    'capacity_GB': -20,
    'interface': "PCIe NVMe 3.0 x4"
},
    {
    'name': 'Joe',
    'manufacturer': '',
    'total': 100,
    'allocated': -10,
    'capacity_GB': -20,
    'interface': 4
},
    {
    'name': 'Joe',
    'manufacturer': '',
    'total': 100,
    'allocated': -10,
    'capacity_GB': -20,
    'interface': ""
}
]


@pytest.fixture
def ssd_values():
    return {
        'name': 'Joe',
        'manufacturer': 'Dell',
        'total': 100,
        'allocated': 10,
        'capacity_GB': 20,
        'interface': "PCIe NVMe 3.0 x4"

    }


@pytest.fixture
def ssd(ssd_values):
    return SSD(**ssd_values)


def test_make_ssd_valid(ssd_values, ssd):
    for attribute in ssd_values:
        assert getattr(ssd, attribute) == ssd_values.get(attribute)


@pytest.mark.parametrize('name, manufacturer, total, allocated, capacity_GB, interface', invalid_values)
def test_create_invalid_allocated_value(name, manufacturer, total, allocated, capacity_GB, interface):
    with pytest.raises(ValueError):
        SSD(name, manufacturer, total, allocated, capacity_GB, interface)


def test_category(ssd):
    assert 'ssd' == ssd.category


def test_repr(ssd):
    assert "Interface" in repr(ssd)
