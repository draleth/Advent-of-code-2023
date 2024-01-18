import pandas as pd
import re
df=pd.read_csv("*.csv",sep='[:]', header=None, engine='python', quotechar="'")
#df
df=df[1].str.replace(" ","").astype(int)
#df[0]
count=0
for time in range(14,df[0]-13):
    time_rem= df[0]-time
    dist= time * time_rem
    if dist > df[1]:
        count+=1
print(count)
