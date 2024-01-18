import pandas as pd
import re
df=pd.read_csv("*.csv", header=None, engine='python',sep='[:|]', quotechar="'")
#df.head()
pattern = r'(\d+)'
def strngsplt(item):
    if item is None:
        return []
    else:
        item=re.findall(pattern, item)
    return item
df[1]=df[1].apply(strngsplt)
df[2]=df[2].apply(strngsplt)
df.head()
dic={i:1 for i in range(1,len(df)+1)}
for i in range(len(df)):
    count=sum(1 for ele in df.iloc[i][2] if ele in df.iloc[i][1])
    #print(count)
    k=1
    while k<=dic[i+1]:
        for j in range(i+2,i+count+2):
            dic[j]+=1
            #print(dic)
        k+=1
print(sum(dic.values()))