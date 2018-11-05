import unittest

from LeaderboardCyclopeptideSequencing import LinearScore, LeaderboardCyclopeptideSequencing, ConvertPeptidesToMasses


class TestLeaderboardCyclopeptideSequencing(unittest.TestCase):

    def test_LinearScore(self):
        result = LinearScore('NQEL','0 99 113 114 128 27 257 299 355 356 370 371 484'.split())
        self.assertEqual(8, result)

    def test_LeaderboardCyclopeptideSequencing(self):
        N = 9
        Spectrum = '0 71 101 103 113 114 128 131 156 156 172 199 232 242 259 269 270 287 300 303 313 372 372 373 388 398 400 414 431 459 469 486 501 501 503 528 545 570 572 572 587 604 614 642 659 673 675 685 700 701 701 760 770 773 786 803 804 814 831 841 857 874 901 917 917 942 945 959 960 970 972 1002 1073'
        result = ConvertPeptidesToMasses(LeaderboardCyclopeptideSequencing(N, Spectrum))
        self.assertEqual('103-156-114-128-71-101-131-156-113', result)

if __name__ == '__main__':
    unittest.main()
