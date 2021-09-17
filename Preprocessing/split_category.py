from library import *

def split_category(data_dir, result_dir, filename):
    '''
        Args:
            data_dir : 기존 category가 있는 경로
            result_dir : Split된 결과가 저장될 경로
            filename : Category File Name
        
        Note:
            Category File에서 대분류, 중분류, 소분류로 카테고리를 나눠 각각 파일로 저장
            이후 DB Table에 사용
    '''
    categories = pd.read_json(data_dir+f"/{filename}.json", lines=True, chunksize=1000)

    big = dict() # Big Category Info 저장 Dictionary
    mid = dict() # Middle Category Info 저장 Dictionary

    big_index, mid_index = 1, 1

    big_df = pd.DataFrame(columns=['name'])
    mid_df = pd.DataFrame(columns=['name', 'cb_id'])
    sm_df = pd.DataFrame(columns=['name', 'cm_id', 'cb_id'])

    for idx, category in enumerate(categories):
        for idx, row in category.iterrows():
            big_df = big_df.append(pd.Series(row['category'][1], index=big_df.columns), ignore_index=True)
            big_df.drop_duplicates(inplace=True)

            if row['category'][1] not in big.keys():
                big[row['category'][1]] = big_index
                big_index += 1

            if len(row['category']) <= 2:
                mid_df = mid_df.append(pd.Series(['Extra',  int(big[row['category'][1]])], index=mid_df.columns), ignore_index=True)
            else :
                mid_df = mid_df.append(pd.Series([row['category'][2], int(big[row['category'][1]])], index=mid_df.columns), ignore_index=True)
                if row['category'][2] not in mid.keys():
                    mid[row['category'][2]] = mid_index
                    mid_index += 1
            mid_df.drop_duplicates(inplace=True)

    
            if len(row['category']) <= 2 or row['category'][2] not in mid.keys():
                continue
            elif len(row['category']) <= 3:
                sm_df = sm_df.append(pd.Series(['Extra', int(mid[row['category'][2]]), int(big[row['category'][1]])], index=sm_df.columns), ignore_index=True)
            else :
                sm_df = sm_df.append(pd.Series([row['category'][3], int(mid[row['category'][2]]), int(big[row['category'][1]])], index=sm_df.columns), ignore_index=True)
            sm_df.drop_duplicates(inplace=True)
    
    # 각 Dataframe Index 1부터 Assign
    big_df.index = np.arange(1, len(big_df)+1)
    mid_df.index = np.arange(1, len(mid_df)+1)
    sm_df.index = np.arange(1, len(sm_df)+1)

    # 각 Category 저장
    big_df.to_csv(result_dir+f"/big_{filename}.csv")
    mid_df.to_csv(result_dir+f"/mid_{filename}.csv")
    sm_df.to_csv(result_dir+f"/sm_{filename}.csv")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_dir", type=str, default="../data")
    parser.add_argument("--result_dir", type=str, default="../data")
    parser.add_argument("--filename", type=str, default="category_2018")

    args = parser.parse_args()
    split_category(data_dir=args.data_dir, result_dir=args.result_dir, filename=args.filename)
