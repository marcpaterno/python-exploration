from dataclasses import dataclass
import numpy as np

@dataclass(frozen = True)
class Position:
    __slots__ = ['x', 'y']
    x: np.ndarray
    y: np.ndarray

size = 100 * 1000

p1 = Position(x=np.ones(size), y=np.ones(size))

p2 = {'x': np.ones(size), 'y': np.ones(size) }
