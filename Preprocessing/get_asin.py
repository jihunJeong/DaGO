import pandas as pd
import numpy as np

if __name__ == "__main__":
    data_path = "../data/"
    review_reader = pd.read_csv(data_path+"item_2018.csv", chunksize=1000)

    pre_df = pd.DataFrame(columns=['asin'])
    for idx, review in enumerate(review_reader):
        print(f"{idx} done")
        select = review[["asin"]]
        pre_df = pd.concat([pre_df, select], ignore_index=True)
        pre_df.drop_duplicates(inplace=True)
    
    pre_df.index = np.arange(0, len(pre_df))
    pre_df.drop(columns=['asin'],inplace=True)
    pre_df.to_csv("../data/asin_2018.csv")