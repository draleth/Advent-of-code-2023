import pandas as pd
import re
dft=pd.read_csv("*.csv", header=None, engine='python',sep='\n|:|;',names=['game','draw1','draw2','draw3','draw4','draw5','draw6'], quotechar="'")
#print(dft.info())
#dft.head()
pattern = r'(\d+|\w+)'
def strngsplt(item):
    if item is None:
        return []
    else:
        item=re.findall(pattern, item)
    return item
dft["draw1"]=dft["draw1"].apply(strngsplt)
dft["draw2"]=dft["draw2"].apply(strngsplt)
dft["draw3"]=dft["draw3"].apply(strngsplt)
dft["draw4"]=dft["draw4"].apply(strngsplt)
dft["draw5"]=dft["draw5"].apply(strngsplt)
dft["draw6"]=dft["draw6"].apply(strngsplt)
#dft.head()
#12 red cubes, 13 green cubes, and 14 blue cubes
def gametrue(glist):
    l=len(glist)
    rd,gr,bl=0,0,0
    if l==0:
        glist=True
    else:
        for i in range(1,l+1,2):
            if glist[i]=="blue":
                bl=int(glist[i-1])
            elif glist[i]=="green":
                gr=int(glist[i-1])
            elif glist[i]=="red":
                rd=int(glist[i-1])
    if rd<=12 and gr<=13 and bl<=14:
        glist=True
    else:
        glist=False
    return glist
dft["draw1"]=dft["draw1"].apply(gametrue)
dft["draw2"]=dft["draw2"].apply(gametrue)
dft["draw3"]=dft["draw3"].apply(gametrue)
dft["draw4"]=dft["draw4"].apply(gametrue)
dft["draw5"]=dft["draw5"].apply(gametrue)
dft["draw6"]=dft["draw6"].apply(gametrue)
dft.drop(columns="game",inplace=True)
flist=dft.all(axis=1)
slist=[]
for index,bval in enumerate(flist):
    if bval==True:
        slist.append(index+1)
    else:
        continue
#print(slist)
print(sum(slist))