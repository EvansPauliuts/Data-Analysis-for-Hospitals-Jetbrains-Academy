# write your code here
import glob
import pandas as pd


class AnalysisHospitals:
    def __init__(self):
        pass

    @staticmethod
    def data_all_csv():
        dataframes_list = [v for v in map(pd.read_csv, glob.glob('test/*.csv'))]
        dataframes_list[1].rename(columns={'HOSPITAL': 'hospital', 'Sex': 'gender'}, inplace=True)
        dataframes_list[2].rename(columns={'Hospital': 'hospital', 'Male/female': 'gender'}, inplace=True)

        df = pd.concat(dataframes_list, ignore_index=True)
        df.drop(columns=['Unnamed: 0'], inplace=True)

        print(df.sample(n=20, random_state=30))


def main():
    AnalysisHospitals.data_all_csv()


if __name__ == '__main__':
    main()
