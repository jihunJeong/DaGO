import pandas as pd
import numpy as np

if __name__ == "__main__":
    data_path = "../data/"
    
    filename =["item_2018.csv"]

    brand = pd.read_csv(data_path+"brand_2018.csv", names=['bid','brand'])
    brandd = dict()
    for idx, row in brand.iterrows():
        brandd[row['brand']] = row['bid']

    pre_df = pd.DataFrame(columns=['brand_id'])
    for name in filename:
        meta_data = pd.read_csv(data_path+name,chunksize=1000)

        for idx, meta in enumerate(meta_data):
            print(f"{idx} done")
            select = meta[["brand_id"]]
            pre_df = pd.concat([pre_df, select])
            pre_df.drop_duplicates(inplace=True)
    pre_df.index = np.arange(1, len(pre_df)+1)
    pre_df.to_csv("../data/id_brand_2018.csv", index=False)