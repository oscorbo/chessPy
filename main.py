
from table import periodicTable, atom, molecule

pT = periodicTable()

hidro = atom(pT.getSimb('H'), 0)
oxige = atom(pT.getSimb('O'), 0)

hidroMol = molecule([hidro])
hidroMol.printSystematic()