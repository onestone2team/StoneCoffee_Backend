import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import euclidean_distances 


def recommend_start(Aroma, Acidity, Sweetness, Balance):
    user_data = {
        "name_ko":["user"],
        "aroma_grade": [Aroma],
        "acidity_grade": [Acidity],
        "sweet_grade": [Sweetness],
        "body_grade":[Balance]
    }

    usecols = ['name_ko','aroma_grade','acidity_grade','sweet_grade', 'body_grade']
    user_table = pd.DataFrame(user_data, columns=usecols)

    datas = pd.read_csv('machine/data.csv', usecols=usecols)
    datas = pd.merge(datas, user_table, how='outer', on=None)
    df = datas.dropna()

    title_table = pd.pivot_table(df, index = ['name_ko'])

    item_based_collab = euclidean_distances(title_table, title_table)
    item_based_collab = pd.DataFrame(item_based_collab, index=title_table.index, columns=title_table.index)

    return_items = item_based_collab['user'].sort_values(ascending=True)[:4].index.tolist()

    return_items.remove('user')

    return return_items

