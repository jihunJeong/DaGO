import pandas as pd

if __name__ == "__main__":
    data_path = "../data/"
    categories = pd.read_json(data_path+"test_category_2018.json", lines=True, chunksize=1000)

    pre_df = pd.DataFrame()
    
    for idx, category in enumerate(categories):
        print(f"{idx} done")
        for idx, row in category.iterrows():
            prd_df = pd.concat([pre_df, pd.Series(row['category'][1])])
            pre_df.drop_duplicates(inplace=True)
    pre_df.to_csv("../data/category_big_2018.csv", index=False)