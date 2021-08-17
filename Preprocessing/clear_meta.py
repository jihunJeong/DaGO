import pandas as pd


# meta data count : 154192

if __name__ == "__main__":
    mToN = {"January":"01", "February":"02", "March":"03", "April":"04", "May":"05", "June":"06",
            "July":"07", "August":"08", "September":"09", "October":"10", "November":"11", "December":"12"}
    
    data_path = "../data/"
    meta_reader = pd.read_json(data_path+"meta_2018.json", lines=True, chunksize=1000)
    
    pre_df = pd.DataFrame()
    cnt = 0
    for idx, meta in enumerate(meta_reader):
        print(f"{idx} done")
        select = meta.drop(columns=['fit', 'similar_item','tech1','tech2','rank','details','main_cat']).copy()
        
        for i, row in select.iterrows():
            li = []
            for s in row['category']:
                li.append(s.replace("&amp;", "&"))
            select.at[i, 'category'] = li

            if not row['feature']:
                select.at[i, 'feature'] = None

            if not row['description']:
                select.at[i, 'description'] = None

            if not row['brand'].replace("&amp;", "&"):
                select.at[i, 'brand'] = None
            else :
                if "by" in str(row['brand']):
                    select.at[i, 'brand'] = None
                else :
                    select.at[i, 'brand'] = row['brand'].replace("&amp;", "&")

            if row['price']:
                if not row['price'].replace(".", "1").replace("$", "").isdigit():
                    select.at[i, 'price'] = None
                else :
                    select.at[i, 'price'] = row['price'].replace("$", "")

            if row['date']:
                if not isinstance(row['date'], str) or len(row['date'].split()) != 3 or "div" in str(row['date']):
                    select.at[i, 'edate'] = "20210101"
                else :
                    m, d, year = row['date'].split()
                    if m not in mToN.keys():
                        select.at[i, 'edate'] = "20210101"
                    else :
                        select.at[i, 'edate'] = year+mToN[m]+"0"*(3-len(d))+d[:-1]
            else :
                select.at[i, 'edate'] = "20210101"
        select.drop(columns=['date'], inplace=True)    
        pre_df = pd.concat([pre_df, select])
        if (idx+1)%40 == 0:
            pre_df.dropna(inplace=True)
            cnt += len(pre_df)
            pre_df.to_json(f"../data/clear_meta_2018_{(idx+1)}.json", orient='records', lines=True)
            pre_df = pd.DataFrame()
    pre_df.dropna(inplace=True)
    cnt += len(pre_df)
    print(cnt)
    pre_df.to_json(f"../data/clear_meta_2018_last.json", orient='records', lines=True)