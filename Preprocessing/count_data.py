import pandas as pd

if __name__ == "__main__":
    data_path = "../data/"

    count = 0    
    review_reader = pd.read_csv(data_path+'clear_review_2018.csv')
    g = review_reader.groupby('overall').size()
    print(g)

   
