from datetime import date
import calendar

class Date:
    def __init__(self, year: int = 1900, month: int = 1, day: int = 1) -> None:
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
        return calendar.isleap(self.__date.year)

    @staticmethod
    def is_Year_leap(year: int) -> bool:
        return calendar.isleap(year)   
    
    def last_day(self) -> int:
        return calendar.monthrange(self.__date.year, self.__date.month)[1]

    @staticmethod
    def last_day_of_month(year: int, month: int) -> int:
        return calendar.monthrange(year, month)[1]

    def to_numeric_string(self) -> str:
        return self.__date.strftime("%m/%d/%Y")

    def to_month_first_string(self) -> str:
        return self.__date.strftime("%B %d, %Y")




