""" This code demonstrates that the rebinding of a name
passed to a new value does not change the value associated
with that name in the caller.

This is true even when the name in question is 'self'.
"""
class C:
    def __init__(self, i):
        self.i = i

    def foo(self):
        return self.i

    def nuke_me(self):
        # We can re-bind the name self to a different value. But this does
        # not change the object that was passed into the method; it only
        # changes the the local binding.
        assert self is not None
        self = None
        assert self is None


def main():
    obj1 = C(10)
    print(f"obj1.i: {obj1.i}")
    obj1.nuke_me()
    print(f"obj1.i: {obj1.i}")


if __name__ == "__main__":
    main()
