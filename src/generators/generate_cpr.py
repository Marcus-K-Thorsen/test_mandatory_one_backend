import random
import re

CPR_OPTIONS = {
    "last_three_digit_range": (0, 9),
    "male_last_digit_list": [1, 3, 5, 7, 9],
    "female_last_digit_list": [0, 2, 4, 6, 8]
}

class GenerateCPR:
    """Generate a random CPR number based on the given day, month, year, and gender."""
    
    def __init__(self, gender: str, date: dict, options: dict = CPR_OPTIONS):
        day = date.get("day")
        month = date.get("month")
        year = date.get("year")
        
        last_three_digit_range = options.get("last_three_digit_range") # , (0, 9)
        male_last_digit_list = options.get("male_last_digit_list") # , [1, 3, 5, 7, 9]
        female_last_digit_list = options.get("female_last_digit_list") # , [0, 2, 4, 6, 8]
        
        if not day: raise ValueError("day is not provided.")
        if not month: raise ValueError("month is not provided.")
        if not year: raise ValueError("year is not provided.")
        if not gender: raise ValueError("gender is not provided.")
        if not last_three_digit_range: raise ValueError("last_three_digit_range is not provided.")
        if not male_last_digit_list: raise ValueError("male_last_digit_list is not provided.")
        if not female_last_digit_list: raise ValueError("female_last_digit_list is not provided.")
        
        if not isinstance(day, int): raise TypeError(f"day must be of type int, but got {type(day).__name__}.")
        if not isinstance(month, int): raise TypeError(f"month must be of type int, but got {type(month).__name__}.")
        if not isinstance(year, int): raise TypeError(f"year must be of type int, but got {type(year).__name__}.")
        if not isinstance(gender, str): raise TypeError(f"gender must be of type str, but got {type(gender).__name__}.")
        if not isinstance(last_three_digit_range, tuple): raise TypeError(f"last_three_digit_range must be of type tuple, but got {type(last_three_digit_range).__name__}.")
        if not isinstance(male_last_digit_list, list): raise TypeError(f"male_last_digit_list must be of type list, but got {type(male_last_digit_list).__name__}.")
        if not isinstance(female_last_digit_list, list): raise TypeError(f"female_last_digit_list must be of type list, but got {type(female_last_digit_list).__name__}.")
        
        if not (1 <= day <= 31): raise ValueError("day must be between 1 and 31.")
        if not (1 <= month <= 12): raise ValueError("month must be between 1 and 12.")
        if not (1 <= year): raise ValueError("year must be greater than 0.")

        if not re.match(r"^male$|^female$", gender): raise ValueError(f"gender must be either male or female. The value is: {gender}")
        
        if not all(isinstance(i, int) for i in last_three_digit_range): raise TypeError("last_three_digit_range must contain only integers.")
        if not all(0 <= i <= 9 for i in last_three_digit_range): raise ValueError("last_three_digit_range must contain only integers between 0 and 9.")
        
        if not all(isinstance(i, int) for i in male_last_digit_list): raise TypeError("male_last_digit_list must contain only integers.")
        if not all(i % 2 != 0 for i in male_last_digit_list): raise ValueError("male_last_digit_list must contain only odd numbers.")
        
        if not all(isinstance(i, int) for i in female_last_digit_list): raise TypeError("female_last_digit_list must contain only integers.")
        if not all(i % 2 == 0 for i in female_last_digit_list): raise ValueError("female_last_digit_list must contain only even numbers.")
        
        self.day = day
        self.month = month
        self.year = year
        self.gender = gender
        self.last_three_digit_range = last_three_digit_range
        self.male_last_digit_list = male_last_digit_list
        self.female_last_digit_list = female_last_digit_list

    def generate(self):
        last_three_digit_first = random.randint(self.last_three_digit_range[0], self.last_three_digit_range[1])
        last_three_digit_second = random.randint(self.last_three_digit_range[0], self.last_three_digit_range[1])
        last_three_digit_third = random.randint(self.last_three_digit_range[0], self.last_three_digit_range[1])        
        last_three_digits = f"{last_three_digit_first}{last_three_digit_second}{last_three_digit_third}"
        
        last_digit = random.choice(self.male_last_digit_list) if self.gender == "male" else random.choice(self.female_last_digit_list)
        last_two_year_digits = str(self.year)[2:]
        
        return f"{self.day}{self.month}{last_two_year_digits}{last_three_digits}{last_digit}"
    