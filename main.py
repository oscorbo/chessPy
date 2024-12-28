
from table import periodicTable, atom, molecule

pT = periodicTable()

# fix numeros de oxidacion
# 1
hidro = atom(pT.getSimb('H'), 0)
# 1
sodio = atom(pT.getSimb('Na'), 0)
# -2
oxige = atom(pT.getSimb('O'), 0)
# -2
peroxi = atom(pT.getSimb('(O2)'), 0)
# 4
carb = atom(pT.getSimb('C'), 1)
# -1
fluo = atom(pT.getSimb('F'), 0)
# 1
liti = atom(pT.getSimb('Li'), 0)
# -3
nitro = atom(pT.getSimb('N'), 5)
# -2
sulfu = atom(pT.getSimb('S'), 3)
# -1
cloro = atom(pT.getSimb('Cl'), 4)
# 1
brom = atom(pT.getSimb('Br'), 0)
# 1
cobal = atom(pT.getSimb('Co'), 0)
# 2
hier = atom(pT.getSimb('Fe'), 0)
# 2
tita = atom(pT.getSimb('Ti'), 0)

hidroMol = molecule([hidro, cloro])
# solamente la sistematica, por ahora
hidroMol.printThatShitASAP()

# acido sulfurico
# H2SO4