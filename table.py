
from element import element as ele
from utils import elementKind as eKind

class periodicTable:
	def __init__(self):
		eles = []
		eles.append(
			ele(simb = 'H', name = 'Hidrogeno', 
			nAtomic = 1, weigAtomic = 1.008, 
			valency = [1, -1], eKin = eKind.NoMetal, coords = [1,1]))
		eles.append(
			ele(simb = 'He', name = 'Helio', 
			nAtomic = 2, weigAtomic = 4.003, 
			valency = [0], eKin = eKind.GasNoble, coords = [1,18]))
		eles.append(
			ele(simb = 'Li', name = 'Litio', 
			nAtomic = 3, weigAtomic = 6.941, 
			valency = [1], eKin = eKind.Metal, coords = [2,1]))
		eles.append(
			ele(simb = 'Be', name = 'Berilio', 
			nAtomic = 4, weigAtomic = 9.012, 
			valency = [2], eKin = eKind.Metal, coords = [2,2]))
		eles.append(
			ele(simb = 'B', name = 'Boro', 
			nAtomic = 5, weigAtomic = 10.811, 
			valency = [3, -3], eKin = eKind.SemiMetal, coords = [2, 13]))
		eles.append(
			ele(simb = 'C', name = 'Carbono', 
			nAtomic = 6, weigAtomic = 12.011, 
			valency = [2, 4, -4], eKin = eKind.NoMetal, coords = [2, 14]))
		eles.append(
			ele(simb = 'N', name = 'Nitrogeno', 
			nAtomic = 7, weigAtomic = 14.007, 
			valency = [1, 2, 3, 4, 5, -3], eKin = eKind.NoMetal, coords = [2, 15]))
		eles.append(
			ele(simb = 'O', name = 'Oxigeno', 
			nAtomic = 8, weigAtomic = 15.999, 
			valency = [-2], eKin = eKind.NoMetal, coords = [2, 16]))
		
		self.elements = eles
		
	def getSimb(self, simbToGet):
		for element in self.elements:
			if element.simb == simbToGet:
				return element
		return None
	
class atom:
	def __init__(self, element, valency):
		self.element = element
		self.charge = 0
		self.setCharge(valency)
		
	def setCharge(self, valencyToSet):
		for valency in self.element.valencies:
			if valencyToSet == valency:
				self.charge = valency
				return
		print('Error: No found Valency!!')
		
class molecule:
	def __init__(self, atoms):
		self.atoms = atoms
		
	def hasOxigen(self):
		for atom in self.atoms:
			if atom.element.simb == 'O':
				return True
		return False
		
	def getNot(self, simbNoGet):
		for atom in self.atoms:
			if not atom.element.simb == simbNoGet:
				return atom
		return None
		
	def printSystematic(self):
		match len(self.atoms):
			case 1:
				print('Monoatomico')
				onlyAtom = self.atoms[0]
				if onlyAtom.charge > 0:
					# positive
					print('Ion '+ onlyAtom.element.name + str(onlyAtom.charge))
					
				if onlyAtom.charge < 0:
					# negative
					print('Ion '+ onlyAtom.element.name + 'uro')
			case 2:
				print('Binario')
				if self.hasOxigen:
					print('Oxido de ' + self.getNot('O').element.name)
					pass 
			case _:
				print('wtf')