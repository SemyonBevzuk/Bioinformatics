import unittest

from ImplementMotifEnumeration import MotifEnumeration, HammingDistance

class Test(unittest.TestCase):

    def test_HammingDistance_1(self):
        res = HammingDistance('AAAA', 'AAAA')
        self.assertEqual(0, res)

    def test_HammingDistance_2(self):
        res = HammingDistance('AAAA', 'ABCD')
        self.assertEqual(3, res)

    def test_HammingDistance_3(self):
        res = HammingDistance('ABCD', 'DCBA')
        self.assertEqual(4, res)

    def test_MotifEnumeration_1(self):
        k = 4
        d = 1
        dna = [ 'CACTGATCGACTTATC',
                'CTCCGACTTACCCCAC',
                'GTCTATCCCTGATGGC',
                'CAGGGTTGTCTTGTCT']
        res = MotifEnumeration(dna, k, d)
        correct_res = 'CAGA CCTT CTCT CTTA CTTG CTTT GACT GATT GCCT GGCT GTCT TATC TCTG TCTT TGAC TTAT TTTC'
        self.assertEqual(correct_res, res)

if __name__ == '__main__':
    unittest.main()