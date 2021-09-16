from library import *

def split_category(data_dir, result_dir, filename):
    categories = pd.read_json(data_dir+f"/{filename}.json", lines=True, chunksize=1000)
    
    big_df = pd.DataFrame(columns=['name'])
    for idx, category in enumerate(categories):
        print(f"{idx} done")
        for idx, row in category.iterrows():
            pre_df = pre_df.append(pd.Series(row['category'][1], index=pre_df.columns), ignore_index=True)
            pre_df.drop_duplicates(inplace=True)
    pre_df.index = np.arange(1, len(pre_df)+1)
    pre_df.to_csv("../data/category_big_2018.csv")

    big = pd.read_csv(data_path+"category_big_2018.csv", names=['cb_id', 'category'])
    pre_df = pd.DataFrame(columns=['category', 'cb_id'])
    
    info = dict()
    for idx, row in big.iterrows():
        info[row['category']] = row['cb_id']
    print(info)
    for idx, category in enumerate(categories):
        print(f"{idx} done")
        for idx, row in category.iterrows():
            if len(row['category']) <= 2:
                pre_df = pre_df.append(pd.Series(['Extra',  int(info[row['category'][1]])], index=pre_df.columns), ignore_index=True)
            else :
                pre_df = pre_df.append(pd.Series([row['category'][2], int(info[row['category'][1]])], index=pre_df.columns), ignore_index=True)
            pre_df.drop_duplicates(inplace=True)
    pre_df.index = np.arange(1, len(pre_df)+1)
    pre_df.to_csv("../data/category_mid_2018.csv")

    big = pd.read_csv(data_path+"category_big_2018.csv", names=['cb_id', 'category'])
    mid = pd.read_csv(data_path+"category_mid_2018.csv", names=['cm_id', 'category', 'cb_id'])
    pre_df = pd.DataFrame(columns=['name', 'cm_id', 'cb_id'])
    
    info = dict()
    for idx, row in big.iterrows():
        info[row['category']] = row['cb_id']
    
    midd = dict()
    for idx, row in mid.iterrows():
        midd[row['category']] = row['cm_id']
    print(midd)
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

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_dir", type=str, default="../data")
    parser.add_argument("--result_dir", type=str, default="../data")
    parser.add_argument("--filename", type=str, default="category_2018")

    args = parser.parse_args()
    split_category(data_dir=args.data_dir, result_dir=args.result_dir, filename=args.filename)
