import pandas as pd

# review row : 1485031

if __name__ == "__main__":
    data_path = "../data/"
    review_reader = pd.read_csv(data_path+"category_big_2018.csv")
    review_reader.index += 1
    review_reader.to_csv(f"../data/id_category_big_2018.csv")