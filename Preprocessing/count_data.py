import pandas as pd
import numpy  as np

if __name__ == "__main__":
    data_path = "../data/"

    count = 0    
    review_reader = pd.read_csv(data_path+'clear_review_2018.csv')
    t = review_reader.groupby('reviewerID')['reviewerID'].count().nlargest(1000)
    print(t)
    g = review_reader[(review_reader['reviewerID'] == 'A1NSAEZV6AQP2X') | (review_reader['reviewerID'] =='A1O09DT1PREH9Y')]
    g.drop(columns=['Unnamed: 0'], inplace=True)
    g.index = np.arange(1, len(g)+1)
    g.to_csv(data_path+"persona_review.csv")
    

    
