
from math import sqrt

# ELEMENT CLASS
class element:
	def __init__(self, simb, name, nAtomic, weigAtomic, valency, eKin, coords, root, electronegatividad):
		self.simb = simb
		self.name = name
		self.nAtomic = nAtomic
		self.weigth = weigAtomic
		self.valencies = valency
		self.elementKind = eKin
		self.period = coords[0]
		self.group = coords[1]
		self.root = root
		self.electronegativity = electronegatividad
		#distance = (self.period - 2) + (self.group - 17)
		#if distance > 0:
		#	self.electronegativity = sqrt(distance)
		#else:
		#	self.electronegativity = sqrt(-1 * distance)

# ATOM

class atom:
    def __init__(self, element, valency):
        self.element = element
        self.charge = 0
		# should change to valency or n° oxi
        self.setCharge(valency)
		
    def setCharge(self, valencyToSet):
        try: 
            self.charge = self.element.valencies[valencyToSet]
        except:
            print('Error: No found Valency!!')
            self.charge = 0
			
    def getKind(self):
        return self.element.elementKind
	
    def isGroup17(self): return self.element.group == 17