import pandas as pd

if __name__ == "__main__":
    data_path = "../data/"
    meta_reader = pd.read_json(data_path+"meta_Electronics.json", lines=True, chunksize=1000)
    
    pre_meta_df = pd.DataFrame()
    for idx, meta in enumerate(meta_reader):
        print(f"{idx} done")
        pre_meta_df = pd.concat([pre_meta_df, meta])

        if (idx+1) % 40 == 0:
            print(pre_meta_df['category'])
            pre_meta_df.to_json(data_path+f"meta_2018_{(idx+1)}.json", orient="records", lines=True)
            break