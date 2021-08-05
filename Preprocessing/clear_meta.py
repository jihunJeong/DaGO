import pandas as pd

if __name__ == "__main__":
    data_path = "../data/"
    meta_reader = pd.read_csv(data_path+"meta_2018.csv", chunksize=1000)
    
    pre_df = pd.DataFrame()
    for idx, meta in enumerate(meta_reader):
        print(f"{idx} done")
        select = meta.drop(columns=['fit', 'similar_item','tech1','tech2'])
        select['category'] = select['category'].str.replace("&amp;", "&")
        pre_df = pd.concat([pre_df, select])
        pre_df.drop_duplicates(inplace=True)

        if (idx+1)%40 == 0:
            pre_df.to_csv(f"../data/clear_meta_2018_{(idx+1)}.csv", index=False)
            pre_df = pd.DataFrame()
    pre_df.to_csv(f"../data/clear_meta_2018_last.csv", index=False)