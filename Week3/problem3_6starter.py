# -problem3_6.py *- coding: utf-8 -*-

import sys

infilename = sys.argv[1]
outfilename = sys.argv[2]

ifile = open(infilename)
ofile = open(outfilename,'w')

for line in ifile:
    ofile.write(str(len(line.strip('\n')))+'\n')
    
ifile.close()
ofile.close()