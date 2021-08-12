import pandas as pd
import gzip

def parse(path):
  g = gzip.open(path, 'rb')
  for l in g:
    yield json.loads(l)

def getDF(path):
  i = 0
  df = {}
  for d in parse(path):
    df[i] = d
    i += 1
  return pd.DataFrame.from_dict(df, orient='index')

df = getDF('reviews_Video_Games.json.gz')
if __name__ == "__main__":
    data_path = "../data/"
    meta_reader = pd.read_json(data_path+"meta_Electronics.json", lines=True, chunksize=1000)
    
    pre_meta_df = pd.DataFrame()
    for idx, meta in enumerate(meta_reader):
        print(f"{idx} done")
        pre_meta_df = pd.concat([pre_meta_df, meta])

    pre_meta_df.to_json(data_path+f"meta_2018.json", orient="records", lines=True)