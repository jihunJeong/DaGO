import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

ds = pd.read_csv("../data/item_2018.csv").head(10000)

tf = TfidfVectorizer(analyzer='word', ngram_range=(1,3), min_df=0, stop_words='english')
tfidf_matrix = tf.fit_transform(ds['feature'])

cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)
print("Done")
results = {}
for idx, row in ds.iterrows():
    similar_indices = cosine_similarities[idx].argsort()[:-100:-1]
    similar_items = [(cosine_similarities[idx][i], ds['asin'][i]) for i in similar_indices]

    results[row['asin']] = similar_items[1:]

print(results.keys())
print("Done")

def item(asin):
    return ds.loc[ds['asin'] == asin]['asin'] + " --- " + ds.loc[ds['asin'] == asin]['title']

def recommend(item_asin, num):
    print("Recommending " + str(num) + " products similar to " + item(item_asin) + "...")
    print("-------")
    recs = results[item_asin][:num]
    for rec in recs:
        print("Recommended: " + item(rec[1]))
        print("(score:" + str(rec[0]) + ")")
    

recommend(item_asin='B001DFUSR6', num=5)