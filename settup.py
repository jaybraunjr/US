import argparse
import re
import os
import subprocess
import numpy as np
import matplotlib.pyplot as plt

def read_dist(dist_file):
    
    
    f = open(dist_file,'r')
    lines = f.readlines()[17:]
    f.close()

    
    ### now we need to start at line 17 and read down
    out_dict = {}

    for i in range(len(lines)):
    
    # Split on white-space; grab frame/distance
        columns = lines[i].split()
        num=float(columns[0])
        dist=float(columns[3])
        out_dict[num] = dist
    keys = out_dict.keys()
    sorted(keys)
    
    ### some numbers turn negative for some reason, making them positive.
    ### system dependant!!!
    ### Will comment out for now, don't think it makes a difference actually...
    
#     for key, value in out_dict.items():
#         out_dict[key] = abs(value)
    out = [(k,out_dict[k]) for k in keys]
    return out

test=read_dist('dist.xvg')

def get_dist(dist_list, inp_num):
    
    distances = [d[1] for d in dist_list]
    current=0
    sampled=[current]
    while current < len(distances):
#         print(current,'current')
        targ = distances[current] + inp_num
#         print(targ,'targ')
        on = [abs(targ-d) for d in distances[current:]]
        next_ = on.index(min(on)) + current
        if current == next_:
            break
        else:
            sampled.append(next_)
            current = next_
    return sampled

test2=get_dist(test,0.1)


def trjconv(grofile,xtcfile,newgrofile,begin,end):
    myexec = 'gmx'
    args = [myexec,'trjconv',
           '-f', xtcfile,
           '-s', grofile,
           '-o', newgrofile,
           '-b', begin,
           '-dump', end]
    p = subprocess.Popen(args, 
                             stdin=subprocess.PIPE,
                             )
    p.stdin.write(b'0\n')
    p.communicate()[0]
    p.stdin.close()
    p.wait()
    
ls=[]
def stuff():
    for num in range(len(test2)):
#         ls.append(num)
        return num

stuff()

old=0
for num in test2:
    old=old+1
    trjconv('pull2.gro','pull2.xtc', str(old)+'.gro',str(num),str(num))

def grompp(mdpfile,grofile,topfile,tprfile,ndxfile):
    myexec = 'gmx'
    args = [myexec,'grompp',
           '-f', mdpfile,
           '-c', grofile,
           '-p', topfile,
           '-o', tprfile,
           '-n', ndxfile,
            ]
    p = subprocess.Popen(args, 
                             stdin=subprocess.PIPE,
                             )
    p.stdin.write(b'0\n')
    p.communicate()[0]
    p.stdin.close()
    p.wait()
    
old_=0
for num in test2:
    old_=old_+1
    grompp('pull.mdp', str(old_)+'.gro','topol.top','inp'+str(old_)+'.tpr','leaflet.ndx')