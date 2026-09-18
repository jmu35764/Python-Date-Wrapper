import unittest
from date_class import Date

class TestDate(unittest.TestCase):

    def test_construction(self):
        #Test if the constructor for the date class gives the desired  date
        d = Date()
        self.assertEqual(d.year, 1900)
        self.assertEqual(d.month, 1)
        self.assertEqual(d.day, 1)

    def test_date_entry(self):
        #Test if the value errors are raised when necesary
        self.assertRaises(ValueError):
            Date(1950, 13, 32)


if __name__ == '__main__':
    unittest.main()
