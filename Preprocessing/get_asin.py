import pandas as pd

if __name__ == "__main__":
    data_path = "../data/"
    review_reader = pd.read_csv(data_path+"review_2018.csv", chunksize=1000)

    pre_df = pd.DataFrame()
    for idx, review in enumerate(review_reader):
        print(f"{idx} done")
        select = review["asin"]
        pre_df = pd.concat([pre_df, select])
        pre_df.drop_duplicates(inplace=True)

    
    pre_df.to_csv("../data/asin_2018.csv", index=False, header=False)