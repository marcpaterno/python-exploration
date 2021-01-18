from dataclasses import dataclass
import numpy as np
from time import time as now


@dataclass(frozen=True)
class Position:
    __slots__ = ["x", "y"]
    x: np.ndarray
    y: np.ndarray


size = 100 * 1000

if __name__ == "__main__":
    from timeit import timeit

    print(timeit("p1 = Position(x=np.ones(size), y=np.ones(size))", globals=globals()))
    print(timeit("p2 = {'x': np.ones(size), 'y': np.ones(size)}", globals=globals()))
