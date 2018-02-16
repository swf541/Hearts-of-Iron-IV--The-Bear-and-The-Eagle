import os
import sys
import asyncio
import shutil
from io import BytesIO
from functools import wraps
from textwrap import dedent
from random import choice, shuffle
from collections import defaultdict
ideologies = ["",""]
file = ["",""]
justname = ""
extension = ""
countrylines = [""]
list = ""
print('Chupachu\'s country loc maker, a tool for quickly setting up country localization\n\n')
list = input('Read from countries.txt? Y/N: ')
file=0
if list.lower()=="y" or list.lower() == "yes":
    file=1
else:
    file=0
if file==0:
    countrylines[0] = input('Enter your TAG|countryname|countryADJ: ')
filename = 'out.yml'
print('File: ', filename)

if os.path.isfile(filename):
    print("out.yml found.\n")
    if file==1:
        f = open("countries.txt","r")
        countrylines = f.read().split('\n')
        f.close()
        print(str(len(countrylines))+" country lines detected.")
    f = open("ideologies.txt", "r")
    ideologytxt=f.read()
    idelines = ideologytxt.split('\n')
    f.close()

    print(str(len(idelines))+" ideology lines detected.")
    txt=""
    for country in countrylines:
        csplit = country.split('|')
        if len(csplit) > 2:
            cname = csplit[0]
            cfullname = csplit[1]
            cadj = csplit[2]
            
            for line in idelines:
                
                idesplit = line.split('|')
                if len(idesplit) > 1:
                    idesplit[1] = idesplit[1].replace('[ADJ]',cadj)
                    idesplit[1] = idesplit[1].replace('[NAME]',cfullname)
                    newstr = idesplit[1]
                    print(""+cname+"_"+idesplit[0]+":0 \""+newstr+"\"")
                    txt+="\n "+cname+"_"+idesplit[0]+":0 \""+newstr+"\""
                    print(""+cname+"_"+idesplit[0]+"_DEF:0 \""+newstr+"\"")
                    txt+="\n "+cname+"_"+idesplit[0]+"_DEF:0 \""+newstr+"\""
                    print(""+cname+"_"+idesplit[0]+"_ADJ:0 \""+cadj+"\"")
                    txt+="\n "+cname+"_"+idesplit[0]+"_ADJ:0 \""+cadj+"\""
    f = open("out.yml", "w+")
    
    f.write(txt)
    print("Lines successfully written.")
    f.close()
    print("File Closed.")
else:
    print('Error: could not find file specified.  Please make sure the file is located in the same folder as the python/bat script.')
