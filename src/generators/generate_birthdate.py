import random
from src.generators.generate_year import GenerateYear
from src.generators.generate_month import GenerateMonth
from src.generators.generate_day import GenerateDay

DAY_CONF = {
    "MONTHS_WITH_31_DAYS": [1, 3, 5, 7, 8, 10, 12],
    "MONTHS_WITH_30_DAYS": [4, 6, 9, 11],
    "MONTH_31_RANGE": (1, 31),
    "MONTH_30_RANGE": (1, 30),
    "MONTH_28_RANGE": (1, 28)
}

class GenerateBirthdate:
    """Generate a random birthdate based on some predefined rules."""
    
    def __init__(self, yearRange: tuple, monthRange: tuple, dayConfiguration: dict = DAY_CONF):
        # Rely on error handling from other classes
        self.year = GenerateYear(yearRange).generate()
        self.month = GenerateMonth(monthRange).generate()
        self.day = GenerateDay(self.month, dayConfiguration).generate()

    def generate(self):
        y = self.year
        m = self.month if self.month > 9 else f'0{self.month}'
        d = self.day if self.day > 9 else f'0{self.day}'
        
        return f"{y}-{m}-{d}"
