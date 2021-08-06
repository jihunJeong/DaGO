import pandas as pd

# review row : 1485031

if __name__ == "__main__":
    data_path = "../data/"
    review_reader = pd.read_json(data_path+"review_2018.json", lines=True,chunksize=1000)

    pre_df = pd.DataFrame()
    for idx, review in enumerate(review_reader):
        print(f"{idx} done")
        select = review[["overall","reviewTime",
                         "reviewerID", "asin","reviewText"]]
        pre_df = pd.concat([pre_df, select])
        pre_df.drop_duplicates(inplace=True)
        if (idx+1)%100 == 0:
            pre_df.to_json(f"../data/clear_review_2018_{(idx+1)}.json", orient='records', lines=True)
            pre_df = pd.DataFrame()
    pre_df.to_json(f"../data/clear_review_2018_last.json", orient='records', lines=True)