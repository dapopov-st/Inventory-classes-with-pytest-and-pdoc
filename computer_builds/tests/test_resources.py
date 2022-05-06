"""
Tests for Resources class
Command line: python -m pytest computer_builds/tests/test_resources.py
or pytest 
if added conftest.py to the directory right above computer builds and that directory does not have __init__.py
"""

# See:https://stackoverflow.com/questions/10253826/path-issue-with-pytest-importerror-no-module-named-yadayadayada
# pytest adds the parent directory of the conftest.py to the sys.path
import pytest
from computer_builds.models.resources import Resources

invalid_values = [{
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
    'manufacturer': '',
    'total': -100,
    'allocated': 10
},
    {
    'name': 'Joe',
    'manufacturer': '',
    'total': 100,
    'allocated': -10
}
]


@pytest.fixture
def resource_values():
    return {
        'name': 'Joe',
        'manufacturer': 'Dell',
        'total': 100,
        'allocated': 10
    }


@pytest.fixture
def resource(resource_values):
    return Resources(**resource_values)


def test_make_resource_valid(resource_values, resource):
    for attribute in resource_values:
        assert getattr(resource, attribute) == resource_values.get(attribute)


@pytest.mark.parametrize('name, manufacturer, total, allocated', invalid_values)
def test_create_invalid_allocated_value(name, manufacturer, total, allocated):
    with pytest.raises(ValueError):
        Resources(name, manufacturer, total, allocated)


def test_total(resource, resource_values):
    assert resource_values['total'] == resource.total == resource._total


def test_allocated(resource, resource_values):
    assert resource_values['allocated'] == resource.allocated == resource._allocated


def test_allocated_gt_total():
    with pytest.raises(ValueError):
        Resources(name='GIntel Core i9-9900K',
                  manufacturer='GNvidia', total=100, allocated=150)


def test_claim(resource):
    n = 50
    resource.orig_allocated = resource.allocated
    resource.orig_total = resource.total
    resource.claim(n)
    assert resource.allocated == resource.orig_allocated+n
    assert resource.total == resource.orig_total


@pytest.mark.parametrize('n', [110, 0, -10])
def test_claim_invalid(resource, n):
    with pytest.raises(ValueError) as er:
        resource.claim(n)
    #assert "cannot exceed" in str(er.value)


def test_freeup(resource):
    n = 5
    resource.orig_allocated = resource.allocated
    resource.orig_total = resource.total
    resource.freeup(n)
    assert resource.allocated == resource.orig_allocated-n
    assert resource.total == resource.orig_total


@pytest.mark.parametrize('n', [110, 0, 11, -10])
def test_freeup_invalid(resource, n):
    with pytest.raises(ValueError) as er:
        resource.freeup(n)


def test_died(resource):
    n = 3
    resource.orig_allocated = resource.allocated
    resource.orig_total = resource.total
    resource.died(n)
    assert resource.allocated == resource.orig_allocated-n
    assert resource.total == resource.orig_total-n


@pytest.mark.parametrize('n', [110, 0.-10])
def test_died_invalid(resource, n):
    with pytest.raises(ValueError) as er:
        resource.died(n)


def test_purchased(resource):
    n = 3
    resource.orig_allocated = resource.allocated
    resource.orig_total = resource.total
    resource.purchased(n)
    assert resource.allocated == resource.orig_allocated
    assert resource.total == resource.orig_total+n


@pytest.mark.parametrize('n', [0, -10])
def test_purchased_invalid(resource, n):
    with pytest.raises(ValueError) as er:
        resource.purchased(n)


def test_category(resource):
    assert resource.category == 'resources'


def test_str(resource):
    assert str(resource) == resource.name


def test_repr(resource):
    assert (repr(resource) == f"\nResource: {resource.name}\nManufacturer: {resource.manufacturer}\nTotal available: {resource.total}\n" +
            f"Allocated resource: {resource._allocated}")
