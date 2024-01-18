import pandas as pd
import re
from collections import Counter
df=pd.read_csv("*.csv",sep='[ ]',engine='python',quotechar="'",header=None)
# df.head()
# len(df)
lst_class=[]
for i in range(len(df)):
    lst_hand=list(df[0][i])
    dic_hand=dict(Counter(lst_hand))
    if "J" in dic_hand:
        if len(dic_hand)==1:
            lst_class.append("5oK")
            continue
        else:
            max_key=max(dic_hand, key=dic_hand.get)
            if max_key == "J":
                dic_hand_2=dict(Counter(lst_hand))
                del dic_hand_2["J"]
                max_key_2=max(dic_hand_2, key= dic_hand_2.get)
                dic_hand[max_key_2]+=dic_hand["J"]
                del dic_hand["J"]
            else:
                dic_hand[max_key]+=dic_hand["J"]
                del dic_hand["J"]
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
    #else:
        #lst_class.append("HC")
# len(lst_class)
rank={"5oK":1,"4oK":2,"FH":3,"3oK":4,"2P":5,"1P":6,"HC":7}
card_rank = {
    'A': 1, 'K': 2, 'Q': 3, 'T': 4,
    '9': 5, '8': 6, '7': 7, '6': 8, '5': 9,
    '4': 10, '3': 11, '2': 12, 'J': 13  # Assigning 'J' the value 13
}
hand_type=list(rank.keys())
df["hand"]=lst_class
def hand_sort(char):
    return rank[char]

def card_sort(cards):
    return [card_rank.get(char) for char in cards]
# df.head()
df1=df.iloc[df[0].map(card_sort).sort_values().index]
df1=df1.reset_index(drop=True)
# df1
temp_df=df1["hand"].map(hand_sort).to_frame(name="vals")
temp_df["og_index"]=temp_df.index
sort_temp_df=temp_df.sort_values(by=["vals","og_index"])
dff=df1.iloc[sort_temp_df["og_index"]]
dff=dff.reset_index(drop=True)
dff["f_rank"]=list(range(len(df),0,-1))
sum(dff[1] * dff["f_rank"])
f_lst=list(dff[1] * dff["f_rank"])
print(sum(f_lst))
# dff["sum"]=f_lst