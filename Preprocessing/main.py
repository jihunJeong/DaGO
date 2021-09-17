from library import *
from get_review_by_year import get_review
from get_meta_by_review import get_meta
from extract_column import save_column_data
from split_category import split_category

'''
    Amazon Electronics Data
    Preprocessing

    Version 1.1.0
'''

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_dir", type=str, default="../data")
    parser.add_argument("--result_dir", type=str, default="../data")
    parser.add_argument("--year", type=int, default=2018)

    args = parser.parse_args()

    # 기준 연도 이상 Review 저장
    get_review(args.data_dir, args.result_dir, args.year)
    
    # Review에 해당하는 상품 저장
    args.review = f"review_{args.year}.json"
    get_meta(args.result_dir, args.result_dir, args.review, args.year)

    # DB Table에 필요한 파일 저장
    save_column_data(args.result_dir, args.year)

    # Category를 Split 해 대, 중, 소분류 얻음
    args.category = f"category_{args.year}.json"
    split_category(args.result_dir, args.result_dir, args.category)
    