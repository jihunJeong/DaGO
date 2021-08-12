import pandas as pd


# meta data count : 154192

if __name__ == "__main__":
    data_path = "../data/"
    meta_reader = pd.read_json(data_path+"meta_2018.json", lines=True, chunksize=1000)
    
    pre_df = pd.DataFrame()
    for idx, meta in enumerate(meta_reader):
        print(f"{idx} done")
        select = meta.drop(columns=['fit', 'similar_item','tech1','tech2','rank','details','main_cat']).copy()
        
        for i, row in select.iterrows():
            li = []
            for s in row['category']:
                li.append(s.replace("&amp;", "&"))
            select.at[i, 'category'] = li

            select.at[i, 'brand'] = row['brand'].replace("&amp;", "&")

        pre_df = pd.concat([pre_df, select])
        if (idx+1)%40 == 0:
            pre_df.to_json(f"../data/clear_meta_2018_{(idx+1)}.json", orient='records', lines=True)
            pre_df = pd.DataFrame()
    pre_df.to_json(f"../data/clear_meta_2018_last.json", orient='records', lines=True)