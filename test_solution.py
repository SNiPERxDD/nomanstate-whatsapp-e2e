import unittest

from solution import normalize_name


class NormalizeNameTest(unittest.TestCase):
    def test_normalizes_name(self):
        self.assertEqual(normalize_name("  ada   lovelace "), "Ada Lovelace")


if __name__ == "__main__":
    unittest.main()
