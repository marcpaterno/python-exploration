"""A module to demonstrate how context managers function."""


class Traced:
    """A class that demonstrates how a context manager works."""

    def __init__(self):
        """Context manager objects are created like any other object, using the
        class name as a factory function.

        __init__() is called to initialize the object."""
        print(f"Creating a Traced object {id(self)}")

    def __enter__(self):
        """This is the method called when the context is entered (not when the
        context manager object is created). This is where one would typically
        acquire a resource that must be managed.

        We return self so that the statement body of the `with` statement gets
        this object. Sometimes, one would return a wrapped object insteead."""
        print(f"Entering context for object {id(self)}")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """This is the method called when the context is exited (even if an
        exception is thrown).

        If the statement body did not raise an exception, then all arguments
        except `self` will be None. If an exeption was raised, we get the
        appropriate information.

        We return a boolean value: True if we want the `with` statement to
        suppress the exception, and continue execution with the statement
        following the `with` statement, or False to propagate the exception.
        """
        print(f"Exiting context for object {id(self)}")
        if exc_type:
            print("Exiting with exception of type {exc_type}")
        return False


# Demonstrate the simplest use of the Traced.
with Traced() as m:
    print(f"We are now in the body of the context, using the object {id(m)}")

print("\n\n\n")

# Demonstrate the use of Traced side a generator. When does the context manager
# exit?
def some_numbers(maximum):
    """Generator that yields a sequence of numbers, up to maximum.

    We create a Traced context manager before starting to yield values."""
    print("In some_numbers(), before creating the context manager.")
    with Traced():
        print("In some_numbers, within the context but before the loop")
        for i in range(maximum):
            print(f"About to yield {i}")
            yield i
        print("Before exiting the context manager in the generator")


print("Before calling some_numbers in our for statement...")
for n in some_numbers(5):
    print(f"The for loop got {n}")
print("After the for statement")
