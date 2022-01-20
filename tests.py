import re

from hstest.stage_test import StageTest
from hstest.test_case import TestCase
from hstest.check_result import CheckResult

df_result_float_zero = '''     hospital gender   age  height  ...  mri  xray children months
929    sports      f  23.0   6.809  ...    t     f      0.0    0.0
927    sports      m  21.0   6.052  ...    t     f      0.0    0.0
516  prenatal      f  20.0   1.650  ...    0     f      1.0    4.0
87    general      m  54.0   1.720  ...    0     0      0.0    0.0
885    sports      f  16.0   5.915  ...    t     f      0.0    0.0
463  prenatal      f  34.0   1.650  ...    0     f      1.0    5.0
112   general      m  77.0   1.690  ...    0     0      0.0    0.0
297   general      m  56.0   1.480  ...    0     0      0.0    0.0
417   general      f  26.0   1.650  ...    0     0      0.0    0.0
660  prenatal      f  38.0   1.590  ...    0     f      1.0    4.0
344   general      f  60.0   1.410  ...    0     0      0.0    0.0
834    sports      f  21.0   5.585  ...    f     t      0.0    0.0
10    general      m  27.0   1.850  ...    0     0      0.0    0.0
56    general      m  23.0   1.650  ...    0     0      0.0    0.0
616  prenatal      f  33.0   1.770  ...    0     f      1.0    7.0
479  prenatal      f  35.0   1.810  ...    0     f      1.0    8.0
578  prenatal      f  31.0   1.770  ...    0     f      1.0    8.0
411   general      m  26.0   1.610  ...    0     0      0.0    0.0
521  prenatal      f  30.0   1.740  ...    0     f      1.0    3.0
941    sports      f  25.0   6.208  ...    f     t      0.0    0.0

[20 rows x 14 columns]'''

df_result_int_zero = '''     hospital gender   age  height  ...  mri  xray children months
929    sports      f  23.0   6.809  ...    t     f        0      0
927    sports      m  21.0   6.052  ...    t     f        0      0
516  prenatal      f  20.0   1.650  ...    0     f      1.0    4.0
87    general      m  54.0   1.720  ...    0     0        0      0
885    sports      f  16.0   5.915  ...    t     f        0      0
463  prenatal      f  34.0   1.650  ...    0     f      1.0    5.0
112   general      m  77.0   1.690  ...    0     0        0      0
297   general      m  56.0   1.480  ...    0     0        0      0
417   general      f  26.0   1.650  ...    0     0        0      0
660  prenatal      f  38.0   1.590  ...    0     f      1.0    4.0
344   general      f  60.0   1.410  ...    0     0        0      0
834    sports      f  21.0   5.585  ...    f     t        0      0
10    general      m  27.0   1.850  ...    0     0        0      0
56    general      m  23.0   1.650  ...    0     0        0      0
616  prenatal      f  33.0   1.770  ...    0     f      1.0    7.0
479  prenatal      f  35.0   1.810  ...    0     f      1.0    8.0
578  prenatal      f  31.0   1.770  ...    0     f      1.0    8.0
411   general      m  26.0   1.610  ...    0     0        0      0
521  prenatal      f  30.0   1.740  ...    0     f      1.0    3.0
941    sports      f  25.0   6.208  ...    f     t        0      0

[20 rows x 14 columns]'''


class EDATest(StageTest):
    def generate(self):
        return [TestCase()]

    def check(self, reply, attach):
        lines = reply.split('\n')
        if len(lines) < 24:
            return CheckResult.wrong(feedback="There is not enough lines in the answer, check the example output at the stage 3")

        # check random 20 rows printing
        lines_with_digit_first = [i for i in lines if len(i) > 0 and i[0].isdigit()]
        columns = lines[1]
        if 'Unnamed: 0' in columns:
            return CheckResult.wrong(feedback='Holy-moly! you\'ve printed \'Unnamed: 0\' column')
        if len(lines_with_digit_first) != 20:
            return CheckResult.wrong(feedback='There should be 20 lines of data, found ' + str(len(lines_with_digit_first)))

        row_indexes_in_reply = [int(re.findall(r'\d+', x.split(' ')[0])[0]) for x in lines_with_digit_first]
        right_row_indexes = [929, 927, 516, 87, 885, 463, 112, 297, 417, 660, 344, 834, 10, 56, 616, 479, 578, 411, 521, 941]
        if set(row_indexes_in_reply) != set(right_row_indexes):
            return CheckResult.wrong(feedback=f"You've printed a wrong sample of data\nFound indexes: {row_indexes_in_reply},\nExpected indexes: {right_row_indexes}\n"
                                              f"Make sure that you set random_state=30 and completed all the steps in the Objectives section including deleting empty rows")
        if df_result_float_zero not in reply and df_result_int_zero not in reply:
            return CheckResult.wrong(feedback="Seems like your answer is incorrect. Make sure that you completed all the steps in the Objectives section")

        # check data shape reply
        data_shape_reply = list(map(float, re.findall(r'\d*\.\d+|\d+', lines[0])))
        if len(data_shape_reply) != 2:
            return CheckResult.wrong(feedback="The shape of the data should consist of 2 numbers")
        if data_shape_reply[0] != 1000:
            return CheckResult.wrong(feedback=f"{data_shape_reply[0]} is a wrong number of rows in the data frame. Make sure that you deleted empty rows and completed all the steps in the Objectives section")
        if data_shape_reply[1] != 14:
            return CheckResult.wrong(feedback=f"{data_shape_reply[1]} is a wrong number of columns in the data frame. Make sure that you completed all the steps in the Objectives section")

        return CheckResult.correct()


if __name__ == '__main__':
    EDATest('analysis').run_tests()
