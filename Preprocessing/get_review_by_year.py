from library import *
from preprocessing_data import change_html_expression

def get_review(data_dir, result_dir, year):
    '''
        Args:
            data_dir : review data가 있는 경로
            result_dir : 얻은 review data를 저장할 경로
            year : 선택한 연도 
        
        Note:
            연도를 선택하면 Electronics.json에서 해당 연도 이후
            Review Data 추출 그 후 원하는 Column만 저장

            Overall : Rating of the product
            ReviewTime : Time of the review
            reviewerID : ID of the reviewer
            Asin : ID of the product
            ReviewText : Text of the review
    '''

    print("Split Review ...", flush=True)
    review_reader = pd.read_json(data_dir+"/Electronics.json", lines=True,chunksize=1000)
    print("Origin Count {}".format(20995))
    pre_df = pd.DataFrame()
    for idx, review in enumerate(tqdm(review_reader, desc="Get Review")):
        # Year 기준으로 추출
        select = review[review["reviewTime"].apply(lambda x: int(x.split()[2]) >= year)]
        # 필요한 Column 추출
        select = select[["overall","reviewTime",
                         "reviewerID", "asin","reviewText"]]
        
        for i, row in select.iterrows():
            select.at[i] = change_html_expression(row)

        pre_df = pd.concat([pre_df, select])

    if not os.path.isdir(result_dir): # 저장 경로 존재하지 않는다면 생성
        os.mkdir(result_dir)

    pre_df.index = np.arange(1, len(pre_df)+1)
    pre_df.to_json(result_dir+f"/review_{year}.json", orient='records', lines=True)
    print("Done")
    print("Get Review : {}".format(len(pre_df)))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_dir", type=str, default="../data")
    parser.add_argument("--result_dir", type=str, default="../data")
    parser.add_argument("--year", type=int, default=2018)

    args = parser.parse_args()
    get_review(data_dir=args.data_dir, result_dir=args.result_dir, year=args.year)