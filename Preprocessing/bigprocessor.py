import pandas as pd

if __name__ == "__main__":
    data_path = "../data/"
    review_reader = pd.read_json(data_path+"Electronics.json", lines=True,chunksize=1000)

    pre_df = pd.DataFrame()
    for idx, review in enumerate(review_reader):
        print(f"{idx} done")
        select = review[review["reviewTime"].apply(lambda x: int(x.split()[2]) >= 2018)]
        pre_df = pd.concat([pre_df, select])
    
    pre_df.to_json("../data/review_2018.json", orient='records', lines=True)