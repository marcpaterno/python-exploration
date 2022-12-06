"""A module to demonstrate the use of a context manager to manage the lifetime of a library.
"""

import dummy_util


class Counter:
    """Demo of a context manager class for controlling initialization and
    finalization of a library."""

    def __enter__(self):
        """Entering the context of the manager initializes the library."""
        dummy_util.initialize()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """Existing the context of the manager finalizes the library."""
        dummy_util.finalize()
        # Production-quality code would handle exc_type, exc_value and traceback
        # being other than None.
        return False

    def increment(self):
        """Increment the count"""
        dummy_util.increment()

    def get_count(self):
        """Return the current count."""
        return dummy_util.get_count()


def use_counter():
    return Counter()


if __name__ == "__main__":
    with use_counter() as c:
        print("Start of the context")
        print(f"The count starts at {c.get_count()}")
        for _ in range(11):
            c.increment()
        print(f"The count ends at {c.get_count()}")
        print("Exiting context")
