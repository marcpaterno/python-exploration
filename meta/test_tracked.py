import pytest
from tracked import Tracked


class Derived(Tracked):
    def __init__(self, a, bb, xyz):
        self.a = a
        self.bb = bb
        self.xyz = xyz


def test_1():
    d = Derived(1, "cow", 1.5)
    assert d.a == 1
    assert d.bb == "cow"
    assert d.xyz == 1.5
    assert d.short_names == ["a", "bb"]
