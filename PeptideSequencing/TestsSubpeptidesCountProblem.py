import unittest

from SubpeptidesCountProblem import FindNumberOfSubpeptides


class TestSubpeptidesCountProblem(unittest.TestCase):

    def test_sample(self):
        result = FindNumberOfSubpeptides(34215)
        self.assertEqual(1170632010, result)

if __name__ == '__main__':
    unittest.main()
