import pytest
from tracked import Tracked


class Child(Tracked):
    def __init__(self, a, bb, xyz):
        """The names 'a' and 'bb' will be in short_names, but not xyz"""
        super().__init__()
        self.a = a
        self.bb = bb
        self.xyz = xyz

    def ff(self):
        """Silly method to make sure method names do not get found"""
        return 1

    def grow_wart(self):
        self.z = True


class Grandchild(Child):
    def _init__(self, a, bb, xyz, cc):
        super.__init__(a, bb, xyz)
        self.cc = cc


def test_child():
    d = Child(1, "cow", 1.5)
    # Make sure the instance variables we initialized are as expected...
    assert d.a == 1
    assert d.bb == "cow"
    assert d.xyz == 1.5

    # Make sure short_names contains all the right values and no wrong values...
    assert d.short_names == ["a", "bb"]

    # Call the function that adds a new instance variable, make sure it is as
    # expected...
    d.grow_wart()
    assert d.z

    # Verify that short_names has not grown a new value.
    assert d.short_names == ["a", "bb"]


def test_grandchild():
    g = Grandchild(1, "cow", 1.5, [1])
    # Make sure the instance variables we initialized are as expected...
    assert g.a == 1
    assert g.bb == "cow"
    assert g.xyz == 1.5
    assert g.cc == [1]

    # Make sure short_names contains all the right values and no wrong values...
    assert g.short_names == ["a", "bb", "cc"]

    # Call the function that adds a new instance variable, make sure it is as
    # expected...
    g.grow_wart()
    assert g.z

    # Verify that short_names has not grown a new value.
    assert g.short_names == ["a", "bb", "cc"]
