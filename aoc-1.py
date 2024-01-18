import pandas as pd
num=list(range(0,10))
num=list(map(str,num))
filepath="~/*.csv"
df=pd.read_csv(filepath)
new=[]
for line in df['lines']:
    n=[]
    for char in line:
        if char.isdigit():
            #print(nm)
            n.append(char)
    new.append(n)
fr=[]
for ln in new:
    if len(ln)==1:
        ab=int(ln[0]+ln[0])
    else:
        ab=int(ln[0]+ln[-1])
    fr.append(ab)  
print(sum(fr))