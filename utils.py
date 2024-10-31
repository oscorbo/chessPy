
from enum import Enum

prefix = ['mono', 'bi', 'tri', 'tetra', 'penta', 'hexa']

# class syntax
class elementKind(Enum):
    NoMetal = 1
    Metal = 2
    SemiMetal = 3
    GasNoble = 4
    