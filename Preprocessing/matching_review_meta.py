import pandas as pd

if __name__ == "__main__":
    data_path = "../data/"
    review = pd.read_json(data_path+"review_2016_2018.csv")
    meta_reader = pd.read_json(data_path+"meta_Electronics.json.csv", lines=True, chunksize=100)
    
    pre_meta_df = pd.DataFrame()
    for idx, meta in enumerate(meta_reader):
        select = meta[meta["asin"].apply(lambda x: review["asin"].str.match(x, na=False))]
        pre_meta_df = pd.concat([pre_meta_df, select])

    pre_meta_df.to_csv("../data/meta_2016_2018.csv", index=False)