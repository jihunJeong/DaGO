import pandas as pd

if __name__ == "__main__":
    data_path = "../data/"
    categories = pd.read_csv(data_path+"category_2018.csv", chunksize=1000)

    pre_big = pd.DataFrame()
    pre_mid = pd.DataFrame()
    pre_sm = pd.DataFrame()
    
    for idx, category in enumerate(categories):
        print(f"{idx} done")
        for idx, row in category.iterrows():
            print(row['category'])
            print(row['category'][1])
            prd_df = pd.concat([pre_df, pd.DataFrame(row['category'][1])])
            pre_df.drop_duplicates(inplace=True)
    pre_df.to_csv("../data/category_big_2018.csv", index=False)