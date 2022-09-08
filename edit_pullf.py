import argparse
import re
import os
import subprocess
import sys

filepath = 'pullf.dat'
f = open(filepath,'r')
lines = f.readlines()
f.close()


with open(filepath, "w") as fp:

    for line in lines:
        index = line.find('_')
        output_line = line[:index]+'.part0002'+ line[index:]
        print(output_line,file=fp)

output=""
with open("pullf.dat") as f:
    for line in f:
        if not line.isspace():
            output+=line
            
f= open("pull2.dat",'w')
f.write(output)