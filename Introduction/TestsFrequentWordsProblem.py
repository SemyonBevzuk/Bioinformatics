import unittest

from FrequentWordsProblem import FrequentWords


class TestFrequentWordsProblem(unittest.TestCase):

    def test_sample(self):
        result = FrequentWords('ACGTTGCATGTCGCATGATGCATGAGAGCT', 4)
        right_result = 'CATG GCAT'
        self.assertEqual(right_result, result)


if __name__ == '__main__':
    unittest.main()
