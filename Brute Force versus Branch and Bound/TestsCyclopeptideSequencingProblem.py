import unittest

from CyclopeptideSequencingProblem import Cyclospectrum, Linearspectrum, CyclopeptideSequencing, ConvertPeptidesToMasses


class TestCyclopeptideSequencingProblem(unittest.TestCase):

    def test_CyclopeptideSequencing(self):
        result = ConvertPeptidesToMasses(CyclopeptideSequencing('0 113 128 186 241 299 314 427'))
        self.assertEqual('113-128-186 113-186-128 128-113-186 128-186-113 186-113-128 186-128-113', result)

if __name__ == '__main__':
    unittest.main()
