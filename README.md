# US
Umbrella sampling pipeline (in development)

To do:
- [ ] automate inputs for slurm 
- [ ] move_protein.py script. Needs to be cleaned up and instructions need to be made


In this repository there are instructions and scripts to run steered-MD and impliment US on amino acids permiating membranes (bilayers and LD monolayers)

# Steps
(in development)
1) extract PDB structure. We are wanting only side-chain of amino acids, so find PDBs of only side-chain, or use CGenFF (CHARMM-GUI takes care of this)

2) Place above the membrane. This can be done for bilayer systems on CHARMM-GUI. For monolayers, we use our own MDAnalysis scripts that usually require some additional manual modification of topology files. Future work on scripts could be aimed to streamline this better.

3) Create custom gromacs index file that identifies the COM of PL and (and for LDs also identifies COM of LD-core). This is needed for steered and US. We use MDAnalysis script to create this index file (in repository)

4) Run steered-MD. MDP file is in this repository. Probably have to modify it depending on system. Goal is to push amino acid through bilayer, but I found it a bit tricky. There wasn't an easy way to push it through whole bilayer in one step, as GMX complains about PBC conditions and reference groups being too far apart and stuff like that. First I have to push it to the tails of the PLs then GMX simulation stopped. Than I took last frame of that simulation and had to push it to PL headgroup of bottom leaflet. 

5) Then concatenate both of those XTC files. After that, run 'GMX distance'. This finds distance between amino acid and reference.

6) Run settup_us.py script. This script automates the time-intensive stuff:
  - Reads distnace.xvg files z-coordinate
  - Runs 'GMX trjconv' to extract specific frames at time points in which amino acid is 0.1 apart in distance
  - Runs 'GMX grompp' to settup US files
  - This outputs 1.tpr, 2.tpr, 3.tpr, .... n.tpr for the US simulations

From here, we run it on CHPC or Expanse, or another HPC 


*** 
# PLUMED

