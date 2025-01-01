
from enum import Enum

# sistematica
prefix = ['x', 'mono', 'di', 'tri', 'tetra', 'penta', 'hexa']

# tradicional
prefixTradicional1i = [""]
prefixTradicional1f = ["ico"]

prefixTradicional2i = ["", ""]
prefixTradicional2f = ["oso", "ico"]

prefixTradicional3i = ["hipo", "", ""]
prefixTradicional3f = ["oso", "oso", "ico"]

prefixTradicional4i = ["hipo", "", "", "per"]
prefixTradicional4f = ["oso", "oso", "ico", "ico"]

Volatile_HydridesElements = ["N", "P", "As", "Sb", "C", "Si", "B"]
HydracidsElements = ["F", "Cl", "Br", "I", "S", "Se", "Te"]


# diccionary
# element to root
rootsElements = {
  'O' : "Oxido",
  '(O2)' : "Peroxido",
  'H' : "Hidrudo",

    # ????
  'Cl' : "Cloruro",
  'Br' : "Bromuro"
} 

# class binaryCompound
class binaryCompound(Enum):
    Metal_Oxides = 1
    Anhydrides = 2
    Peroxides = 3
    Metal_Hydrides = 4
    Volatile_Hydrides = 5
    Hydracids = 6
    Neutral_Salts = 7
    Volatile_Salts = 8

compoundKindToPrefix = {
    "Metal_Oxides" : "Oxido",
    "Anhydrides" : "Anhidrido",
    "Peroxides" : "Peroxido",
    "Volatile_Hydrides" : "Hidruro",
    "Metal_Hydrides" : "Hidruro",
    "Hydracids" : "??",
    "Neutral_Salts" : "??",
    "Volatile_Hydrides" : "??",
}


# class syntax
class elementKind(Enum):
    NoMetal = 1
    Metal = 2
    SemiMetal = 3
    GasNoble = 4
    
def isInArray(target, array):
    for item in array:
        if target == item:
            return True
    return False

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

def valenciesToTraditional(element, charge):
    # (1, 3, -2)
    if charge < 0:
        print("tf is less than 0")
    # 1, 3
    without_negatives = []
    # x +- 1 ?
    index = 0

    for singleValency in element.valencies:
        if singleValency > 0:
             without_negatives.append(singleValency)

    for i in range(0, len(without_negatives)):
        if without_negatives[i] == charge:
            index = i
            break

    match len(without_negatives):
        case 1:
            return [prefixTradicional1i[index], prefixTradicional1f[index]]
        case 2:
            return [prefixTradicional2i[index], prefixTradicional2f[index]]
        case 3:
            return [prefixTradicional3i[index], prefixTradicional3f[index]]
        case 4:
            return [prefixTradicional4i[index], prefixTradicional4f[index]]
        case _:
            return ["!!!!!", "!!!!!"]
