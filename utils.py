
from enum import Enum

prefix = ['x', 'mono', 'bi', 'tri', 'tetra', 'penta', 'hexa']

# class syntax
class elementKind(Enum):
    NoMetal = 1
    Metal = 2
    SemiMetal = 3
    GasNoble = 4
    
def contains(list, target):
    for item in list:
        if item.element.simb == target.element.simb and item.charge == target.charge:
            return True
    return False

def getIndexOf(list, target):
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return 0