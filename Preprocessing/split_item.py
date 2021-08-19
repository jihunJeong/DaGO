import pandas as pd

if __name__ == "__main__":
    data_path = "../data/"
    df = pd.read_csv(data_path+"item_2018.csv")

    for i in range(1, 16):
        g = df.groupby(['cb']).get_group(i)
        g.to_csv(data_path+f"split_item/split_item_2018_{i}.csv")