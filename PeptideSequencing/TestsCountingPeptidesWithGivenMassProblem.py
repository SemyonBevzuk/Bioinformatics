import unittest

from CountingPeptidesWithGivenMassProblem import NumberPeptidesWithGivenMass


class TestCountingPeptidesWithGivenMassProblem(unittest.TestCase):

    def test_sample(self):
        result = NumberPeptidesWithGivenMass(1024)
        right_result = 14712706211
        self.assertEqual(right_result, result)

    def test_1(self):
        result = NumberPeptidesWithGivenMass(57)
        right_result = 1
        self.assertEqual(right_result, result)

    def test_2(self):
        result = NumberPeptidesWithGivenMass(3)
        right_result = 0
        self.assertEqual(right_result, result)

    def test_3(self):
        result = NumberPeptidesWithGivenMass(102)
        right_result = 0
        self.assertEqual(right_result, result)

    def test_4(self):
        result = NumberPeptidesWithGivenMass(58)
        right_result = 0
        self.assertEqual(right_result, result)

    def test_5(self):
        result = NumberPeptidesWithGivenMass(200)
        right_result = 8
        self.assertEqual(right_result, result)

if __name__ == '__main__':
    unittest.main()
