import unittest

from ImplementMedianString import FindPatternFromNumber, DistancePatternText, MedianString

class Test(unittest.TestCase):

    def test_FindPatternFromNumber_1(self):
        res = FindPatternFromNumber(0, 1)
        self.assertEqual('A', res)

    def test_FindPatternFromNumber_2(self):
        res = FindPatternFromNumber(6, 2)
        self.assertEqual('GC', res)

    def test_DistancePatternText_1(self):
        res = DistancePatternText('GATTCTCA', ['GCAAAGACGCTGACCAA'])
        self.assertEqual(3, res)

    def test_MedianString_1(self):
        dna = ['GAAACTACGCACGTAGTGTTTTGCTACGGTTCTCA',
               'TATATCCACATGACCTCGACAACGCACGGTCGAAT',
               'TAGCGGGACAATCAGGTCTGAGTCGACTGTTGTGC',
               'TCCTGCCGGTTGCTAACTGTAGACGTTTACCCCTT',
               'TCCCTCCCTAACTCTAGGCTACTGTCGTCCGCAGT',
               'AGGCAGAAAGACAACGGTAGTAATCTAGAGACCGT',
               'CGCTCCACGCAGCTCATAGAACCGTGTTGTTCAAC',
               'ACTGTCTCCCGGAAACCATAAACTACTTGGTTTGT',
               'GGTTTTCTTGACTGTAATTACAATCCAGGAGACCA',
               'ATGTCGCTCTACAGTGAACACGTAACTGTCTTCGG']
        k = 5
        res = MedianString(dna, k)
        self.assertEqual('ACTGT', res)

if __name__ == '__main__':
    unittest.main()