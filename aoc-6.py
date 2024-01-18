import pandas as pd
import re
df=pd.read_csv("*.csv",sep='[:]', header=None, engine='python', quotechar="'")
#df
df=df[1].str.split(expand=True).astype(int)
#df[0]
el=1
for i in range(len(df.columns)):
    count=0
    for time in range(1,df[i][0]):
        time_rem= df[i][0]-time
        dist= time * time_rem
        if dist > df[i][1]:
            count+=1
    el*=count
print(el)
