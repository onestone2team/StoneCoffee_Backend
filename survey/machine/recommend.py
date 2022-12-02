import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import euclidean_distances 

user_data = {
    "name_ko":["user"],
    "Aroma": [4],
    "Acidity": [3],
    "Sweetness": [3],
    "Bitterness": [2],
    "Balance":[5]
}

usecols = ['name_ko','Aroma','Acidity','Sweetness','Bitterness','Balance']
user_table = pd.DataFrame(user_data, columns=usecols)

datas = pd.read_csv('survey/machine/data.csv', usecols=usecols)
datas = pd.merge(datas, user_table, how='outer', on=None)
df = datas.dropna()

title_table = pd.pivot_table(df, index = ['name_ko'])

item_based_collab = euclidean_distances(title_table, title_table)
item_based_collab = pd.DataFrame(item_based_collab, index=title_table.index, columns=title_table.index)

return_items = item_based_collab['user'].sort_values(ascending=True)[:4].index.tolist()

return_items.remove('user')

print(return_items)

