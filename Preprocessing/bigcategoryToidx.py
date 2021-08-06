import pandas as pd

if __name__ == "__main__":
    data_path = "../data/"
    categories = pd.read_json(data_path+"category_2018.json", lines=True, chunksize=1000)
    big = pd.read_csv(data_path+"id_category_big_2018.csv")

    pre_df = pd.DataFrame(columns=['category'])
    
    for idx, category in enumerate(categories):
        print(f"{idx} done")
        for idx, row in category.iterrows():
            pre_df = pre_df.append(pd.Series(row['category'][1], index=pre_df.columns), ignore_index=True)
            pre_df.drop_duplicates(inplace=True)
    pre_df.to_csv("../data/category_idx_2018.csv", index=False)