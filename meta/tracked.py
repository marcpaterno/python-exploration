"""The module `tracked` provides the class `Tracked`.

Classes can inherit from `Tracked` to obtain an instance variable
`short_names`, which is a list containing the names of all instance
variables with length 1 or 2 established by the `__init__` method
of the class that inherits from `Tracked`."""


class Tracked:
    """Classes that inherit from `Tracked` obtain an instance variable
    `short_names` which is a list containing the names of all instance
    variables with length of 1 or 2 established by the `__init__` method
    of the class that inherits from `Tracked`."""

    def __init_subclass__(cls, *args, **kwargs):
        """Called when Tracked is subclassed, with `cls` as the new
        subclass."""

        # Capture the old __init__ method...
        old_init = cls.__init__
        # Create the method new_init, that calls the old one and then does the new work.
        def new_init(self, *args, **kwargs):
            old_init(self, *args, **kwargs)
            self.short_names = [n for n in vars(self) if len(n) <= 2]

        # Replace the __init__ method with our new one.
        cls.__init__ = new_init
