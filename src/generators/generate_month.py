import random
import re

class GenerateMonth:
    """Generate a random month between two given month."""
    
    def __init__(self, monthRange: tuple):
        if not monthRange: 
            raise ValueError("monthRange is not provided.")
        
        if not isinstance(monthRange, tuple):
            raise ValueError(f"monthRange must be of type tuple, but got {type(monthRange).__name__}.")
        
        if len(monthRange) != 2:
            raise ValueError("monthRange must contain two values.")
        
        if not all(isinstance(month, int) for month in monthRange):
            raise TypeError("Both values in monthRange must be integers.")
        
        if not (1 <= monthRange[0] <= 12):
            raise ValueError("The first value must be between 1 and 12.")
        
        if not (1 <= monthRange[1] <= 12):
            raise ValueError("The second value must be between 1 and 12.")
     
        if monthRange[0] > monthRange[1]:
            raise ValueError("The first value cannot be greater than the second value.")
        
        self.monthRange = monthRange

    def generate(self):
        return random.randint(self.monthRange[0], self.monthRange[1])
    