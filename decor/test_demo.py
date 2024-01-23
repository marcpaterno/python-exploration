import pytest
from demo import State, Thing


def test_new_thing_is_initialized():
    x = Thing("Laura")
    assert x.state == State.INITIALIZED


def test_say_howdy_before_read_fails():
    x = Thing("Laura")
    with pytest.raises(
        AssertionError, match="read\\(\\) must be called before say_howdy\\(\\)."
    ):
        x.say_howdy()


def test_read_ends_in_right_state():
    x = Thing("Laura")
    x.read()
    assert x.state == State.READY


def test_say_howdy_after_read_works():
    x = Thing("Laura")
    x.read()
    x.say_howdy()
    assert x.state == State.UPDATED


def test_calling_read_twice_fails():
    x = Thing("Laura")
    x.read()
    with pytest.raises(AssertionError, match="read\\(\\) can only be called once."):
        x.read()


def test_calling_foo_before_read_fails():
    x = Thing("Laura")
    with pytest.raises(AssertionError, match=r"read\(\) must be called before foo\(\)"):
        x.foo()


def test_calling_foo_after_read_does_not_change_state():
    x = Thing("Laura")
    x.read()
    old_state = x.state
    x.foo()
    assert x.state == old_state
    assert x.state == State.READY


def test_calling_foo_after_say_howdy_does_not_change_state():
    x = Thing("Laura")
    x.read()
    x.say_howdy()
    old_state = x.state
    x.foo()
    assert x.state == old_state
    assert x.state == State.UPDATED
