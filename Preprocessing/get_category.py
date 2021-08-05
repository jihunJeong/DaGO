import pandas as pd

if __name__ == "__main__":
    data_path = "../data/"
    
    filename =["clear_meta_2018_40.csv", "clear_meta_2018_80.csv",
    "clear_meta_2018_120.csv", "clear_meta_2018_last.csv"]

    pre_df = pd.DataFrame()
    for name in filename:
        review_reader = pd.read_csv(data_path+name, chunksize=1000)

        for idx, review in enumerate(review_reader):
            print(f"{idx} done")
            select = review[["category"]]
            pre_df = pd.concat([pre_df, select])
            pre_df.drop_duplicates(inplace=True)
    
    pre_df.to_csv("../data/category_2018.csv")