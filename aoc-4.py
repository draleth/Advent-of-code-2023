import pandas as pd
import re
df=pd.read_csv("*.csv", header=None, engine='python',sep='[:|]', quotechar="'")
#df
pattern = r'(\d+)'
def strngsplt(item):
    if item is None:
        return []
    else:
        item=re.findall(pattern, item)
    return item
df[1]=df[1].apply(strngsplt)
df[2]=df[2].apply(strngsplt)
#df
#df.iloc[0]
fl=[]
for i in range(len(df)):
    count=sum(1 for ele in df.iloc[i][2] if ele in df.iloc[i][1])
    if count>0:
        pwr=2**(count-1)
        fl.append(pwr)
    else:
        continue
#print(fl)
print(sum(fl))
