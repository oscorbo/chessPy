from element import element as ele, atom
from utils import elementKind as eKind, prefix, contains, getIndexOf, valenciesToTraditional, binaryCompound, rootsElements, compoundKindToPrefix
from utils import isInArray, Volatile_HydridesElements, HydracidsElements

class periodicTable:
	def __init__(self):
		eles = []
		eles.append(
			ele(simb = 'H', name = 'Hidrogeno', 
			nAtomic = 1, weigAtomic = 1.008, 
			valency = [1, -1], eKin = eKind.NoMetal, coords = [1,1], root = "hidr", electronegatividad = 2.1))
		eles.append(
			ele(simb = 'He', name = 'Helio', 
			nAtomic = 2, weigAtomic = 4.003, 
			valency = [0], eKin = eKind.GasNoble, coords = [1,18], root = "heli",  electronegatividad = 0))
		eles.append(
			ele(simb = 'Li', name = 'Litio', 
			nAtomic = 3, weigAtomic = 6.941, 
			valency = [1], eKin = eKind.Metal, coords = [2,1], root = "lit", electronegatividad = 1.0))
		eles.append(
			ele(simb = 'Be', name = 'Berilio', 
			nAtomic = 4, weigAtomic = 9.012, 
			valency = [2], eKin = eKind.Metal, coords = [2,2], root = "no encontre", electronegatividad = 1.6))
		eles.append(
			ele(simb = 'B', name = 'Boro', 
			nAtomic = 5, weigAtomic = 10.811, 
			valency = [3, -3], eKin = eKind.NoMetal, coords = [2, 13], root = "bor", electronegatividad = 2.0))
		eles.append(
			ele(simb = 'C', name = 'Carbono', 
			nAtomic = 6, weigAtomic = 12.011, 
			valency = [2, 4, -4], eKin = eKind.NoMetal, coords = [2, 14], root = "carb", electronegatividad = 2.5))
		eles.append(
			ele(simb = 'N', name = 'Nitrogeno', 
			nAtomic = 7, weigAtomic = 14.007, 
			valency = [1, 2, 3, 4, 5, -3], eKin = eKind.NoMetal, coords = [2, 15], root = "nitr",  electronegatividad = 3.0))
		eles.append(
			ele(simb = 'O', name = 'Oxigeno', 
			nAtomic = 8, weigAtomic = 15.999, 
			valency = [-2], eKin = eKind.NoMetal, coords = [2, 16], root = "oxi?",  electronegatividad = 3.5))
		eles.append(
			ele(simb = 'F', name = 'Fluor', 
			nAtomic = 9, weigAtomic = 18.998, 
			valency = [-1], eKin = eKind.NoMetal, coords = [2, 17], root = "fluor",  electronegatividad = 4.0))
		eles.append(
			ele(simb = 'Ne', name = 'Neon', 
			nAtomic = 10, weigAtomic = 20.180, 
			valency = [0], eKin = eKind.GasNoble, coords = [2, 18], root = "neon",  electronegatividad = 0))
		eles.append(
			ele(simb = 'Na', name = 'Sodio', 
			nAtomic = 11, weigAtomic = 22.990, 
			valency = [1], eKin = eKind.Metal, coords = [3, 1], root = "sodi?",  electronegatividad = 0.9))
		eles.append(
			ele(simb = 'Mg', name = 'Magnesio', 
			nAtomic = 12, weigAtomic = 24.305, 
			valency = [2], eKin = eKind.Metal, coords = [3, 2], root = "mag?",  electronegatividad = 1.2))
		eles.append(
			ele(simb = 'Al', name = 'Aluminio', 
			nAtomic = 13, weigAtomic = 26.981, 
			valency = [3], eKin = eKind.Metal, coords = [3, 13], root = "alum?",  electronegatividad = 1.5))
		eles.append(
			ele(simb = 'Si', name = 'Silicio', 
			nAtomic = 14, weigAtomic = 28.086, 
			valency = [4], eKin = eKind.NoMetal, coords = [3, 14], root = "silici",  electronegatividad = 1.8))
		eles.append(
			ele(simb = 'P', name = 'Fosforo', 
			nAtomic = 15, weigAtomic = 30.974, 
			valency = [3, 5, -3], eKin = eKind.NoMetal, coords = [3, 15], root = "fosfo",  electronegatividad = 2.1))
		eles.append(
			ele(simb = 'S', name = 'Azufre', 
			nAtomic = 16, weigAtomic = 32.066, 
			valency = [2, 4, 6, -2], eKin = eKind.NoMetal, coords = [3, 16], root = "sulf",  electronegatividad = 2.5))
		eles.append(
			ele(simb = 'Cl', name = 'Cloro', 
	   		nAtomic = 17, weigAtomic = 35.453, 
			valency = [1, 3, 5, 7, -1], eKin = eKind.NoMetal, coords = [3, 17], root = "clor",  electronegatividad = 3.0))
		eles.append(
			ele(simb = 'Ar', name = 'Argon', 
	   		nAtomic = 18, weigAtomic = 39.948, 
			valency = [0], eKin = eKind.GasNoble, coords = [3, 18], root = "argon?",  electronegatividad = 0))
		eles.append(
			ele(simb = 'K', name = 'Potasio', 
	   		nAtomic = 19, weigAtomic = 39.098, 
			valency = [1], eKin = eKind.Metal, coords = [4, 1], root = "potas?",  electronegatividad = 0.8))
		eles.append(
			ele(simb = 'Ca', name = 'Calcio', 
	   		nAtomic = 20, weigAtomic = 40.078, 
			valency = [2], eKin = eKind.Metal, coords = [4, 2], root = "calci?",  electronegatividad = 1.0))
		eles.append(
			ele(simb = 'Sc', name = 'Escandio', 
	   		nAtomic = 21, weigAtomic = 44.956, 
			valency = [3], eKin = eKind.Metal, coords = [4, 3], root = "escand?",  electronegatividad = 1.3))
		eles.append(
			ele(simb = 'Ti', name = 'Titanio', 
	   		nAtomic = 22, weigAtomic = 47.867, 
			valency = [2, 3, 4], eKin = eKind.Metal, coords = [4, 4], root = "Titan",  electronegatividad = 1.5))
		eles.append(
			ele(simb = 'V', name = 'Vanadio', 
	   		nAtomic = 23, weigAtomic = 50.941, 
			valency = [2, 3, 4, 5], eKin = eKind.Metal, coords = [4, 5], root = "vanadi",  electronegatividad =1.6))
		eles.append(
			ele(simb = 'Cr', name = 'Cromo', 
	   		nAtomic = 24, weigAtomic = 51.996, 
			valency = [2, 3, 4, 5, 6], eKin = eKind.Metal, coords = [4, 6], root = "crom",  electronegatividad =1.6))
		eles.append(
			ele(simb = 'Mn', name = 'Manganesio', 
	   		nAtomic = 25, weigAtomic = 54.938, 
			valency = [2, 3, 4, 5, 6, 7], eKin = eKind.Metal, coords = [4, 7], root = "mangan",  electronegatividad =1.5))
		eles.append(
			ele(simb = 'Fe', name = 'Hierro', 
	   		nAtomic = 26, weigAtomic = 55.845, 
			valency = [2, 3], eKin = eKind.Metal, coords = [4, 8], root = "ferr",  electronegatividad =1.8))
		eles.append(
			ele(simb = 'Co', name = 'Cobalto', 
	   		nAtomic = 27, weigAtomic = 58.933, 
			valency = [2, 3], eKin = eKind.Metal, coords = [4, 9], root = "cobalt",  electronegatividad =1.9))
		eles.append(
			ele(simb = 'Ni', name = 'Niquel', 
	   		nAtomic = 28, weigAtomic = 58.693, 
			valency = [2, 3], eKin = eKind.Metal, coords = [4, 10], root = "niquel",  electronegatividad =1.9))
		eles.append(
			ele(simb = 'Cu', name = 'Cobre', 
	   		nAtomic = 29, weigAtomic = 63.546, 
			valency = [1, 2], eKin = eKind.Metal, coords = [4, 11], root = "cupr",  electronegatividad = 1.9))
		eles.append(
			ele(simb = 'Zn', name = 'Zinc', 
	   		nAtomic = 30, weigAtomic = 65.39, 
			valency = [2], eKin = eKind.Metal, coords = [4, 12], root = "zinc",  electronegatividad = 1.6))
		eles.append(
			ele(simb = 'Ga', name = 'Galio', 
	   		nAtomic = 31, weigAtomic = 69.723, 
			valency = [3], eKin = eKind.Metal, coords = [4, 13], root = "gal",  electronegatividad = 1.6))
		eles.append(
			ele(simb = 'Ge', name = 'Germanio', 
	   		nAtomic = 32, weigAtomic = 72.61, 
			valency = [4], eKin = eKind.Metal, coords = [4, 14], root = "germ",  electronegatividad = 1.8))
		eles.append(
			ele(simb = 'As', name = 'Arsenico', 
	   		nAtomic = 33, weigAtomic = 74.921, 
			valency = [3, 5, -3], eKin = eKind.Metal, coords = [4, 15], root = "arsen?",  electronegatividad = 2.0))
		eles.append(
			ele(simb = 'Se', name = 'Selenio', 
	   		nAtomic = 34, weigAtomic = 78.960, 
			valency = [2, 4, 6, -2], eKin = eKind.NoMetal, coords = [4, 16], root = "Selen?",  electronegatividad =2.4))
		eles.append(
			ele(simb = 'Br', name = 'Bromo', 
	   		nAtomic = 35, weigAtomic = 79.904, 
			valency = [1, 3, 5, 7, -1], eKin = eKind.NoMetal, coords = [4, 17], root = "brom",  electronegatividad =2.8))

		eles.append(
			ele(simb = '(O2)', name = 'Peroxido', 
			nAtomic = -2, weigAtomic = 31.998, 
			valency = [-2], eKin = eKind.NoMetal, coords = [99,99], root = "2oxi?",  electronegatividad = 99.0))
		
		self.elements = eles
		
	def getSimb(self, simbToGet):
		for element in self.elements:
			if element.simb == simbToGet:
				return element
		return None
	
	def valencyMixer(self, simbs):
		for index in range(len(simbs)):
			current_atom = self.getSimb(simbs[index])
			next_atom = self.getSimb(simbs[index - 1])
			for negativeValency in current_atom.getNegativeValencies():
				for positiveValency in next_atom.getPositiveValencies():
					# xddddd perreo poliglota
					if negativeValency * - 1 == positiveValency:
						print(f"{current_atom.simb} {next_atom.simb}")
					else:
						print(f"{current_atom.simb}{positiveValency} {next_atom.simb}{negativeValency * -1}")


class molecule:

	def __init__(self, atomsToAssign):
		self.atoms_no_sorted = []
		self.amount_atoms_no_sorted = []
		
		# agrupados
		for atom in atomsToAssign:
			if not contains(self.atoms_no_sorted, atom):
				self.atoms_no_sorted.append(atom)
				self.amount_atoms_no_sorted.append(1)
			else:
				self.amount_atoms_no_sorted[getIndexOf(self.atoms_no_sorted, atom)] += 1
		print(" ------ ")

		self.atoms = []
		self.amount_atoms = []

		for i in range(len(self.atoms_no_sorted)):
			for j in range(0, len(self.atoms_no_sorted) - i - 1):
				if self.atoms_no_sorted[j].element.electronegativity > self.atoms_no_sorted[j + 1].element.electronegativity:
					# .element.electronegativity
					# .charge
					self.atoms_no_sorted[j], self.atoms_no_sorted[j + 1] = self.atoms_no_sorted[j + 1], self.atoms_no_sorted[j]
					self.amount_atoms_no_sorted[j], self.amount_atoms_no_sorted[j + 1] = self.amount_atoms_no_sorted[j + 1], self.amount_atoms_no_sorted[j]

		self.atoms = self.atoms_no_sorted
		self.amount_atoms = self.amount_atoms_no_sorted

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
	
	def getElementIndex(self, simbGet):
		for i in range(len(self.atoms)):
			if self.atoms[i].element.simb == simbGet:
				return i
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
		if self.containsElement('O') and self.getNotElement('O').getKind() is eKind.Metal: return binaryCompound.Metal_Oxides
		if self.containsElement('O') and self.getNotElement('O').getKind() is eKind.NoMetal: return binaryCompound.Anhydrides
		if self.containsElement('(O2)'): return binaryCompound.Peroxides
		if self.containsElement('H') and self.getNotElement('H').getKind() is eKind.NoMetal and isInArray(self.getNotElement('H').element.simb, Volatile_HydridesElements): return binaryCompound.Volatile_Hydrides
		if self.containsElement('H') and self.getNotElement('H').getKind() is eKind.NoMetal and isInArray(self.getNotElement('H').element.simb, HydracidsElements): return binaryCompound.Hydracids
		if self.containsElement('H') and self.getNotElement('H').getKind() is eKind.Metal: return binaryCompound.Metal_Hydrides

		elementsM = self.getAtomsByEKinds([eKind.NoMetal, eKind.NoMetal])
		if len(elementsM) == len(self.atoms): return binaryCompound.Volatile_Salts
		
		elementsNoM_M = self.getAtomsByEKinds([eKind.NoMetal, eKind.Metal])
		if len(elementsNoM_M) == len(self.atoms): return binaryCompound.Neutral_Salts
		

	def printSistematic(self):
		print(" | sistematica")
		tempString = ""
		for i in range(len(self.atoms)):
			# check if has other name??
			# oxigeno -> oxido
			atom = self.atoms[i]
			amount_atom = self.amount_atoms[i]
			# primero??
			if not i == len(self.atoms) - 1:
				try:
					tempString += prefix[amount_atom] + rootsElements[atom.element.simb] + " de "
				except:
					tempString += prefix[amount_atom] + atom.element.name + " de "
			else:
				if not amount_atom == 1:
					tempString += prefix[amount_atom] + atom.element.name
				else:
					tempString += atom.element.name
		print(tempString)
		
	def printSistematicInverted(self):
		print(" | sistematica")
		tempString = ""
		atoms = self.atoms[::-1]
		amount_atoms = self.amount_atoms[::-1]
		for i in range(len(atoms)):
			# check if has other name??
			# oxigeno -> oxido
			atom = atoms[i]
			amount_atom = amount_atoms[i]
			if not i == len(atoms) - 1:
				# ??
				try:
					tempString += prefix[amount_atom] + rootsElements[atom.element.simb] + " de "
				except:
					tempString += prefix[amount_atom] + atom.element.root + "uro de "
			else:
				if not amount_atom == 1:
					tempString += prefix[amount_atom] + atom.element.name
				else:
					tempString += atom.element.name
		print(tempString)

	def getTradicionalFromAtom(self, atom):
		return f"{valenciesToTraditional(atom.element, atom.charge)[0]}{atom.element.root}{valenciesToTraditional(atom.element, atom.charge)[1]}"

	def printStock(self, element1, element2):
		print(" | stock")
		if len(element2.element.getPositiveValencies()) != 1:
			print(f"{rootsElements[element1.element.simb]} de {element2.element.name} ({str(element2.charge)})") 
		else:
			print(f"{rootsElements[element1.element.simb]} de {element2.element.name} ") 

	def printTradicional(self, compoundKind, nonMain):
		print(" | tradicional")
		tempCOmpoundKind = str(compoundKind).split(".")[1]
		print(f"{compoundKindToPrefix[str(tempCOmpoundKind)]} {self.getTradicionalFromAtom(nonMain)}")

	def printFormula(self):
		print(" | formula")
		#atoms_Reverted = self.atoms[::-1]
		atoms_Reverted = self.atoms
		#amount_atoms_Reverted = self.amount_atoms[::-1]
		amount_atoms_Reverted = self.amount_atoms
		empty_String = ""
		for i in range(0, len(atoms_Reverted)):
			atom = atoms_Reverted[i]
			amount_atom = amount_atoms_Reverted[i]
			empty_String += atom.element.simb
			if not amount_atom == 1:
				empty_String += str(amount_atom)
		print(empty_String)

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

					self.printSistematicInverted()
					self.printStock(oxygen, noOxygen)
					self.printTradicional(compoundBinaryKind, noOxygen)
					self.printFormula()

				elif compoundBinaryKind == binaryCompound.Anhydrides:
					oxygen = self.getElement("O")
					noOxygen = self.getNotElement("O")

					self.printSistematic()
					self.printStock(oxygen, noOxygen)
					self.printTradicional(compoundBinaryKind, noOxygen)
					self.printFormula()

				elif compoundBinaryKind == binaryCompound.Peroxides:
					peroxide = self.getElement("(O2)")
					noPeroxide = self.getNotElement("(O2)")

					# improve
					if not noPeroxide.element.elementKind == eKind.Metal:
						print("error no peroxide found!!")
						return

					# tradicional | na
					# print(f"Anhidrico {noOxygen.element.root}{valenciesToTraditional(noOxygen.element, noOxygen.charge)[1]}")

					self.printSistematic()
					self.printStock(peroxide, noPeroxide)
					self.printTradicional(compoundBinaryKind, noPeroxide)
					self.printFormula()
					
				elif compoundBinaryKind == binaryCompound.Metal_Hydrides:
					hydro = self.getElement("H")
					noHydro = self.getNotElement("H")
					# print(peroxide.element.electronegativity)
					# print(noPeroxide.element.electronegativity)

					# sistematica
					self.printSistematic()
					self.printTradicional(compoundBinaryKind, noHydro)
					self.printStock(hydro, noHydro)
					self.printFormula()
				
				elif compoundBinaryKind == binaryCompound.Volatile_Hydrides:
					hydro = self.getElement("H")
					noHydro = self.getNotElement("H")

					print("Compuestos: Hidruros Volatiles no tienen nomenclatura tradicional")

					self.printSistematic()
					self.printTradicional(compoundBinaryKind, noHydro)
					self.printFormula()

				elif compoundBinaryKind == binaryCompound.Hydracids:
					hydro = self.getElement("H")
					noHydro = self.getNotElement("H")
					amountHydros = self.amount_atoms[self.getElementIndex("H")]
					if amountHydros == 1:
						amountHydros = ""
					else:
						amountHydros = str(amountHydros)
					
					print("Compuestos: Hidracidos no tienen nomenclatura tradicional")

					# sistematica
					print(" | sistematica")
					print(noHydro.element.root + "uro de " + hydro.element.name)
					print(" | tradicional")
					print(f"Acido {noHydro.element.root}{hydro.element.root}ico")
					print(" | Formula")
					print(f"{hydro.element.simb}{amountHydros}{noHydro.element.simb}")

				elif compoundBinaryKind == binaryCompound.Neutral_Salts:
					elementsNoM_M = self.getAtomsByEKinds([eKind.Metal, eKind.NoMetal])
					atom1 = elementsNoM_M[1]
					atom2 = elementsNoM_M[0]
					
					print(" | stock")
					if len(atom2.element.getPositiveValencies()) != 1:
						print(f"{atom1.element.root}uro de {atom2.element.name} ({atom2.charge})")
					else:
						print(f"{atom1.element.root}uro de {atom2.element.name} ")
					self.printSistematicInverted()
					print(" | tradicional")
					print(f"{atom1.element.root}uro {self.getTradicionalFromAtom(atom2)}")
					self.printFormula()

				elif compoundBinaryKind == binaryCompound.Volatile_Salts:
					elementsNoM = self.getAtomsByEKinds([eKind.NoMetal])
					atom1 = elementsNoM[1]
					atom2 = elementsNoM[0]
					
					# tradicional | na
					# print(f"Anhidrico {noOxygen.element.root}{valenciesToTraditional(noOxygen.element, noOxygen.charge)[1]}")
					
					print(" | tradicional")
					print(f"{atom1.element.root}uro {self.getTradicionalFromAtom(atom2)}")
					print(" | stock")
					if len(atom2.element.getPositiveValencies()) != 1:
						print(f"{atom1.element.root}uro de {atom2.element.name} ({atom2.charge})")
					else:
						print(f"{atom1.element.root}uro de {atom2.element.name} ")
					self.printSistematicInverted()
					self.printFormula()

				print(" Kind Compound:")
				print(" | " + str(compoundBinaryKind))
			case _:
				print('wtf')
				print(len(self.atoms))