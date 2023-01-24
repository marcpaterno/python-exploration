"""Demonstration of the use of __slots__.
"""
#  pylint: disable-msg=too-few-public-methods


class ForceSlots(type):
    """This is a metaclass to enforce that classes do not accidentally
    introduce a __dict__.
    """

    @classmethod
    def __prepare__(cls, name, bases, **kwds):
        """Return a class namespace that contains __slots__ in order
        to suppress the generation of __dict__.
        """
        # calling super is not strictly necessary because
        #  type.__prepare() simply returns an empty dict.
        # But if you plan to use metaclass-mixins then this is essential!
        super_prepared = super().__prepare__(cls, name, bases, **kwds)
        super_prepared["__slots__"] = ()
        return super_prepared


class Base(metaclass=ForceSlots):
    """Base class that has __slots__ and so no __dict__."""

    __slots__ = ["basevar"]

    def __init__(self, var):
        """Create a Base with basevar set to var."""
        self.basevar = var


class Derived(Base):
    """Derived class that adds a new instance variable the wrong way.
    It ends up having both __slots__ and __dict__.
    """

    __slots__ = ("newvar",)

    def __init__(self, basevar, newvar):
        """Create an instance of Derived with the given basevar and newvar."""
        super().__init__(basevar)

        self.newvar = newvar


class BadDerived(Base):
    """You can't create an instance of this class, because assigning a new
    instance variable that is not in __slots__ fails.
    """

    def __init__(self):
        super().__init__(3)
        self.cannot_add_a_new_instance_variable_without_a_slot = 3


class BadLateAssignment(Base):
    """You can't create an instance of this class because of the late assignment."""

    def __init__(self):
        """Initialize only the base, no new instance variables."""
        super().__init__(4)

    def some_function(self):
        """Calling this function creates a new instance variable."""
        self.newthing = "dog"
