import random
from src.generators.generate_year import GenerateYear
from src.generators.generate_month import GenerateMonth
from src.generators.generate_day import GenerateDay

class GenerateBirthdate:
    """Generate a random birthdate based on year, month, and day."""
    
    def __init__(self, year: int, month: int, day: int):
        
        if not year: 
            raise ValueError("year is not provided.")
        if not month: 
            raise ValueError("month is not provided.")
        if not day: 
            raise ValueError("day is not provided.")
        
        if not isinstance(year, int):
            raise TypeError(f"year must be of type int, but got {type(year).__name__}.")
        if not isinstance(month, int):
            raise TypeError(f"month must be of type int, but got {type(month).__name__}.")
        if not isinstance(day, int):
            raise TypeError(f"day must be of type int, but got {type(day).__name__}.")
        
        if not (1 <= year):
            raise ValueError("year must be greater than 0.")
        if not (1 <= month <= 12):
            raise ValueError("month must be between 1 and 12.")
        
        if month in [1, 3, 5, 7, 8, 10, 12]:
            if not (1 <= day <= 31):
                raise ValueError("day must be between 1 and 31.")
        elif month in [4, 6, 9, 11]:
            if not (1 <= day <= 30):
                raise ValueError("day must be between 1 and 30.")
        else:
            if not (1 <= day <= 28):
                raise ValueError("day must be between 1 and 28.")
        
        self.year = year
        self.month = month
        self.day = day

    def generate(self):
        y = str(self.year).zfill(4)
        m = str(self.month).zfill(2)
        d = str(self.day).zfill(2)

        return f"{y}-{m}-{d}"
