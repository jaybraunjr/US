### UNTESTED
import MDAnalysis as mda
from MDAnalysis import transformations
import numpy as np

### READ A MEMBRANE (LD or a bilayer membrane)
### BETTER TO BE A WHOLE STRUCTURE (NOT BROKEN)
u = mda.Universe('50.50_1us.gro')
halfz = u.dimensions[2] / 2

UP = u.select_atoms('name P and prop z < %f' %halfz)

UPz = UP.center_of_mass()[2]

### READ A PROTEIN-ONLY STRUCTURE
prot = mda.Universe('step5_input.gro').select_atoms('protein')
# prot2 = mda.Universe('step5_input.gro').select_atoms('protein')
prot.positions -= prot.center_of_mass()
prot.positions += np.array([u.dimensions[0]/2, UPz + 12])
# prot2.positions += np.array([u.dimensions[0]/3, u.dimensions[1]/2, UPz + 10])


### MERGE membrane and  protein
newu = mda.Merge(prot, u.atoms)
newu.dimensions = u.dimensions
print(newu)
prot_pos = prot.atoms.center_of_geometry()




ag = newu.select_atoms('(protein) or (resname POPC DOPE SAPI TRIO CHYO) or (resname TIP3 and not byres (resname TIP3 and name OH2 and around 2.8 protein)) or (resname SOD CLA and not byres (resname SOD CLA and around 2.8 protein))')

ag.write('final.gro')
