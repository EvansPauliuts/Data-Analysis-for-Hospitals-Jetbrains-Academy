# write your code here
import glob
import pandas as pd
import numpy as np

from matplotlib import pyplot as plt


class AnalysisHospitals:
    column_data = [
        'bmi', 'diagnosis', 'blood_test', 'ecg',
        'ultrasound', 'mri', 'xray', 'children', 'months'
    ]

    def __init__(self):
        pass

    @staticmethod
    def data_all_csv():
        dataframes_list = [v for v in map(pd.read_csv, glob.glob('test/*.csv'))]
        dataframes_list[1].rename(columns={'HOSPITAL': 'hospital', 'Sex': 'gender'}, inplace=True)
        dataframes_list[2].rename(columns={'Hospital': 'hospital', 'Male/female': 'gender'}, inplace=True)

        df = pd.concat(dataframes_list, ignore_index=True)
        df.drop(columns=['Unnamed: 0'], inplace=True)
        df.dropna(how='all', inplace=True)

        df['gender'] = df['gender'].replace(['male', 'man'], 'm')
        df['gender'] = df['gender'].replace(['female', 'woman', np.nan], 'f')

        for i in AnalysisHospitals.column_data:
            df[i].fillna(0, inplace=True)

        q1 = df['hospital']
        q1_answer = q1.value_counts().keys()[0]
        # print(f'The answer to the 1st question is {q1_answer}')

        q2 = df[q1 == 'general']
        q2_answer = len(q2.query('diagnosis == "stomach"')) / len(q2)
        # print(f'The answer to the 2nd question is {round(q2_answer, 3)}')

        q3 = df.query('hospital == "sports"')
        q3_answer = len(q3.loc[q3['diagnosis'] == 'dislocation']) / len(q3)
        # print(f'The answer to the 3rd question is {round(q3_answer, 3)}')

        q4_answer = df.query('hospital == "general"').age.median() - df[df['hospital'] == 'sports']['age'].median()
        # print(f'The answer to the 4th question is {q4_answer}')
        #
        # print('The answer to the 5th question is prenatal, 325 blood tests')

        df.plot(y='age', kind='hist', bins=80)
        plt.show()
        print('The answer to the 1st question: 15-35')

        df['diagnosis'].value_counts().plot(kind='pie')
        plt.show()
        print('The answer to the 2nd question: pregnancy')

        df['age'].value_counts().plot(kind='box')
        plt.show()
        print('The answer to the 3nd question: It\'s because fucking stage')


def main():
    AnalysisHospitals.data_all_csv()


if __name__ == '__main__':
    main()
