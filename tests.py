from hstest.stage_test import StageTest
from hstest.test_case import TestCase
from hstest.check_result import CheckResult

gen_answers = '''    Unnamed: 0 hospital gender  age  ...  mri  xray  children months
0            0  general    man   33  ...  NaN   NaN       NaN    NaN
1            1  general    man   48  ...  NaN   NaN       NaN    NaN
2            2  general  woman   23  ...  NaN   NaN       NaN    NaN
3            3  general    man   27  ...  NaN   NaN       NaN    NaN
4            4  general  woman   22  ...  NaN     f       NaN    NaN
5            5  general    man   46  ...  NaN   NaN       NaN    NaN
6            6  general  woman   68  ...  NaN   NaN       NaN    NaN
7            7  general    man   35  ...  NaN   NaN       NaN    NaN
8            8  general  woman   50  ...  NaN     f       NaN    NaN
9            9  general    man   25  ...  NaN   NaN       NaN    NaN
10          10  general    man   27  ...  NaN   NaN       NaN    NaN
11          11  general    man   57  ...  NaN   NaN       NaN    NaN
12          12  general    man   29  ...  NaN     f       NaN    NaN
13          13  general  woman   18  ...  NaN   NaN       NaN    NaN
14          14  general  woman   47  ...  NaN   NaN       NaN    NaN
15          15  general  woman   51  ...  NaN   NaN       NaN    NaN
16          16  general  woman   56  ...  NaN     t       NaN    NaN
17          17  general  woman   38  ...  NaN   NaN       NaN    NaN
18          18  general  woman   32  ...  NaN   NaN       NaN    NaN
19          19  general  woman   69  ...  NaN     f       NaN    NaN

[20 rows x 15 columns]'''

pren_answers = '''    Unnamed: 0  HOSPITAL  Sex   age  ...  mri  xray  children months
0            0  prenatal  NaN  27.0  ...  NaN     f       0.0    3.0
1            1  prenatal  NaN  18.0  ...  NaN     f       1.0    5.0
2            2  prenatal  NaN  34.0  ...  NaN     f       1.0    5.0
3            3  prenatal  NaN  29.0  ...  NaN     f       2.0    3.0
4            4  prenatal  NaN  33.0  ...  NaN     f       1.0    7.0
5            5  prenatal  NaN  31.0  ...  NaN     f       0.0    3.0
6            6  prenatal  NaN  30.0  ...  NaN     f       0.0    5.0
7            7  prenatal  NaN  19.0  ...  NaN     f       1.0    6.0
8            8  prenatal  NaN  44.0  ...  NaN     f       2.0    6.0
9            9  prenatal  NaN  35.0  ...  NaN     f       0.0    6.0
10          10  prenatal  NaN  41.0  ...  NaN     f       2.0    7.0
11          11  prenatal  NaN  26.0  ...  NaN     f       0.0    7.0
12          12  prenatal  NaN  25.0  ...  NaN     f       1.0    5.0
13          13  prenatal  NaN  41.0  ...  NaN     f       2.0    8.0
14          14  prenatal  NaN  27.0  ...  NaN     f       0.0    6.0
15          15  prenatal  NaN  26.0  ...  NaN     f       2.0    2.0
16          16  prenatal  NaN  16.0  ...  NaN     f       1.0    4.0
17          17  prenatal  NaN  33.0  ...  NaN     f       1.0    9.0
18          18  prenatal  NaN  35.0  ...  NaN     f       1.0    8.0
19          19  prenatal  NaN  30.0  ...  NaN     f       2.0    9.0

[20 rows x 15 columns]'''

sports_answers = '''    Unnamed: 0 Hospital Male/female   age  ...  mri  xray  children months
0            0   sports      female  20.0  ...    t     f       NaN    NaN
1            1   sports      female  20.0  ...    f     t       NaN    NaN
2            2   sports        male  16.0  ...    f     t       NaN    NaN
3            3   sports        male  17.0  ...    t     f       NaN    NaN
4            4   sports        male  19.0  ...    f     t       NaN    NaN
5            5      NaN         NaN   NaN  ...  NaN   NaN       NaN    NaN
6            6   sports      female  14.0  ...    t     f       NaN    NaN
7            7   sports      female  22.0  ...    t     f       NaN    NaN
8            8   sports      female  21.0  ...    f     t       NaN    NaN
9            9   sports      female  18.0  ...    t     f       NaN    NaN
10          10   sports        male  12.0  ...    f     t       NaN    NaN
11          11   sports        male  15.0  ...    f     t       NaN    NaN
12          12   sports      female  22.0  ...    f     f       NaN    NaN
13          13   sports      female  19.0  ...    f     t       NaN    NaN
14          14   sports      female  16.0  ...    f     t       NaN    NaN
15          15   sports      female  19.0  ...    f     t       NaN    NaN
16          16   sports        male  18.0  ...    f     t       NaN    NaN
17          17   sports      female  18.0  ...    t     f       NaN    NaN
18          18   sports        male  19.0  ...    f     t       NaN    NaN
19          19   sports      female  17.0  ...    t     f       NaN    NaN

[20 rows x 15 columns]
'''


class EDATest(StageTest):
    def generate(self):
        return [TestCase()]

    def check(self, reply, attach):
        lines = reply.split('\n')
        lines_with_digit = [i for i in lines if len(i) > 0 and i[0].isdigit()]
        if len(lines_with_digit) != 60:
            return CheckResult.wrong(
                'There should be 60 lines of data, found ' + str(len(lines_with_digit)))

        if gen_answers not in reply:
            return CheckResult.wrong(
                "Seems like you didn't print first 20 rows of general.csv")

        if pren_answers not in reply:
            return CheckResult.wrong(
                "Seems like you didn't print first 20 rows of prenatal.csv")

        if sports_answers not in reply:
            return CheckResult.wrong(
                "Seems like you didn't print first 20 rows of sports.csv")

        return CheckResult.correct()


if __name__ == '__main__':
    EDATest('analysis').run_tests()
