import pandas as pd

if __name__ == "__main__":
    data_path = "../data/"
    categories = pd.read_json(data_path+"category_2018.json", lines=True, chunksize=1000)
    big = pd.read_csv(data_path+"category_big_2018.csv", names=['cb_id', 'category'])
    mid = pd.read_csv(data_path+"category_mid_2018.csv", names=['cm_id', 'category', 'cb_id'])
    pre_df = pd.DataFrame(columns=['category', 'cm_id', 'cb_id'])
    
    info = dict()
    for idx, row in big.iterrows():
        info[row['category']] = row['cb_id']
    
    midd = dict()
    for idx, row in mid.iterrows():
        midd[row['category']] = row['cm_id']

    for idx, category in enumerate(categories):
        print(f"{idx} done")
        for idx, row in category.iterrows():
            if len(row['category']) <= 2 or row['category'][2] not in midd.keys():
                continue
            elif len(row['category']) <= 3:
                pre_df = pre_df.append(pd.Series(['Extra', int(midd[row['category'][2]]), int(info[row['category'][1]])], index=pre_df.columns), ignore_index=True)
            else :
                pre_df = pre_df.append(pd.Series([row['category'][3], int(midd[row['category'][2]]), int(info[row['category'][1]])], index=pre_df.columns), ignore_index=True)
            pre_df.drop_duplicates(inplace=True)
    pre_df.to_csv("../data/category_sm_2018.csv")