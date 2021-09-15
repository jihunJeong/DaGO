from library import *

def extract_column_data(data_dir, result_dir, filename, column):
    '''
        Args:
            data_dir: 추출할 원본 데이터가 있는 경로
            result_dir: 추출 된 데이터를 저장할 경로
            filename: 추출할 원본 데이터 이름
            column: 추출할 Column name

        Note:
            원본 데이터에서 Column만 추출해 중복을 제거한 뒤 저장
    '''

    print(f"Extract {column} column ... ", end="")
    pre_df = pd.DataFrame(columns=[column])
    jsonObject = pd.read_json(data_dir+f"/{filename}.json", lines=True, chunksize=1000)

    for idx, obj in enumerate(jsonObject):
        select = obj[[column]]
        pre_df = pd.concat([pre_df, select])
        pd.DataFrame(pre_df, columns=pre_df.columns)

    pre_df.drop_duplicates(inplace=True)
    pre_df.index = np.arange(1, len(pre_df)+1)
    pre_df.to_json(result_dir+f"/{column}_{filename}.json", orient="records", lines=True)
    print("Done")

def save_column_data(data_dir, year):
    '''
        Args:
            data_dir: 전처리에서 User가 설정한 저장 경로
            year: User가 얻고자 설정한 연도

        Note:
            Data 전처리에서 DB Table에 필요한 Category와 Brand 파일 저장
    '''

    print("Progress Save Column File")
    extract_column_data(data_dir, data_dir, f"meta_{year}", "category")
    extract_column_data(data_dir, data_dir, f"meta_{year}", "brand")
    print("Done")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_dir", type=str, default="../data")
    parser.add_argument("--result_dir", type=str, default="../data")
    parser.add_argument("--filename", type=str)
    parser.add_argument("--column", type=str)

    args = parser.parse_args()
    extract_column_data(data_dir=args.data_dir, result_dir=args.result_dir, filename=args.filename, column=args.column)