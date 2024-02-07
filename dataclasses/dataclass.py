from dataclasses import dataclass
import numpy as np
from time import time as now


@dataclass(frozen=True)
class Position:
    __slots__ = ["x", "y"]
    x: np.ndarray
    y: np.ndarray


size = 1 * 1000

if __name__ == "__main__":
    from timeit import timeit

    print(f"Time for creating {size} dataclass objects:")
    print(timeit("p1 = Position(x=np.ones(size), y=np.ones(size))", globals=globals()))
    print(f"Time for creating {size} dictionary objects:")
    print(timeit("p2 = {'x': np.ones(size), 'y': np.ones(size)}", globals=globals()))
