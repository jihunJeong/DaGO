import argparse
from get_review_by_year import get_review

'''
    Amazon Electronics Data
    Preprocessing

    Version 1.0.0
'''

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_dir", type=str, default="../data")
    parser.add_argument("--result_dir", type=str, default="../data")
    parser.add_argument("--year", type=int, default=2018)

    args = parser.parse_args()

    # 기준 연도 이상 Review 추출
    get_review(args.data_dir, args.result_dir, args.year)
    