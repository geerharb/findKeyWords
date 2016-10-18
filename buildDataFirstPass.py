import wikipedia
from time import sleep
import time
import string
import os

###
import unicodedata
import sys
tbl = dict.fromkeys(i for i in xrange(sys.maxunicode)
                      if unicodedata.category(unichr(i)).startswith('P'))
def remove_punctuation(text):
    return text.translate(tbl)
###
#for n in range(0,10):
#  sleep(1.2)
#  print n
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
#print uniques
if not os.path.exists("firstPass"):
  os.makedirs("firstPass")
startTime=time.time()
computationRate=1.0
for i in range(0,len(uniques)):
  subfolder="word%d"%i
  #print "%ETA: %0.2f ; d of %d"%((len(uniques)-i)/computationRate,i,len(uniques))
  if not os.path.exists("firstPass/"+subfolder):
    os.makedirs("firstPass/"+subfolder)
  else:
    print "nothing"
  searchResults=wikipedia.search(uniques[i],results=20)
  #print "print unique=",uniques[i]
  #print searchResults
  sleep(1.1)
  count=-1
  for j in range(0,len(searchResults)):
    if count>=9: break
    if os.path.exists("firstPass/"+subfolder+"/searchResult%d.txt"%(count+1)):
      count+=1
      continue
    searchResult=searchResults[j]
    #print j,"\r",
    
    '''try:
      info=wikipedia.page(searchResults[j])
      count+=1
    except wikipedia.exceptions.DisambiguationError as e:
      continue'''

    try:
      info=wikipedia.page(searchResults[j])
      count+=1
    except KeyboardInterrupt:
      raise
    except:
      continue
    
    
    contentString=info.content
    #contentString=contentString.translate(string.maketrans("",""),string.punctuation)
    contentString=remove_punctuation(contentString)
    contentStrings=contentString.lower().split()
    #contentUniques=[]
    write=open("firstPass/"+subfolder+"/searchResult%d.txt"%count,'w')
    #write=open("firstPass/"+uniques[i]+"/%s.txt"%searchResult,'w')
    write.write("%s\n"%uniques[i].encode("utf-8"))
    write.write("%s\n"%searchResult.encode("utf-8"))
    for content in contentStrings:
      #if content not in contentUniques:
      #  contentUniques.append(content)
      write.write((u"%s\n"%content).encode("utf-8"))
    write.close()
    sleep(1.1)
    computationRate=(i+(count+1)/10.0)/(time.time()-startTime+0.001)
    print "ETA: %0.2f ; %d of %d"%((len(uniques)+j/10.0-i)/computationRate,i,len(uniques))
print len(allStrings)
print len(allStrings)
print len(uniques)


