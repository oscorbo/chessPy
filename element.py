
from math import sqrt

class element:
	def __init__(self, simb, name, nAtomic, weigAtomic, valency, eKin, coords):
		self.simb = simb
		self.name = name
		self.nAtomic = nAtomic
		self.weigth = weigAtomic
		self.valencies = valency
		self.elementKind = eKin
		self.period = coords[0]
		self.group = coords[1]
		# if is negative
		distance = (self.period - 2) + (self.group - 17)
		if distance > 0:
			self.electronegativity = sqrt(distance)
		else:
			self.electronegativity = sqrt(-1 * distance)