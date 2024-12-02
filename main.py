
from table import periodicTable, atom, molecule

pT = periodicTable()

# fix numeros de oxidacion
# 1
hidro = atom(pT.getSimb('H'), 0)
# -2
oxige = atom(pT.getSimb('O'), 0)
# 4
carb = atom(pT.getSimb('C'), 1)

hidroMol = molecule([hidro, oxige, hidro])
# solamente la sistematica, por ahora
hidroMol.printThatShitASAP()