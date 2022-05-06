"""
Tests for the CPU class
Command line: python -m pytest computer_builds/tests/test_cpu.py
or pytest 
if added conftest.py to the directory right above computer builds and that directory does not have __init__.py
"""
import pytest
from computer_builds.models.resources import CPU

invalid_values = [
    {
        'name': '',
        'manufacturer': 'Dell',
        'total': 100,
        'allocated': 10,
        'cores': 4,
        'socket': 'AM4',
        'power_watts': 94
    },
    {
        'name': 'Joe',
        'manufacturer': '',
        'total': 100,
        'allocated': 10,
        'cores': 4,
        'socket': 'AM4',
        'power_watts': 94
    },
    {
        'name': 'Joe',
        'manufacturer': 'Dell',
        'total': 0,
        'allocated': 10,
        'cores': 4,
        'socket': 'AM4',
        'power_watts': 94
    },
    {
        'name': 'Joe',
        'manufacturer': 'Dell',
        'total': 100,
        'allocated': -10,
        'cores': 4,
        'socket': 'AM4',
        'power_watts': 94
    },


    {
        'name': 'Joe',
        'manufacturer': 'Dell',
        'total': 100,
        'allocated': 10,
        'cores': 1,
        'socket': 'AM4',
        'power_watts': 94
    },
    {
        'name': 'Joe',
        'manufacturer': 'Dell',
        'total': 100,
        'allocated': 10,
        'cores': -1,
        'socket': 'AM4',
        'power_watts': 94
    },
    {
        'name': 'Joe',
        'manufacturer': 'Dell',
        'total': 100,
        'allocated': 10,
        'cores': 102,
        'socket': 'AM4',
        'power_watts': 94
    },
    {
        'name': 'Joe',
        'manufacturer': 'Dell',
        'total': 100,
        'allocated': 10,
        'cores': 102,
        'socket': '',
        'power_watts': 94
    },
    {
        'name': 'Joe',
        'manufacturer': 'Dell',
        'total': 100,
        'allocated': 10,
        'cores': 102,
        'socket': 'AM4',
        'power_watts': 0
    },
]


@pytest.fixture
def cpu_values():
    return {
        'name': 'Joe',
        'manufacturer': 'Dell',
        'total': 100,
        'allocated': 10,
        'cores': 4,
        'socket': 'AM4',
        'power_watts': 94
    }


@pytest.fixture
def cpu(cpu_values):
    return CPU(**cpu_values)


def test_make_cpu_valid(cpu_values, cpu):
    for attribute in cpu_values:
        assert getattr(cpu, attribute) == cpu_values.get(attribute)


@pytest.mark.parametrize('name, manufacturer, total, allocated, cores, socket, power_watts', invalid_values)
def test_create_invalid_vals(name, manufacturer, total, allocated, cores, socket, power_watts):
    with pytest.raises(ValueError):
        CPU(name, manufacturer, total,
            allocated, cores, socket, power_watts)


def test_category(cpu):
    assert 'cpu' == cpu.category


def test_repr(cpu):
    assert "Socket" in repr(cpu)
