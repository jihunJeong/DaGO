from numpy import isin
import pandas as pd


# meta data count : 124415

if __name__ == "__main__":
    data_path = "../data/"
    filename =["clear_meta_2018_40.json", "clear_meta_2018_80.json",
            "clear_meta_2018_120.json","clear_meta_2018_last.json"]
    
    big = pd.read_csv(data_path+"category_big_2018.csv", names=['cb_id', 'category'])
    mid = pd.read_csv(data_path+"category_mid_2018.csv", names=['cm_id', 'category', 'cb_id'])
    small = pd.read_csv(data_path+"category_sm_2018.csv", names=['cs_id', 'category', 'cm_id', 'cb_id'])
    brand = pd.read_csv(data_path+"brand_2018.csv", names=['bid','brand'])

    brandd = dict()
    for idx, row in brand.iterrows():
        brandd[row['brand']] = row['bid']

    bigd = dict()
    for idx, row in big.iterrows():
        bigd[row['category']] = row['cb_id']
    
    midd = dict()
    for idx, row in mid.iterrows():
        if row['category'] == "Extra":
            if "Extra" in midd.keys():
                midd['Extra'][int(row['cb_id'])] = row['cm_id']
            else :
                midd['Extra'] = {int(row['cb_id']) : row['cm_id']} 
        else :
            midd[row['category']] = row['cm_id']
    
    smd = dict()
    for idx, row in small.iterrows():
        if row['category'] == "Extra":
            if "Extra" in smd.keys():
                smd['Extra'][int(row['cm_id'])] = row['cs_id']
            else :
                smd['Extra'] = {int(row['cm_id']) : row['cs_id']} 
        else :
            smd[row['category']] = row['cs_id']
    
    pre_df = pd.DataFrame()
    also_df = pd.DataFrame()
    for name in filename:
        meta_reader = pd.read_json(data_path+name,lines=True,chunksize=1000)

        for idx, meta in enumerate(meta_reader):
            print(f"{idx} done")

            select = meta.copy()
            for i, row in select.iterrows():
                li = []
                for s in row['category']:
                    li.append(s.replace("&amp;", "&"))
                if len(li) >= 2:
                    select.at[i, 'cb'] = int(bigd[li[1]])
                    if len(li) >= 3 and li[2] in midd.keys():
                        select.at[i, 'cm'] = int(midd[li[2]])
                        if len(li) >= 4 and li[3] in smd.keys():
                            select.at[i, 'cs'] = int(smd[li[3]])
                        else :
                            if len(li) < 4:
                                select.at[i, 'cs'] = int(smd['Extra'][int(midd[li[2]])])
                    else :
                        select.at[i, 'cm'] = int(midd['Extra'][int(bigd[li[1]])])
                
                select.at[i, 'brand_id'] = brandd[row['brand'].replace("&amp;", "&")]
            select.drop(columns=['category', 'brand'], inplace=True)
            pre_df = pd.concat([pre_df, select])
    pre_df = pre_df.drop_duplicates(subset=['asin'])
    pre_df = pre_df.drop_duplicates(subset=['title'])
    pre_df['cb'] = pre_df['cb'].astype('int8')
    pre_df['cm'] = pre_df['cm'].astype('int8')
    pre_df['edate'] = pd.to_datetime(pre_df['edate'].astype(str), format='%Y%m%d')
    pre_df['asin'] = pre_df['asin'].astype(str)
    # Delete Trash Value
    pre_df = pre_df[pre_df['asin'] != "B01BB1PJGG"]
    pre_df = pre_df[pre_df['asin'] != "B01AK9UDG6"]
    pre_df = pre_df[pre_df['asin'] != "B01DIL84BY"]
    pre_df = pre_df[pre_df['asin'] != "B01DKAHXNI"]
    pre_df = pre_df[pre_df['asin'] != "BO1DNTWIA4"]

    also_df = pre_df[['asin', 'also_view', 'also_buy']]
    pre_df = pre_df.drop(columns=['also_view', 'also_buy'])
    print(len(pre_df))
    print(len(also_df))
    pre_df.to_csv("../data/item_2018.csv")
    also_df.to_csv("../data/also_item.csv")