import pandas as pd


# meta data count : 154192

if __name__ == "__main__":
    data_path = "../data/"
    meta_reader = pd.read_json(data_path+"meta_2018.json", lines=True, chunksize=1000)
    big = pd.read_csv(data_path+"category_big_2018.csv", names=['cb_id', 'category'])
    mid = pd.read_csv(data_path+"category_mid_2018.csv", names=['cm_id', 'category', 'cb_id'])
    small = pd.read_csv(data_path+"category_sm_2018.csv", names=['cs_id', 'category', 'cb_id', 'cm_id'])
    
    mToN = {"January":"01", "February":"02", "March":"03", "April":"04", "May":"05", "June":"06",
            "July":"07", "August":"08", "September":"09", "October":"10", "November":"11", "December":"12"}
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
    for idx, meta in enumerate(meta_reader):
        print(f"{idx} done")
        select = meta.drop(columns=['fit', 'similar_item','tech1','tech2','also_buy','rank','also_view','main_cat','details']).copy()
        
        for i, row in select.iterrows():
            li = []
            for s in row['category']:
                li.append(s.replace("&amp;", "&"))
            if len(li) >= 2:
                select.at[i, 'cb'] = int(bigd[li[1]])
                if len(li) >= 3:
                    select.at[i, 'cm'] = int(midd[li[2]])
                    if len(li) >= 4:
                        select.at[i, 'cs'] = int(smd[li[3]])
                    else :
                        print(smd['Extra'])
                        select.at[i, 'cs'] = int(smd['Extra'][int(midd[li[2]])])
                else :
                    select.at[i, 'cm'] = int(midd['Extra'][int(bigd[li[1]])])
            

            select.at[i, 'brand'] = row['brand'].replace("&amp;", "&")
            if row['price']:
                select.at[i, 'price'] = row['price'].replace("$", "")
            else :
                select.at[i, 'price'] = None

            if row['date']:
                if not isinstance(row['date'], str) or len(row['date'].split()) != 3:
                    select.at[i, 'date'] = None
                    continue
                m, d, year = row['date'].split()
                if m not in mToN.keys():
                    select.at[i, 'date'] = None
                    continue
                select.at[i, 'date'] = year+"-"+mToN[m]+"-"+"0"*(3-len(d))+d[:-1]
            else :
                select.at[i, 'date'] = None
                
        pre_df = pd.concat([pre_df, select])
        if (idx+1)%40 == 0:
            pre_df.to_json(f"../data/item_2018_{(idx+1)}.json", orient='records', lines=True)
            pre_df = pd.DataFrame()
    pre_df.to_json(f"../data/item_2018_last.json", orient='records', lines=True)