import re

from hstest.stage_test import StageTest
from hstest.test_case import TestCase
from hstest.check_result import CheckResult

df_result = '''     hospital  gender   age  height  ...  mri  xray children months
928    sports    male  22.0   5.961  ...    t     f      NaN    NaN
926    sports    male  26.0   5.804  ...    t     f      NaN    NaN
901    sports  female  23.0   5.894  ...    t     f      NaN    NaN
87    general     man  54.0   1.720  ...  NaN   NaN      NaN    NaN
884    sports  female  20.0   6.771  ...    t     f      NaN    NaN
297   general     man  56.0   1.480  ...  NaN   NaN      NaN    NaN
112   general     man  77.0   1.690  ...  NaN   NaN      NaN    NaN
209   general     man  29.0   2.080  ...  NaN   NaN      NaN    NaN
419   general     man  53.0   1.700  ...  NaN   NaN      NaN    NaN
913    sports  female  22.0   6.435  ...    t     f      NaN    NaN
820    sports  female  17.0   5.722  ...    f     t      NaN    NaN
861       NaN     NaN   NaN     NaN  ...  NaN   NaN      NaN    NaN
10    general     man  27.0   1.850  ...  NaN   NaN      NaN    NaN
56    general     man  23.0   1.650  ...  NaN   NaN      NaN    NaN
618  prenatal     NaN  30.0   1.490  ...  NaN     f      0.0    2.0
978    sports    male  17.0   5.647  ...    f     f      NaN    NaN
373   general   woman  44.0   1.660  ...  NaN   NaN      NaN    NaN
628  prenatal     NaN  24.0   1.610  ...  NaN     f      0.0    2.0
858    sports    male  19.0   7.089  ...    f     t      NaN    NaN
944    sports  female  21.0   6.217  ...    f     t      NaN    NaN

[20 rows x 14 columns]
'''


class EDATest(StageTest):
    def generate(self):
        return [TestCase()]

    def check(self, reply, attach):
        lines = reply.split('\n')
        lines_with_digit_first = [i for i in lines if len(i) > 0 and i[0].isdigit()]
        columns = lines[0].split(' ')
        if 'Unnamed: 0' in columns:
            return CheckResult.wrong(
                'Holy-moly! you\'ve printed \'Unnamed: 0\' column')

        if len(lines_with_digit_first) != 20:
            return CheckResult.wrong(
                'There should be 20 lines of data, found ' + str(len(lines_with_digit_first)))

        row_indexes_in_reply = [int(re.findall(r'\d+', x.split(' ')[0])[0]) for x in lines_with_digit_first]
        right_row_indexes = [928, 926, 901, 87, 884, 297, 112, 209, 419, 913, 820, 861, 10, 56, 618, 978, 373, 628, 858, 944]
        if set(row_indexes_in_reply) != set(right_row_indexes):
            return CheckResult.wrong(
                feedback=f"You've printed a wrong sample of data\nFound indexes: {row_indexes_in_reply},\nExpected indexes: {right_row_indexes}\nMake sure that you set random_state=30")

        if df_result not in reply:
            return CheckResult.wrong(
                "Seems like your answer is incorrect")

        return CheckResult.correct()


if __name__ == '__main__':
    EDATest('analysis').run_tests()
