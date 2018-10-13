import unittest

from PeptideEncodingProblem import FindPeptideInDNA


class TestProteinTranslationProblem(unittest.TestCase):

    def test_sample(self):
        result = FindPeptideInDNA('ATGGCCATGGCCCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA', 'MA')
        right_result = 'ATGGCC ATGGCC GGCCAT'
        self.assertEqual(right_result, result)


if __name__ == '__main__':
    unittest.main()
