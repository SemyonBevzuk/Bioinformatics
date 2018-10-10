import unittest

from ReverseComplementProblem import ReverseComplement, ComplementarityRule

class TestReverseComplementProblem(unittest.TestCase):

    def test_ComplementarityRule_1(self):
        s = ReverseComplement('ACGT')
        self.assertEqual('ACGT', s)

    def test_ComplementarityRule_2(self):
        s = ReverseComplement('AaG')
        self.assertEqual('C T', s)

    def test_sample_1(self):
        s = ReverseComplement('AAAACCCGGT')
        self.assertEqual('ACCGGGTTTT', s)

if __name__ == '__main__':
    unittest.main()
