# US
Umbrella sampling pipeline

# This uses MLX with a collective variable (CV) of the helix Z-COM with a distance calculation to the average position of the phosolipid headgroups

Withing these files, you will find:
- initial windows of MLX. There are 30, all around 0.1nm increments
- mdp file that initializes the run. This determines the force constants etc.
- scripts for analysis. WHAM etc


Sometimes there are scripts that can be set up to initialize the windows (distance etc.) however in some cases you have to go in manually to extract windows. For my case, I took an unbiased trajectory of MLX associating to a LD, and used 'gmx distance' to create a file of z-distances. From here Excel/Pandas can easily extract windows with labeled timesteps that are 0.1nm apart.

There are also scripts that are able to submit a bunch of slurm jobs as once. Since this is on CHPC, you are limited in the amount of jobs you submit (I think). You can go in manually and submit a few at a time.


If you want to do it from the start, you will have to:
1) run 'gmx distance -f full.xtc -s full.tpr -n leaflets.ndx -oav av.xvg -oxyz xyz.xvg -select 'com of group "prot" plus com of group "lower_leaflet"' -b 519000 -e 800000
2) Extract numbers from the 'z' column of the output that are 0.1 nm in increments and capture the cytosol-full bound states. This can be done with a script, which I am working on for the future. If you want to also create a python script that does this, feel free to add.
3) 
