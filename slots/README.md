# Slots and subclasses

One use of `__slots__` is to make sure that class instances do not "grow" additional instance variables.
That is, we want to make sure that every instance of a class has only the instance variables introduced in the `__init__` method.
Having a `__slots__` member avoids having a `__dict__` instance variable.

How do we make sure that *derived* classes do not introduce a new instance variable that causes a new `__dict__` to appear?

This part of the demo uses a local virtual environment to provide pytest.
To create the appropriate environment, use

    python3 -m pip venv local-venv
    source local-venv/bin/activate
    python -m pip install pytest

In further shell sessions (after the environment has been created), one only needs to activate the environment before use.
