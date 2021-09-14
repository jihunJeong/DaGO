import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

datapath = "../data/split_item/"
for i in range(5, 6):
    result_df = pd.DataFrame(columns=['asin', 'recommend'])
    non_value_result_df = pd.DataFrame(columns=['asin', 'recommend'])

    ds = pd.read_csv(datapath+f"split_item_2018_{i}.csv")
    tf = TfidfVectorizer(analyzer='word', ngram_range=(1,3), min_df=0, stop_words='english')
    tfidf_matrix = tf.fit_transform(ds['feature'])
    print(tfidf_matrix.shape)
    print(type(tfidf_matrix))
    
    cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)
    print(f"{i} Done")
    
    results = {}
    non_value_results = {}
    for idx, row in ds.iterrows():
        print(idx, row['asin'])
        similar_indices = cosine_similarities[idx].argsort()[:-100:-1]

        similar_items = [(cosine_similarities[idx][i], ds['asin'][i]) for i in similar_indices]
        non_value_similar_items = [ds['asin'][i] for i in similar_indices]

        results[row['asin']] = similar_items[1:]
        non_value_results[row['asin']] = non_value_similar_items[1:]
    print(f"{i} Done")

    def recommend(item_asin, num):
        recs = results[item_asin][:num]
        non_value_recs = non_value_results[item_asin][:num]
        return recs, non_value_recs
        
    for key in results.keys():
        res, non_value_res = recommend(item_asin=key, num=10)
        result_df = result_df.append({'asin' : key, 'recommend' : res}, ignore_index=True)
        non_value_result_df = non_value_result_df.append({'asin' : key, 'recommend' : non_value_res}, ignore_index=True)
    
    result_df.to_csv(datapath+f"result_item_{i}.csv")
    non_value_result_df.to_csv(datapath+f"db_result_item_{i}.csv")