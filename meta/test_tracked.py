import pytest
from tracked import Tracked


class Derived(Tracked):
    def __init__(self, a, bb, xyz):
        """The names 'a' and 'bb' will be in short_names, but not xyz"""
        self.a = a
        self.bb = bb
        self.xyz = xyz

    def ff(self):
        """Silly method to make sure method names do not get found"""
        return 1

    def grow_wart(self):
        self.z = True


def test_1():
    d = Derived(1, "cow", 1.5)
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
