
from table import periodicTable, atom, molecule

pT = periodicTable()

# 1
hidro = atom(pT.getSimb('H'), 0)
# -2
oxige = atom(pT.getSimb('O'), 0)

hidroMol = molecule([hidro, oxige, hidro])
# solamente la sistematica, por ahora
hidroMol.printSystematic()