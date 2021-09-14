from library import *
from preprocessing_data import *

def get_meta(data_dir, result_dir, review, year=2018):
    '''
        Args:
            data_dir : review data가 있는 경로
            result_dir : 얻은 review data를 저장할 경로
            review : Review 목록
            year : 선택한 연도 
        
        Note:
            meta_Electronics.json에서 review 파일에 있는 상품 얻은 후
            데이터 결측값, Noise 정제 후 meta 파일 얻음

        Save Columns: 
            Asin : ID of the product
            Title : Name of the product
            Feature : bullet-point format features of the product
            description : description of the product
            price : price in US dollars
            imageURL : url of the product image
            imageHighRes : High resolution product image
            brand : brand name
            categories : list of categories the product belongs to
    '''

    print("Processing Meta ...", flush=True)
    meta_reader = pd.read_json(data_dir+"/meta_Electronics.json", lines=True, chunksize=1000)
    review = pd.read_json(data_dir+f"/{review}.json")
    
    meta_df = pd.DataFrame()
    cnt = 0
    print("Origin Count 786645")
    for idx, meta in enumerate(tqdm(meta_reader, desc="Get Meta")):
        select = meta[meta["asin"].apply(lambda x: (review["asin"] == x).any())] # Review에 맞는 Meta Product 추출
        select = select.drop(columns=['fit', 'similar_item','tech1','tech2','rank','details','main_cat']).copy() # Useless Column drop
        
        for i, row in select.iterrows():
            select.at[i] = change_html_expression(row) # Data 안에 Html Expression 변환
            select.at[i] = empty2null(row) # 빈 Data Null 처리
            select.at[i, 'edate'] = change_date_format(row['date'])

            if "by" in str(row['brand']): # Noise Data Preprocessing
                select.at[i, 'brand'] = None
    
            if not row['price'].replace(".", "1").replace("$", "").isdigit(): #Noise Data Preprocessing
                select.at[i, 'price'] = None
            else :
                select.at[i, 'price'] = row['price'].replace("$", "")
        
        select.drop(columns=['date'], inplace=True)    
        pre_df = pd.concat([pre_df, select])
        if (idx+1)%40 == 0:
            pre_df.dropna(inplace=True)
            cnt += len(pre_df)
            pre_df.to_json(result_dir+f"/meta_{year}_{(idx+1)}.json", orient='records', lines=True)
            pre_df = pd.DataFrame()
    pre_df.dropna(inplace=True)
    cnt += len(pre_df)
    print(f"Total count : {cnt}")
    pre_df.to_json(result_dir+f"/meta_{year}_last.json", orient='records', lines=True)

    merge_file(result_dir, result_dir, f"meta_{year}") # Split 된 파일 합쳐 최종 결과
    print("Done")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_dir", type=str, default="../data")
    parser.add_argument("--result_dir", type=str, default="../data")
    parser.add_argument("--review_file", type=str, default="review_2018")

    args = parser.parse_args()
    get_meta(args.data_dir, args.result_dir, args.review_file)