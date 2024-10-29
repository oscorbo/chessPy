
from table import periodicTable, atom, molecule

pT = periodicTable()

hidro = atom(pT.getSimb('H'), -1)
oxige = atom(pT.getSimb('O'), -2)

hidroMol = molecule([hidro, oxige])
hidroMol.printSystematic()