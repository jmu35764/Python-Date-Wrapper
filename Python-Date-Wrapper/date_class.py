from datetime import date, timedelta
import calendar

class Date:
    def __init__(self, year: int = 1900, month: int = 1, day: int = 1) -> None:
        '''Automatically sets the initial date of the class 
           to the given year, month, and day. If no values are given, 
           it defaults to January 1, 1900.
        '''
        self.__date = date(year, month, day)

    @property
    def year(self) -> int:
        return self.__date.year

    @property
    def month(self) -> int:
        return self.__date.month

    @property
    def day(self) -> int:
        return self.__date.day
        
        
    def set_date(self, year: int, month: int, day: int) -> None:
        new_date = date(year, month, day)
        self.__date = new_date

    def is_leap_year(self) -> bool:
        ''' Tests if the year of the date is a leap year.
        '''
        return calendar.isleap(self.__date.year)

    @staticmethod
    def is_Year_leap(year: int) -> bool:
        '''Tests if the given year is a leap year.
        '''
        return calendar.isleap(year)   
    
    def last_day(self) -> int:
        return calendar.monthrange(self.__date.year, self.__date.month)[1]

    @staticmethod
    def last_day_of_month(year: int, month: int) -> int:
        return calendar.monthrange(year, month)[1]

    def to_numeric_string(self) -> str:
        '''Returns the date in standard numeric
           format (MM/DD/YYYY) as a string.
        '''
        return self.__date.strftime("%m/%d/%Y")

    def to_month_first_string(self) -> str:
        '''Returns the date in standard numeric
           format (Month/DD/YYYY) as a string.
        '''
        return self.__date.strftime("%B %d, %Y")

    def to_day_first_string(self) -> str:
        '''Returns the date in standard numeric
           format (DD/Month/YYYY) as a string.
        '''
        return self.__date.strftime("%d %B %Y")


    #This comment is to test if the branch appears on github

    
    def __sub__(self, other: object) -> int:
        '''Returns the difference in days between two Date objects.
        '''
        if not isinstance(other, Date):
            return NotImplemented

        return self.__date.toordinal() - other.__date.toordinal()




