from element import element as ele
from utils import elementKind as eKind, prefix, contains, getIndexOf

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
		
class molecule:

	def __init__(self, atomsToAssign):
		self.atoms_no_sorted = []
		self.amount_atoms_no_sorted = []
		
		for atom in atomsToAssign:
			if not contains(self.atoms_no_sorted, atom):
				self.atoms_no_sorted.append(atom)
				self.amount_atoms_no_sorted.append(1)
			else:
				self.amount_atoms_no_sorted[getIndexOf(self.atoms_no_sorted, atom)] += 1

		self.atoms = []
		self.amount_atoms = []

		for i in range(0, len(self.atoms_no_sorted)):
			for j in range(0, len(self.atoms_no_sorted)):
				index = 0
				electronegativite = 0
				atom = self.atoms_no_sorted[j]
				if atom.element.electronegativity > electronegativite:
					index = j
					electronegativite = atom.element.electronegativity
			self.atoms.append(self.atoms_no_sorted[index])
			self.amount_atoms.append(self.amount_atoms_no_sorted[index])

			self.atoms_no_sorted.remove(atom)


	def containsElement(self, simb):
		# repetidos y atomos
		for atom in self.atoms:
			if atom.element.simb == simb:
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
					# prefijo
					# positive
					print('Ion '+ onlyAtom.element.name + str(onlyAtom.charge))
					
				if onlyAtom.charge < 0:
					# negative
					print('Ion '+ onlyAtom.element.name + 'uro')
			case 2:
				print('Binario')
				# Fe2, O3
				# Fe Fe, O O O
				if self.containsElement('O'):
					# electronegativo 
					# give elemente get amount
					# for each made that shi??
					for i in range(0, len(self.atoms)):
						atom = self.atoms[i]
						amount_atom = self.amount_atoms[i]
						print(prefix[amount_atom] + atom.element.name)
			case _:
				print('wtf')
				print(len(self.atoms))