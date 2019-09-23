import unittest
from src.median import median
from src.data_frame import data_frame


class unit_test(unittest.TestCase):
    def test_median(self):
        sample1 = [1, 5, 2, 7, 9, -23]
        self.assertEqual(median(sample1), 3.5)
        sample2 = [7, -3, 4, 2, 1]
        self.assertEqual(median(sample2), 2)

    def test_data_frame(self):
        self.assertEqual(data_frame("data/test_set1.csv"), 12)
        self.assertEqual(data_frame("data/test_set2.csv"), None)


if __name__ == "__main__":
    unittest.main()
