import functools
from enum import Enum
from typing import Callable, List, Union, Optional, TypeVar
from typing_extensions import ParamSpec  # Remove when we move to Python 3.10


class State(Enum):
    """The states used in GaussFamily."""

    INITIALIZED = 1
    READY = 2
    UPDATED = 3


T = TypeVar("T")
P = ParamSpec("P")


# See https://peps.python.org/pep-0612/ and
# https://stackoverflow.com/questions/66408662/type-annotations-for-decorators
# for how to specify the types of *args and **kwargs, and the return type of
# the method being decorated.


def enforce_states(
    *,
    initial: Union[State, List[State]],
    final: Optional[State] = None,
    failure_message: str,
) -> Callable[[Callable[P, T]], Callable[P, T]]:
    # Return type seems like it should be Callable[P, T]
    """This decorator wraps a method, and enforces state machine behavior. If
    the object is not in one of the states in initial_states, an
    AssertionError is raised with the given failure_message.
    If final_state is None, the state of the object is not modified.
    If final_state is not None, then the call to the wrapped method returns
    normally, the state of the object is set to final_state"""
    if isinstance(initial_states, list):
        initials = initial_states
    else:
        initials = [initial_states]

    def decorator_enforce_states(func: Callable[P, T]) -> Callable[P, T]:
        # def decorator_enforce_states(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper_repeat(*args: P.args, **kwargs: P.kwargs) -> T:
            assert isinstance(args[0], Thing)
            assert args[0].state in initials, failure_message
            value = func(*args, **kwargs)
            if final_state is not None:
                args[0].state = final_state
            return value

        return wrapper_repeat

    return decorator_enforce_states


class Thing:
    def __init__(self, n: str) -> None:
        self.name: str = n
        self.state: State = State.INITIALIZED

    def is_ready(self) -> bool:
        return self.state in (State.READY, State.UPDATED)

    @enforce_states(
        initial=State.INITIALIZED,
        final=State.READY,
        failure_message="read() can only be called once.",
    )
    def read(self) -> None:
        pass

    @enforce_states(
        initial_states=[State.READY, State.UPDATED],
        final_state=State.UPDATED,
        failure_message="read() must be called before say_howdy().",
    )
    def say_howdy(self) -> None:
        print(f"Howdy {self.name}")

    @enforce_states(
        initial_states=[State.UPDATED, State.READY],
        failure_message="read() must be called before foo().",
    )
    def foo(self) -> None:
        print(f"{self.name} says foo")
