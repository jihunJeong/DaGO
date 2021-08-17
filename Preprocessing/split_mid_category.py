import pandas as pd
import numpy as np

if __name__ == "__main__":
    data_path = "../data/"
    categories = pd.read_json(data_path+"category_2018.json", lines=True, chunksize=1000)
    big = pd.read_csv(data_path+"category_big_2018.csv", names=['cb_id', 'category'])
    pre_df = pd.DataFrame(columns=['category', 'cb_id'])
    
    info = dict()
    for idx, row in big.iterrows():
        info[row['category']] = row['cb_id']
    print(info)
    for idx, category in enumerate(categories):
        print(f"{idx} done")
        for idx, row in category.iterrows():
            if len(row['category']) <= 2:
                pre_df = pre_df.append(pd.Series(['Extra',  int(info[row['category'][1]])], index=pre_df.columns), ignore_index=True)
            else :
                pre_df = pre_df.append(pd.Series([row['category'][2], int(info[row['category'][1]])], index=pre_df.columns), ignore_index=True)
            pre_df.drop_duplicates(inplace=True)
    pre_df.index = np.arange(1, len(pre_df)+1)
    pre_df.to_csv("../data/category_mid_2018.csv")