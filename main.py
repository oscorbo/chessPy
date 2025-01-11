
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
# 2
sulfu = atom(pT.getSimb('S'), 0)
# -1
cloro = atom(pT.getSimb('Cl'), 4)
# 1
brom = atom(pT.getSimb('Br'), 0)
# 1
cobal = atom(pT.getSimb('Co'), 0)
# 3
hier = atom(pT.getSimb('Fe'), 1)
# 2
tita = atom(pT.getSimb('Ti'), 0)
# 3
niqu = atom(pT.getSimb('Ni'), 1)
# 3 
boro = atom(pT.getSimb('B'), 0)
# 4
mang = atom(pT.getSimb('Mn'), 2)


hidroMol = molecule([oxige, mang, oxige])
#hidroMol.printThatShitASAP()
pT.valencyMixer(["Mn", "O"])

# acido sulfurico
# H2SO4