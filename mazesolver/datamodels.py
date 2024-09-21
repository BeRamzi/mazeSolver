from dataclasses import dataclass , asdict,astuple
from typing import Dict, Tuple, List
import numpy as np
from enum import Enum, auto()
class UpDown(Enum):
    Up = auto()
    Down = auto()

class LeftRight(Enum):
    Left = auto()
    Right = auto()

@dataclass
class Size:
    x:int
    y:int


@dataclass
class Point:
    x:int
    y:int
    def move()
@dataclass
class Maze:
    array: np.ndarray 

    
    

Moves={"up_":()} 
    
