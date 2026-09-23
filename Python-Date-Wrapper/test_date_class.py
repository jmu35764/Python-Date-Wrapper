import unittest
from date_class import Date

class TestDate(unittest.TestCase):

    def test_default_constructor(self):
        #Test if the constructor for the date class gives the default date of 1/1/1900
        d = Date()
        self.assertEqual(d.year, 1900)
        self.assertEqual(d.month, 1)
        self.assertEqual(d.day, 1)

    def test_valid_constructor(self):
        #Test if the constructor for the date class gives the desired entered date
        d = Date(2000, 2, 14)
        self.assertEqual(d.year, 2000)
        self.assertEqual(d.month, 2)
        self.assertEqual(d.day, 14)

        d1 = Date(2010, 2, 28)
        self.assertEqual(d1.year, 2010)
        self.assertEqual(d1.month, 2)
        self.assertEqual(d1.day, 28)

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

    def test_set_date(self):
        #Test if the set_date method can modify the date properties
        d = Date(2020, 2, 29)
        d.set_date(2021, 2, 28)
        self.assertEqual(d.year, 2021)
        self.assertEqual(d.month, 2)
        self.assertEqual(d.day, 28)

    def test_invalid_set_date(self):
        '''Test if the set_date method raises ValueError for invalid dates 
           and maintians the original date if an invalid date is attempted to be set.
        '''
        d = Date(2020, 2, 29)
        with self.assertRaises(ValueError):
            d.set_date(2021, 13, 29)
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

    def test_change_property(self):
        #Test if the date properties are read-only and cannot be changed directly
        d = Date(2015, 4, 30)
        with self.assertRaises(AttributeError):
            d.day = 15

    def test_to_numeric_string(self) -> str:
        #Test if the to_numeric_string method returns the correct string representation of the date
        d = Date(2020, 2, 29)
        self.assertEqual(d.to_numeric_string(), "02/29/2020")

    def test_to_month_first_string(self) -> str:
        #Test if the to_month_first_string method returns the correct string representation of the date
        d = Date(2020, 2, 29)
        self.assertEqual(d.to_month_first_string(), "February 29, 2020")

    def test_to_day_first_string(self) -> str:
        #Test if the to_day_first_string method returns the correct string representation of the date
        d = Date(2020, 2, 29)
        self.assertEqual(d.to_day_first_string(), "29 February 2020")

    def test_Conv_value(self):
        #Test if the Conv_Value method works correctly
        d = Date(1, 1, 2)
        self.assertEqual(d.Conv_Value(), 2)
        d2 = Date(1, 12, 31)
        self.assertEqual(d2.Conv_Value(), 365)

    def test_sub_overload(self) -> int:
        #Test if the __sub__ method works correctly
        d1 = Date(2020, 4, 10)
        d2 = Date(2020, 4, 9)
        result_1 = d1 - d2
        result_2 = d2 - d1
        self.assertIsInstance(result_1, int)
        self.assertEqual(result_1, 1)
        self.assertEqual(result_2, -1)


if __name__ == '__main__':
    unittest.main()
