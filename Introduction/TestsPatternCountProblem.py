import unittest

from PatternCountProblem import PatternCount


class TestPatternСountProblem(unittest.TestCase):

    def test_search_string_in_string(self):
        count = PatternCount('abc', 'abc')
        self.assertEqual(1, count)

    def test_search_missing_substring(self):
        count = PatternCount('a', 'bbb')
        self.assertEqual(0, count)

    def test_search_intersecting_substring(self):
        count = PatternCount('aba', 'ababa')
        self.assertEqual(2, count)

    def test_search_sample_1(self):
        count = PatternCount('ATAT', 'GATATATGCATATACTT')
        self.assertEqual(3, count)

    def test_search_sample_2(self):
        count = PatternCount('ATAT', 'GATATGCATATACTT')
        self.assertEqual(2, count)

    def test_search_intersecting_substring(self):
        count = PatternCount('aba', 'ababa')
        self.assertEqual(2, count)

    def test_search_substring_more_string(self):
        count = PatternCount('aba', 'ab')
        self.assertEqual(0, count)


if __name__ == '__main__':
    unittest.main()
