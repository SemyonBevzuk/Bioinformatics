import unittest

from GeneratingTheoreticalSpectrumProblem import Cyclospectrum


class TestGeneratingTheoreticalSpectrumProblem(unittest.TestCase):

    def test_sample(self):
        result = Cyclospectrum('LEQN')
        right_result = '0 113 114 128 129 227 242 242 257 355 356 370 371 484'
        self.assertEqual(right_result, result)

    def test_1(self):
        result = Cyclospectrum('')
        right_result = '0 0'
        self.assertEqual(right_result, result)

    def test_2(self):
        result = Cyclospectrum('p')
        right_result = '0 0'
        self.assertEqual(right_result, result)

if __name__ == '__main__':
    unittest.main()
