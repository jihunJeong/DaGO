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
    '''
    Note:
        Reviewer의 리뷰 목록이 들어오면 그 목록에 해당하는 
        Item의 Feature Vector를 얻어 Reviewer의 Profile 만듬

    Args:
        reviewes : Reviewer의 리뷰 목록
        aid : User가 클릭한 제품의 id

    Returns:
        profile : User의 Profile과 클릭한
                    상품을 결합한 최종 Profile    
    '''
    # Feature Vector Load
    matrix_load = sparse.load_npz("./data/feature_matrix.npz")

    # Review 제품과 평점을 이용한 Weighted Average
    first = reviewes[0]
    weighted = first.overall
    profile = matrix_load[AsinId.objects.filter(asin=first.asin).values_list('aid')[0]] * weighted
    for i, o in enumerate(reviewes):
        id = AsinId.objects.filter(asin=o.asin).values_list('aid')[0]
        if i == 0:
            continue
        profile += matrix_load[id] * o.overall # Weighted Average
        weighted += o.overall
    profile = profile / weighted

    beta = 0.5 # Hyper Parameter : 유저 정보를 얼마나 반영할지
    profile = matrix_load[aid] * beta + (1 - beta) * profile
    return profile

def recommend(profile, reviewes, user, item, num):
    '''
    Note:
        Content-Based RecSys을 이용해 상품 추천
    
    Args: 
        profile : 제품을 추천하기 위한 User Feature Vector
        reviewes : User가 리뷰했던 상품들 목록
        user : 추천 받을 User
        item : 사용자가 선택한 Detail Item
        num : 몇 개를 추천 받을 지

    Outputs:
        /data/usercontent/username/item.csv
        User가 추천 받은 목록 파일을 저장
    '''
    reviewes = reviewes.values('asin')
    ids = AsinId.objects.filter(asin__in=reviewes).values_list('aid')
    item_id = AsinId.objects.filter(asin=item.asin).values_list('aid')[0][0]
    id = []
    for i in ids:
        id.append([i[0]]) # 상품의 Id 수집
    matrix_load = sparse.load_npz("./data/feature_matrix.npz")
    cosine_similarities = linear_kernel(profile, matrix_load)

    results = {} # 유사도와 추천 상품 담는 Dict
    non_value_results = {} # 추천 상품만 담는 Dict

    # Feature Vector의 Cosine Similarity를 이용한 상품 추천
    similar_indices = cosine_similarities[0].argsort()[:-100:-1]
    similar_items = [(cosine_similarities[0][i], AsinId.objects.filter(pk=i).values('asin')[0]['asin']) for i in similar_indices if i not in id and i != item_id]
    non_value_similar_items = [AsinId.objects.filter(pk=i).values('asin') for i in similar_indices if i not in id and i != item_id][:num]

    result_df = pd.DataFrame(columns=['asin','similarity'])
    for arr in similar_items:
        result_df = result_df.append({'asin':arr[1], 'similarity':arr[0]}, ignore_index=True)

    # 추천 결과 CSV로 Save
    result_df.to_csv(f"./data/usercontent/{user}/{item.asin}.csv", index=False)

def load_content(reviewes, aid, user, item, num):
    '''
    Note:
        기존에 User와 상품 쌍에 대해 추천한 전적이 있다면 그 내용을 Load
        없다면 새롭게 추천 시작
    '''
    if not os.path.isdir(f'./data/usercontent'):
        os.mkdir(f'./data/usercontent')
    
    if not os.path.isdir(f'./data/usercontent/{user.nickname}'):
        os.mkdir(f'./data/usercontent/{user.nickname}')
    
    if not os.path.isfile(f"./data/usercontent/{user.nickname}/{item.asin}.csv"):
        profile = get_profile(reviewes, aid)
        recommends = recommend(profile, reviewes, user.nickname, item, num=num)
    df = pd.read_csv(f"./data/usercontent/{user.nickname}/{item.asin}.csv")
    recommends = df['asin'][:num]

    return recommends