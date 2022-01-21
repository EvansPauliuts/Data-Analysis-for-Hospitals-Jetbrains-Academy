from hstest.stage_test import StageTest
from hstest.test_case import TestCase
from hstest.check_result import CheckResult

answers = ['general', '0.325', '0.285', '19', ('prenatal', '325')]


class EDATest(StageTest):
    def generate(self):
        return [TestCase()]

    def check(self, reply, attach):
        lines = [line for line in reply.split('\n') if len(line) > 0]

        if len(lines) !=5:
            return CheckResult.wrong(
                'You should output exactly 5 lines with answer to each question in each line. '
                f'Found {len(lines)} lines')

        if answers[0] not in lines[0].lower():
            return CheckResult.wrong('The answer to the 1st question is incorrect')

        if answers[1] not in lines[1]:
            return CheckResult.wrong('The answer to the 2nd question is incorrect')

        if answers[2] not in lines[2]:
            return CheckResult.wrong('The answer to the 3rd question is incorrect')

        if answers[3] not in lines[3]:
            return CheckResult.wrong('The answer to the 4th question is incorrect')

        if answers[4][0] not in lines[4].lower():
            return CheckResult.wrong('The name of the hospital in the answer to the 5th is incorrect')
        if answers[4][1] not in lines[4].lower():
            return CheckResult.wrong('The number of blood tests in the answer to the 5th is incorrect')

        return CheckResult.correct()


if __name__ == '__main__':
    EDATest('analysis').run_tests()
