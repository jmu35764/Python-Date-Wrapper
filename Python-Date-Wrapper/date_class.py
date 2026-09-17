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


