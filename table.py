from element import element as ele, atom
from utils import elementKind as eKind, prefix, contains, getIndexOf, valenciesToTraditional, binaryCompound, rootsElements
from utils import isInArray, Volatile_HydridesElements, HydracidsElements

class periodicTable:
	def __init__(self):
		eles = []
		eles.append(
			ele(simb = 'H', name = 'Hidrogeno', 
			nAtomic = 1, weigAtomic = 1.008, 
			valency = [1, -1], eKin = eKind.NoMetal, coords = [1,1], root = "hidr"))
		eles.append(
			ele(simb = 'He', name = 'Helio', 
			nAtomic = 2, weigAtomic = 4.003, 
			valency = [0], eKin = eKind.GasNoble, coords = [1,18], root = "heli"))
		eles.append(
			ele(simb = 'Li', name = 'Litio', 
			nAtomic = 3, weigAtomic = 6.941, 
			valency = [1], eKin = eKind.Metal, coords = [2,1], root = "lit"))
		eles.append(
			ele(simb = 'Be', name = 'Berilio', 
			nAtomic = 4, weigAtomic = 9.012, 
			valency = [2], eKin = eKind.Metal, coords = [2,2], root = "no encontre"))
		eles.append(
			ele(simb = 'B', name = 'Boro', 
			nAtomic = 5, weigAtomic = 10.811, 
			valency = [3, -3], eKin = eKind.SemiMetal, coords = [2, 13], root = "brom"))
		eles.append(
			ele(simb = 'C', name = 'Carbono', 
			nAtomic = 6, weigAtomic = 12.011, 
			valency = [2, 4, -4], eKin = eKind.NoMetal, coords = [2, 14], root = "carb"))
		eles.append(
			ele(simb = 'N', name = 'Nitrogeno', 
			nAtomic = 7, weigAtomic = 14.007, 
			valency = [1, 2, 3, 4, 5, -3], eKin = eKind.NoMetal, coords = [2, 15], root = "nitr"))
		eles.append(
			ele(simb = 'O', name = 'Oxigeno', 
			nAtomic = 8, weigAtomic = 15.999, 
			valency = [-2], eKin = eKind.NoMetal, coords = [2, 16], root = "oxi?"))
		eles.append(
			ele(simb = 'F', name = 'Fluor', 
			nAtomic = 9, weigAtomic = 18.998, 
			valency = [-1], eKin = eKind.NoMetal, coords = [2, 17], root = "fluor"))
		eles.append(
			ele(simb = 'S', name = 'Sulfuro', 
			nAtomic = 16, weigAtomic = 32.065, 
			valency = [2, 4, 6, -2], eKin = eKind.NoMetal, coords = [3, 16], root = "sulf"))
		eles.append(
			ele(simb = '(O2)', name = 'Peroxido', 
			nAtomic = -2, weigAtomic = 31.998, 
			valency = [-2], eKin = eKind.NoMetal, coords = [99,99], root = "2oxi?"))
		
		self.elements = eles
		
	def getSimb(self, simbToGet):
		for element in self.elements:
			if element.simb == simbToGet:
				return element
		return None
	


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
		print(" ------ ")

		self.atoms = []
		self.amount_atoms = []

		for i in range(0, len(self.atoms_no_sorted)):
			for j in range(0, len(self.atoms_no_sorted)):
				index = -1
				electronegativite = 0
				atom = self.atoms_no_sorted[j]
				if atom.element.electronegativity > electronegativite:
					index = j
					electronegativite = atom.element.electronegativity
			self.atoms.append(self.atoms_no_sorted[index])
			self.amount_atoms.append(self.amount_atoms_no_sorted[index])
			self.atoms_no_sorted.remove(atom)

	# LiF
	# array
	def getAtomsByEKinds(self, eKindsTargets:list):
		returnArray = []
		for atom in self.atoms:
			if eKindsTargets.__contains__(atom.element.elementKind):
				returnArray.append(atom)
		return returnArray

	def containsElement(self, simb):
		# repetidos y atomos
		for atom in self.atoms:
			if atom.element.simb == simb:
				return True
		return False
		
	def getElement(self, simbGet):
		for atom in self.atoms:
			if atom.element.simb == simbGet:
				return atom
		return None
	
	# this should return an array igs
	def getNotElement(self, simbNoGet):
		for atom in self.atoms:
			if not atom.element.simb == simbNoGet:
				return atom
		return None
	
	# getBinaryToBinaryCompound
	def passBinaryToBinaryCompound(self, compound):
		# [o, h2] 
		# like a ton of ifs fsure
		if self.containsElement('O'): return binaryCompound.Metal_Oxides
		if self.containsElement('(O2)'): return binaryCompound.Peroxides
		if self.containsElement('H') and self.getNotElement('H').getKind() is eKind.Metal: return binaryCompound.Metal_Hydrides
		if self.containsElement('H') and self.getNotElement('H').getKind() is eKind.NoMetal and isInArray(self.getNotElement('H').element.simb, Volatile_HydridesElements): return binaryCompound.Volatile_Hydrides
		if self.containsElement('H') and self.getNotElement('H').getKind() is eKind.NoMetal and isInArray(self.getNotElement('H').element.simb, HydracidsElements): return binaryCompound.Hydracids
		elementsNoM_M = self.getAtomsByEKinds([eKind.NoMetal, eKind.Metal])
		if len(elementsNoM_M) == len(self.atoms): return binaryCompound.Neutral_Salts

		
	def printThatShitASAP(self):
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
				# identify
				compoundBinaryKind = self.passBinaryToBinaryCompound(self.atoms)

				# contains oxygen
				if compoundBinaryKind == binaryCompound.Metal_Oxides:
					oxygen = self.getElement("O")
					noOxygen = self.getNotElement("O")
					# sistematica
					print(" | sistematica")
					tempString = ""
					for i in range(0, len(self.atoms)):
						atom = self.atoms[i]
						amount_atom = self.amount_atoms[i]
						tempString += prefix[amount_atom] + atom.element.name + " "
					print(tempString)

					# tradicional | na
					# print(f"Anhidrico {noOxygen.element.root}{valenciesToTraditional(noOxygen.element, noOxygen.charge)[1]}")

					# stock
					print(" | stock")
					print(f"{rootsElements[oxygen.element.simb]} de {noOxygen.element.name} ({str(noOxygen.charge)})") 

					# oxido metalico, anhidrico
					print(" | tipo de oxido")
					if noOxygen.element.elementKind == eKind.Metal:
						print("Oxido Metalico")
					if noOxygen.element.elementKind == eKind.NoMetal:
						print("Anhidrico")

					# formulacion
					print(" | formula")
					atoms_Reverted = self.atoms[::-1]
					amount_atoms_Reverted = self.amount_atoms[::-1]
					empty_String = ""
					for i in range(0, len(atoms_Reverted)):
						atom = atoms_Reverted[i]
						amount_atom = amount_atoms_Reverted[i]
						empty_String += atom.element.simb
						if not amount_atom == 1:
							empty_String += str(amount_atom)
					print(empty_String)
				
				elif compoundBinaryKind == binaryCompound.Peroxides:
					
					peroxide = self.getElement("(O2)")
					noPeroxide = self.getNotElement("(O2)")
					# print(peroxide.element.electronegativity)
					# print(noPeroxide.element.electronegativity)

					# improve
					if not noPeroxide.element.elementKind == eKind.Metal:
						print("error no peroxide found!!")
						return

					# sistematica
					print(" | sistematica")
					tempString = ""
					for i in range(0, len(self.atoms)):
						atom = self.atoms[i]
						amount_atom = self.amount_atoms[i]
						tempString += prefix[amount_atom] + atom.element.name + " "
					print(tempString)

					# tradicional | na
					# print(f"Anhidrico {noOxygen.element.root}{valenciesToTraditional(noOxygen.element, noOxygen.charge)[1]}")

					# stock
					print(" | stock")
					print(f"{rootsElements[peroxide.element.simb]} de {noPeroxide.element.name} ({str(noPeroxide.charge)})") 

					# formulacion
					print(" | formula")
					atoms_Reverted = self.atoms
					amount_atoms_Reverted = self.amount_atoms
					empty_String = ""
					for i in range(0, len(atoms_Reverted)):
						atom = atoms_Reverted[i]
						amount_atom = amount_atoms_Reverted[i]
						empty_String += atom.element.simb
						if not amount_atom == 1:
							empty_String += str(amount_atom)
					print(empty_String)
					
				elif compoundBinaryKind == binaryCompound.Metal_Hydrides:
					hydro = self.getElement("H")
					noHydro = self.getNotElement("H")
					# print(peroxide.element.electronegativity)
					# print(noPeroxide.element.electronegativity)

					# sistematica
					print(" | sistematica")
					tempString = ""
					for i in range(0, len(self.atoms)):
						atom = self.atoms[i]
						amount_atom = self.amount_atoms[i]
						tempString += prefix[amount_atom] + atom.element.name + " "
					print(tempString)

					# tradicional | na
					# print(f"Anhidrico {noOxygen.element.root}{valenciesToTraditional(noOxygen.element, noOxygen.charge)[1]}")

					# stock
					print(" | stock")
					print(f"{rootsElements[hydro.element.simb]} de {noHydro.element.name} ({str(noHydro.charge)})") 

					# formulacion
					print(" | formula")
					# why did that??
					# atoms_Reverted = self.atoms[::-1]
					atoms_Reverted = self.atoms
					# amount_atoms_Reverted = self.amount_atoms[::-1]
					amount_atoms_Reverted = self.amount_atoms
					empty_String = ""
					for i in range(0, len(atoms_Reverted)):
						atom = atoms_Reverted[i]
						amount_atom = amount_atoms_Reverted[i]
						empty_String += atom.element.simb
						if not amount_atom == 1:
							empty_String += str(amount_atom)
					print(empty_String)
				
				elif compoundBinaryKind == binaryCompound.Volatile_Hydrides:
					hydro = self.getElement("H")
					noHydro = self.getNotElement("H")

					# tradicional | na
					# print(f"Anhidrico {noOxygen.element.root}{valenciesToTraditional(noOxygen.element, noOxygen.charge)[1]}")

					# formulacion
					print(" | formula")
					# why did that??
					empty_String = ""
					for i in range(0, len(self.atoms)):
						atom = self.atoms[i]
						amount_atom = self.amount_atoms[i]
						empty_String += atom.element.simb
						if not amount_atom == 1:
							empty_String += str(amount_atom)
					print(empty_String)

					# sistematica
					print(" | sistematica")
					self.atoms = self.atoms[::-1]
					self.amount_atoms = self.amount_atoms[::-1]
					tempString = ""
					for i in range(0, len(self.atoms)):
						atom = self.atoms[i]
						amount_atom = self.amount_atoms[i]
						try:
							tempString += prefix[amount_atom] + rootsElements[atom.element.simb] + " "
						except:
							tempString += prefix[amount_atom] + atom.element.name + " "
						
					print(tempString)

				elif compoundBinaryKind == binaryCompound.Hydracids:
					hydro = self.getElement("H")
					noHydro = self.getNotElement("H")

					# tradicional | na
					# print(f"Anhidrico {noOxygen.element.root}{valenciesToTraditional(noOxygen.element, noOxygen.charge)[1]}")

					# formulacion
					# sistematica
					print(" | sistematica")
					print(noHydro.element.root + "uro de " + hydro.element.name)

					print(" | formula")
					self.atoms = self.atoms[::-1]
					self.amount_atoms = self.amount_atoms[::-1]
					empty_String = ""
					for i in range(0, len(self.atoms)):
						atom = self.atoms[i]
						amount_atom = self.amount_atoms[i]
						empty_String += atom.element.simb
						if not amount_atom == 1:
							empty_String += str(amount_atom)
					print(empty_String)

				elif compoundBinaryKind == binaryCompound.Neutral_Salts:
					elementsNoM_M = self.getAtomsByEKinds([eKind.NoMetal, eKind.Metal])
					atom1 = elementsNoM_M[0]
					atom2 = elementsNoM_M[1]

					# tradicional | na
					# print(f"Anhidrico {noOxygen.element.root}{valenciesToTraditional(noOxygen.element, noOxygen.charge)[1]}")

					# formulacion
					# sistematica
					print(" | sistematica")
					print(atom1.element.root + "uro de " + atom2.element.name)

					print(" | formula")
					self.atoms = self.atoms[::-1]
					self.amount_atoms = self.amount_atoms[::-1]
					empty_String = ""
					for i in range(0, len(self.atoms)):
						atom = self.atoms[i]
						amount_atom = self.amount_atoms[i]
						empty_String += atom.element.simb
						if not amount_atom == 1:
							empty_String += str(amount_atom)
					print(empty_String)

				print(" Kind Compound:")
				print(" | " + str(compoundBinaryKind))
			case _:
				print('wtf')
				print(len(self.atoms))