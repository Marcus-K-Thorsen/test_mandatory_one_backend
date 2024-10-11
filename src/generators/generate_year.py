import random
import re

class GenerateYear:
    """Generate a random year between two given years."""
    
    def __init__(self, yearRange: tuple):
        if not yearRange: 
            raise ValueError("yearRange is not provided.")
        
        if not isinstance(yearRange, tuple):
            raise ValueError(f"yearRange must be of type tuple, but got {type(yearRange).__name__}.")
        
        if len(yearRange) != 2:
            raise ValueError("yearRange must contain two values.")
        
        if not all(isinstance(year, int) for year in yearRange):
            raise TypeError("Both values in yearRange must be integers.")
        
        if yearRange[0] < 1 or yearRange[1] < 1:
            raise ValueError("The values in yearRange must be at least 1.")
     
        if yearRange[0] > yearRange[1]:
            raise ValueError("The first value cannot be greater than the second value.")
        
        self.yearRange = yearRange

    def generate(self):
        return random.randint(self.yearRange[0], self.yearRange[1])
    