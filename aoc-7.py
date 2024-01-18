import pandas as pd
import re
from collections import Counter
df=pd.read_csv("*.csv",sep='[ ]',engine='python',quotechar="'",header=None)
#df.head()
lst_class=[]
for i in range(len(df)):
    lst_hand=list(df[0][i])
    dic_hand=Counter(lst_hand)
    lst_count=list(dic_hand.values())
    lst_count.sort(reverse=True)
    len_count=len(lst_count)
    if len_count==1 and lst_count[0]==5:
        lst_class.append("5oK")
    elif len_count==2 and lst_count[0]==4:
        lst_class.append("4oK")
    elif len_count==2 and lst_count[0]==3 and lst_count[1]==2:
        lst_class.append("FH")
    elif len_count==3 and lst_count[0]==3 and lst_count[1]==1:
        lst_class.append("3oK")
    elif len_count==3 and lst_count[0]==2 and lst_count[1]==2:
        lst_class.append("2P")
    elif len_count==4 and lst_count[0]==2 and lst_count[1]==1 and lst_count[2]==1:
        lst_class.append("1P")
    elif len_count==5 and lst_count[0]==1:
        lst_class.append("HC")
    else:
        lst_class.append("HC")
rank={"5oK":1,"4oK":2,"FH":3,"3oK":4,"2P":5,"1P":6,"HC":7}
card_rank={
    'A': 1, 'K': 2, 'Q': 3, 'J': 4, 'T': 5,
    '9': 6, '8': 7, '7': 8, '6': 9, '5': 10,
    '4': 11, '3': 12, '2': 13
}
hand_type=list(rank.keys())
df["hand"]=lst_class
def hand_sort(char):
    return rank[char]

def card_sort(cards):
    return [card_rank.get(char) for char in cards]
#df.head()
df1=df.iloc[df[0].map(card_sort).sort_values().index]
df1=df1.reset_index(drop=True)
#df1
df1.iloc[df1["hand"].map(hand_sort).sort_values().index]
temp_df=df1["hand"].map(hand_sort).to_frame(name="vals")
temp_df["og_index"]=temp_df.index
sort_temp_df=temp_df.sort_values(by=["vals","og_index"])
dff=df1.iloc[sort_temp_df["og_index"]]
dff=dff.reset_index(drop=True)
dff["f_rank"]=list(range(1000,0,-1))
f_lst=list(dff[1] * dff["f_rank"])
print(sum(f_lst))
#dff.tail(10)
