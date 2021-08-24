import re
from numpy import mat
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from scipy import sparse
from product.models import AsinId, Review
import pandas as pd
import os

def get_profile(reviewes, aid):
    matrix_load = sparse.load_npz("./data/feature_matrix.npz")

    first = reviewes[0]
    weighted = first.overall
    profile = matrix_load[AsinId.objects.filter(asin=first.asin).values_list('aid')[0]] * weighted
    for i, o in enumerate(reviewes):
        id = AsinId.objects.filter(asin=o.asin).values_list('aid')[0]
        if i == 0:
            continue
        profile += matrix_load[id] * o.overall
        weighted += o.overall
    profile = profile / weighted

    beta = 0.5
    profile = matrix_load[aid] * beta + (1 - beta) * profile
    return profile

def recommend(profile, reviewes, user, item, num):
    reviewes = reviewes.values('asin')
    ids = AsinId.objects.filter(asin__in=reviewes).values_list('aid')
    item_id = AsinId.objects.filter(asin=item.asin).values_list('aid')[0][0]
    id = []
    for i in ids:
        id.append([i[0]])
    matrix_load = sparse.load_npz("./data/feature_matrix.npz")
    cosine_similarities = linear_kernel(profile, matrix_load)

    results = {}
    non_value_results = {}
    similar_indices = cosine_similarities[0].argsort()[:-100:-1]
    similar_items = [(cosine_similarities[0][i], AsinId.objects.filter(pk=i).values('asin')[0]['asin']) for i in similar_indices if i not in id and i != item_id]
    non_value_similar_items = [AsinId.objects.filter(pk=i).values('asin') for i in similar_indices if i not in id and i != item_id][:num]

    result_df = pd.DataFrame(columns=['asin','similarity'])
    for arr in similar_items:
        result_df = result_df.append({'asin':arr[1], 'similarity':arr[0]}, ignore_index=True)

    result_df.to_csv(f"./data/usercontent/{user}/{item.asin}.csv", index=False)
    return non_value_similar_items

def load_content(reviewes, aid, user, item, num):
    if not os.path.isdir(f'./data/usercontent/{user.nickname}'):
        os.mkdir(f'./data/usercontent/{user.nickname}')
    
    if not os.path.isfile(f"./data/usercontent/{user.nickname}/{item.asin}.csv"):
        profile = get_profile(reviewes, aid)
        recommends = recommend(profile, reviewes, user.nickname, item, num=num)
    else :
        df = pd.read_csv(f"./data/usercontent/{user.nickname}/{item.asin}.csv")
        recommends = df['asin'][:num]
        print(recommends)

    return recommends