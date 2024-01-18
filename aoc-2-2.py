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
dft.drop(columns="game",inplace=True)
slist=[]
for index, row in dft.iterrows():
    r,g,b=0,0,0
    for value in row:
        l=len(value)
        if l==0:
            continue
        else:
            for i in range(1,l+1,2):
                if value[i]=="blue" and int(value[i-1])>b:
                    b=int(value[i-1])
                elif value[i]=="green" and int(value[i-1])>g:
                    g=int(value[i-1])
                elif value[i]=="red" and int(value[i-1])>r:
                    r=int(value[i-1])
    pwr=r*g*b
    slist.append(pwr)
print(sum(slist))
