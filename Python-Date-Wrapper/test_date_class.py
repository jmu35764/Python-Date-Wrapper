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

    def test_sub_overload(self) -> int:
        #Test if the __sub__ method works correctly
        d1 = Date(2014, 4, 18)
        d2 = Date(2014, 4, 10)
        d3 = Date(2014, 5, 9)
        d4 = Date(2006, 2, 2)
        d5 = Date(2003, 11, 10)

        self.assertIsInstance(d1-d2, int)
        self.assertEqual(d1-d2, 8)
        self.assertEqual(d2-d1, -8)
        self.assertEqual(d1-d1, 0)
        self.assertEqual(d3-d2, 29)
        self.assertEqual(d4-d5, 815)
        with self.assertRaises(TypeError):
            d1 - 5

    def test_increment_overload(self) -> "Date":
        #Test if the increment method works correctly
        d1 = Date(2014, 4, 18)
        self.assertEqual(d1.increment().to_numeric_string(), "04/19/2014")
        d2 = Date(2014, 4, 30)
        self.assertEqual(d2.increment().to_numeric_string(), "05/01/2014")
        d3 = Date(2014, 1, 31)
        self.assertEqual(d3.increment().to_numeric_string(), "02/01/2014")
        d4 = Date(2014, 2, 28)
        self.assertEqual(d4.increment().to_numeric_string(), "03/01/2014")
        d5 = Date(2016, 2, 28)
        self.assertEqual(d5.increment().to_numeric_string(), "02/29/2016")
        d5 = Date(2016, 2, 29)
        self.assertEqual(d5.increment().to_numeric_string(), "03/01/2016")
        d6 = Date(2014, 12, 31)
        self.assertEqual(d6.increment().to_numeric_string(), "01/01/2015")
        test_date = Date(2014, 12, 30)
        returned_value = test_date.increment()
        self.assertIs(returned_value, test_date)

    def test_decrement_overload(self) -> "Date":
        #Test if the decrement method works correctly
        d1 = Date(2014, 5, 1)
        self.assertEqual(d1.decrement().to_numeric_string(), "04/30/2014")
        d2 = date(2014, 3, 1)
        self.assertEqual(d2.decrement().to_numeric_string(), "02/28/2014")
        d3 = Date(2016, 3, 1)
        self.assertEqual(d3.decrement().to_numeric_string(), "02/29/2016")
        d4 = Date(2014, 1, 1)
        self.assertEqual(d4.decrement().to_numeric_string(), "12/31/2013")
        test_date = Date(2014, 12, 30)
        returned_value = test_date.decrement()
        self.assertIs(returned_value, test_date)

        


if __name__ == '__main__':
    unittest.main()
