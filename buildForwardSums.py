import wikipedia
from time import sleep
import time
import string
import os
import sys
import numpy as np

###
import unicodedata
import sys
tbl = dict.fromkeys(i for i in xrange(sys.maxunicode)
                      if unicodedata.category(unichr(i)).startswith('P'))
def remove_punctuation(text):
    return text.translate(tbl)
###

###
file=open("input.txt")
datas=file.readlines()
file.close()
allString=""
for arg in datas:
  allString=allString+arg+" "
allString=allString.translate(string.maketrans("",""),string.punctuation)
allStrings=allString.lower().split()
uniques=[]
for arg in allStrings:
  if arg in uniques: continue
  uniques.append(arg)
###

if not os.path.exists("firstPass"):
    sys.exit()
i=0
ranks=[]
while os.path.exists("firstPass/word%d"%i):
    j=0
    forwardSum=0
    totalAttempts=0
    while os.path.exists("firstPass/word%d/searchResult%d.txt"%(i,j)):
        datas=np.loadtxt("firstPass/word%d/searchResult%d.txt"%(i,j),dtype='str',delimiter='\n')
        for k in range(1,len(datas)):
            if datas[k]==datas[0]:
                continue #don't want feedback from what we searched
            totalAttempts+=1
            if datas[k] in uniques: forwardSum+=1
        j+=1
    print 'i=',i,' what what...',datas[0],' ',forwardSum
    ranks.append([datas[0],forwardSum/float(totalAttempts+1)])
    i+=1
######################
if not os.path.exists("firstPass"):
    sys.exit()
i=0
ranks2=[]
while os.path.exists("firstPass/word%d"%i):
    j=0
    forwardSum=0
    totalAttempts=0
    while os.path.exists("firstPass/word%d/searchResult%d.txt"%(i,j)):
        datas=np.loadtxt("firstPass/word%d/searchResult%d.txt"%(i,j),dtype='str',delimiter='\n')
        
        for k in range(1,len(datas)):
            if datas[k]==datas[0]:
                continue #don't want feedback from what we searched
            totalAttempts+=1
            m=0
            while m<len(ranks) and ranks[m][0]!=datas[k]: m+=1
            if m>=len(ranks): multiFactor=1.0
            else: multiFactor=ranks[m][1]
            if datas[k] in uniques: forwardSum+=multiFactor
        j+=1
    print 'i=',i,' what what...',datas[0],' ',forwardSum
    ranks2.append([datas[0],forwardSum/float(totalAttempts+1)])
    i+=1
######################
ranks=ranks2

if not os.path.exists("firstPass"):
    sys.exit()
i=0
ranks2=[]
while os.path.exists("firstPass/word%d"%i):
    j=0
    forwardSum=0
    totalAttempts=0
    while os.path.exists("firstPass/word%d/searchResult%d.txt"%(i,j)):
        datas=np.loadtxt("firstPass/word%d/searchResult%d.txt"%(i,j),dtype='str',delimiter='\n')
        
        for k in range(1,len(datas)):
            if datas[k]==datas[0]:
                continue #don't want feedback from what we searched
            totalAttempts+=1
            m=0
            while m<len(ranks) and ranks[m][0]!=datas[k]: m+=1
            if m>=len(ranks): multiFactor=1.0
            else: multiFactor=ranks[m][1]
            if datas[k] in uniques: forwardSum+=multiFactor
        j+=1
    print 'i=',i,' what what...',datas[0],' ',forwardSum
    ranks2.append([datas[0],forwardSum/float(totalAttempts+1)])
    i+=1
######################
ranks=ranks2

if not os.path.exists("firstPass"):
    sys.exit()
i=0
ranks2=[]
while os.path.exists("firstPass/word%d"%i):
    j=0
    forwardSum=0
    totalAttempts=0
    while os.path.exists("firstPass/word%d/searchResult%d.txt"%(i,j)):
        datas=np.loadtxt("firstPass/word%d/searchResult%d.txt"%(i,j),dtype='str',delimiter='\n')
        
        for k in range(1,len(datas)):
            if datas[k]==datas[0]:
                continue #don't want feedback from what we searched
            totalAttempts+=1
            m=0
            while m<len(ranks) and ranks[m][0]!=datas[k]: m+=1
            if m>=len(ranks): multiFactor=1.0
            else: multiFactor=ranks[m][1]
            if datas[k] in uniques: forwardSum+=multiFactor
        j+=1
    print 'i=',i,' what what...',datas[0],' ',forwardSum
    ranks2.append([datas[0],forwardSum/float(totalAttempts+1)])
    i+=1
######################
ranks=ranks2

print ""

isSorted=False
while isSorted==False:
    isSorted=True
    for i in range(0,len(ranks)-1):
        if ranks[i][1]>ranks[i+1][1]:
            isSorted=False
            temp=ranks[i]
            ranks[i]=ranks[i+1]
            ranks[i+1]=temp

for arg in ranks:
    print arg
        
