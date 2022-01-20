# write your code here
import glob
import pandas as pd
import numpy as np


class AnalysisHospitals:
    column_data = [
        'bmi', 'diagnosis', 'blood_test', 'ecg',
        'ultrasound', 'mri', 'xray', 'children', 'months'
    ]

    def __init__(self):
        pass

    @staticmethod
    def data_all_csv():
        dataframes_list = [v for v in map(pd.read_csv, glob.glob('tests/*.csv'))]
        dataframes_list[1].rename(columns={'HOSPITAL': 'hospital', 'Sex': 'gender'}, inplace=True)
        dataframes_list[2].rename(columns={'Hospital': 'hospital', 'Male/female': 'gender'}, inplace=True)

        df = pd.concat(dataframes_list, ignore_index=True)
        df.drop(columns=['Unnamed: 0'], inplace=True)
        df.dropna(how='all', inplace=True)

        df['gender'] = df['gender'].replace(['male', 'man'], 'm')
        df['gender'] = df['gender'].replace(['female', 'woman', np.nan], 'f')

        for i in AnalysisHospitals.column_data:
            df[i].fillna(0, inplace=True)

        print(f'Data shape: {df.shape}')
        print(df.sample(n=20, random_state=30))


def main():
    AnalysisHospitals.data_all_csv()


if __name__ == '__main__':
    main()
