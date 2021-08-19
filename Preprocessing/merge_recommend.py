import pandas as pd
import numpy as np

if __name__ == "__main__":
    data_path = "../data/split_item/"
    
    pre_df = pd.DataFrame(columns=['asin', 'recommend'])
    for i in range(1, 16):
        ds = pd.read_csv(data_path+f"result_item_{i}.csv",names=['id', 'asin', 'recommend'], header=0)
        ds.drop(columns=['id'], axis=1, inplace=True)
        pre_df = pd.concat([pre_df, ds])
    pre_df.index = np.arange(1, len(pre_df)+1)
    pre_df.to_csv("../data/recommend.csv")