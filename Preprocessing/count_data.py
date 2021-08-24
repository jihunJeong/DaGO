import pandas as pd
import numpy  as np

if __name__ == "__main__":
    data_path = "../data/"

    count = 0    
    review_reader = pd.read_csv(data_path+'clear_review_2018.csv')
    g = review_reader[(review_reader['reviewerID'] == 'A3RW697Y2EZWUL') | (review_reader['reviewerID'] =='ALDWXFCCVIGGR')]
    g.drop(columns=['Unnamed: 0'], inplace=True)
    g.index = np.arange(1, len(g)+1)
    g.to_csv(data_path+"persona_review.csv")
    
    
    

    
