import unittest
from utils import utils

class utils_tests(unittest.TestCase):

    def test_reversed(self):
        self.assertEqual(utils.reversed(1453), 3541)
        self.assertEqual(utils.reversed(-1453), -3541)
        self.assertIsNone(utils.reversed("abc"))
        self.assertIsNone(utils.reversed("1453"))
        self.assertIsNone(utils.reversed(1453.0))

    def test_formatter(self):
        self.assertEqual(utils.formatter(1453), ("0b10110101101","0o2655"))
        self.assertIsNone(utils.formatter("abc"))
        self.assertIsNone(utils.formatter("123"))
        self.assertIsNone(utils.formatter(1453.0))

if __name__ == '__main__':
    unittest.main()