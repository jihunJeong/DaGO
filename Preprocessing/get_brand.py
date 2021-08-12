import pandas as pd
import numpy as np

if __name__ == "__main__":
    data_path = "../data/"
    
    filename =["clear_meta_2018_40.json", "clear_meta_2018_80.json",
            "clear_meta_2018_120.json","clear_meta_2018_last.json"]

    pre_df = pd.DataFrame(columns=['brand'])
    for name in filename:
        meta_data = pd.read_json(data_path+name,lines=True,chunksize=1000)

        for idx, meta in enumerate(meta_data):
            print(f"{idx} done")
            select = meta[["brand"]]
            pre_df = pd.concat([pre_df, select])
            pre_df.drop_duplicates(inplace=True)
    pre_df.index = np.arange(1, len(pre_df)+1)
    pre_df.to_csv("../data/brand_2018.csv")