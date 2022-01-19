# write your code here
import pandas as pd


class AnalysisHospitals:
    def __init__(self):
        pass

    @staticmethod
    def data_all_csv(file_csv):
        generals = pd.read_csv(file_csv)
        print(generals.head(20))


def main():
    csv_file_list = ['test/general.csv', 'test/prenatal.csv', 'test/sports.csv']
    for v in csv_file_list:
        AnalysisHospitals.data_all_csv(v)


if __name__ == '__main__':
    main()
