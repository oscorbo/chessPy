
from enum import Enum

prefix = ['x', 'mono', 'di', 'tri', 'tetra', 'penta', 'hexa']
prefixTradicional1i = [""]
prefixTradicional1f = ["ico"]

prefixTradicional2i = ["", ""]
prefixTradicional2f = ["oso", "ico"]

prefixTradicional3i = ["hipo", "", ""]
prefixTradicional3f = ["oso", "oso", "ico"]

prefixTradicional4i = ["hipo", "", "", "per"]
prefixTradicional4f = ["oso", "oso", "ico", "ico"]

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

def valenciesToTraditional(element, charge):
    # (1, 3, -2)
    if charge < 0:
        print("tf is less than 0")
        return 1
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
        print("WTF???????? Ion or somshi lk that :v")

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
