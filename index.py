import MDAnalysis as mda
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

u = mda.Universe('6.1.gro','pull.xtc')
prot = u.select_atoms('resname TOL')
system = u.select_atoms('resid 1-84820')
com = prot.center_of_mass()

halfz = u.dimensions[2]/2 ## Get the half of the z-dimension
UP = u.select_atoms('name P and prop z > %f' %halfz)
LP = u.select_atoms('name P and prop z < %f' %halfz)

with mda.selections.gromacs.SelectionWriter('leaflet.ndx', mode='w') as ndx:
	ndx.write(LP,name='lower_leaflet')
	ndx.write(UP,name='upper_leaflet')
	ndx.write(prot,name='prot')
	ndx.write(system,name='all')
