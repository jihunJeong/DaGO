import pandas as pd

if __name__ == "__main__":
    data_path = "../data/"
    
    filename =["clear_meta_2018_40.json", "clear_meta_2018_80.json",
            "clear_meta_2018_120.json","clear_meta_2018_last.json"]

    pre_df = pd.DataFrame()
    for name in filename:
        meta_data = pd.read_json(data_path+name,lines=True,chunksize=1000)

        for idx, meta in enumerate(meta_data):
            print(f"{idx} done")
            select = meta[["category"]]
            pre_df = pd.concat([pre_df, select])
            pd.DataFrame(pre_df, columns=pre_df.columns)
    
    pre_df.to_json("../data/category_2018.json", orient="records",lines=True)