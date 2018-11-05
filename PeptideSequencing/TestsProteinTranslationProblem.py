import unittest

from ProteinTranslationProblem import TranslateRNAIntoAminoAcid


class TestProteinTranslationProblem(unittest.TestCase):

    def test_1(self):
        result = TranslateRNAIntoAminoAcid('AUG')
        self.assertEqual('M', result)

    def test_2(self):
        result = TranslateRNAIntoAminoAcid('AAAUGAAAA')
        self.assertEqual('KK', result)

    def test_sample(self):
        result = TranslateRNAIntoAminoAcid('AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA')
        self.assertEqual('MAMAPRTEINSTRING', result)


if __name__ == '__main__':
    unittest.main()
