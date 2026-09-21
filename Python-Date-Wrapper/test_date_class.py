import unittest
from date_class import Date

class TestDate(unittest.TestCase):

    def test_default_constructor(self):
        #Test if the constructor for the date class gives the desired  date
        d = Date()
        self.assertEqual(d.year, 1900)
        self.assertEqual(d.month, 1)
        self.assertEqual(d.day, 1)

    def test_valid_constructor(self):
        #Test if the constructor for the date class gives the desired  date
        d = Date(2000, 2, 14)
        self.assertEqual(d.year, 2000)
        self.assertEqual(d.month, 2)
        self.assertEqual(d.day, 14)

        d1 = Date(2010, 2, 29)
        self.assertEqual(d1.year, 2010)
        self.assertEqual(d1.month, 2)
        self.assertEqual(d1.day, 29)

    def test_invalid_constructor(self):
        #Test if the constructor raises ValueError for invalid dates
        with self.assertRaises(ValueError):
            d = Date(2001, 13, 15)  
        with self.assertRaises(ValueError):
            d1 = Date(2001, 0, 10)  
        with self.assertRaises(ValueError):
            d2 = Date(2001, 4, 31) 
        with self.assertRaises(ValueError):
            d3 = Date(2001, 2, 29)  


    def test_invalid_day_entry(self):
        #Test if the value errors are raised when necesary
        with self.assertRaises(ValueError):
            d1 = Date(1950, 12, 32)

    def test_invalid_month_entry(self):
        #Test if the value errors are raised when necesary
        with self.assertRaises(ValueError):
            d1 = Date(1950, 13, 15)

    def test_set_date(self):
        #Test if the day property can be modified
        with self.assertRaises(ValueError): 
            d = Date(2020, 2, 29)
        d.set_date(2021, 2, 28)
        self.assertEqual(d.year, 2021)
        self.assertEqual(d.month, 2)
        self.assertEqual(d.day, 28)

    def test_invalid_set_date(self):
        #Test if the day property can be modified
        d = Date(2020, 2, 29)
        with self.assertRaises(ValueError):
            d.set_date(2021, 13, 29)
        self.assertEqual(d.year, 2021)
        self.assertEqual(d.month, 2)
        self.assertEqual(d.day, 29)

    def test_original_date_after_failed_change(self):
        #Test if the day property can be modified
        #self.assertRaises(ValueError)
        d = Date(2020, 2, 29)
        d.set_date(2021, 13, 28)
        self.assertEqual(d.year, 2020)
        self.assertEqual(d.month, 2)
        self.assertEqual(d.day, 29)

    def test_leap_year(self):
        #Test if the leap year function works
        d = Date(2020, 2, 29)
        self.assertTrue(d.is_leap_year())
        d.set_date(2021, 2, 28)
        self.assertFalse(d.is_leap_year())

    def test_static_leap_year(self):
        #Test if the static leap year function works
        self.assertTrue(Date.is_Year_leap(2020))
        self.assertFalse(Date.is_Year_leap(2021))

    def test_last_day(self):
     #Test if the last day function works
        d = Date(2020, 2, 14)
        self.assertEqual(d.last_day(), 29)
        d.set_date(2021, 2, 14)
        self.assertEqual(d.last_day(), 28)

    def test_static_last_day_of_month(self):
        #Test if the static last day of month function works
        self.assertEqual(Date.last_day_of_month(2020, 2), 29)
        self.assertEqual(Date.last_day_of_month(2021, 2), 28)

    def test_to_numeric_string(self) -> str:
        d = Date(2020, 2, 29)
        self.assertEqual(d.to_numeric_string(), "02/29/2020")

    def test_to_month_first_string(self) -> str:
        d = Date(2020, 2, 29)
        self.assertEqual(d.to_month_first_string(), "February 29, 2020")

    def test_to_day_first_string(self) -> str:
        d = Date(2020, 2, 29)
        self.assertEqual(d.to_day_first_string(), "29 February 2020")


if __name__ == '__main__':
    unittest.main()
