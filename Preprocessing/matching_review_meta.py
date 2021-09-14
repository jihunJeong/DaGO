import pandas as pd

if __name__ == "__main__":
    data_path = "../data/"
    review = pd.read_csv(data_path+"asin_2018.csv", names=['asin'])
    meta_reader = pd.read_json(data_path+"review_2018.json", lines=True, chunksize=1000)
    
    pre_meta_df = pd.DataFrame()
    for idx, meta in enumerate(meta_reader):
        print(f"{idx} done")
        select = meta[meta["asin"].apply(lambda x: (review["asin"] == x).any())]
        pre_meta_df = pd.concat([pre_meta_df, select])

    pre_meta_df.to_json(data_path+"review_2018.json", orient='records', lines=True)