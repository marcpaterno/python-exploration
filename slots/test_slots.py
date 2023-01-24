import pytest
from slots import Derived, BadDerived, BadLateAssignment


def test_derived():
    d1 = Derived(2, "cow")
    assert not hasattr(d1, "__dict__")
    assert hasattr(d1, "__slots__")
    assert d1.basevar == 2
    assert d1.newvar == "cow"


def test_bad():
    with pytest.raises(AttributeError):
        _ = BadDerived()

def test_late():
    x = BadLateAssignment()
    assert x.basevar == 4
    with pytest.raises(AttributeError):
        x.some_function()
