import unittest

from CyclopeptideScoringProblem import Score


class TestCyclopeptideScoringProblem(unittest.TestCase):

    def test_Score_1(self):
        result = Score('NQEL', '0 99 113 114 128 227 257 299 355 356 370 371 484')
        self.assertEqual(11, result)

    def test_Score_2(self):
        result = Score('NQEL', '0')
        self.assertEqual(1, result)

    def test_Score_3(self):
        result = Score('II', '0 113 226')
        self.assertEqual(3, result)

    def test_Score_4(self):
        result = Score('II', '0 113 113 113 226')
        self.assertEqual(4, result)

if __name__ == '__main__':
    unittest.main()
