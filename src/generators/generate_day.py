import random
import re

REQUIRED_CONFIGURATION_KEYS = ["MONTHS_WITH_31_DAYS", "MONTHS_WITH_30_DAYS", "MONTH_31_RANGE", "MONTH_30_RANGE", "MONTH_28_RANGE"]
REQUIRED_LIST_KEYS = ["MONTHS_WITH_31_DAYS", "MONTHS_WITH_30_DAYS"]
REQUIRED_TUPLE_KEYS = ["MONTH_31_RANGE", "MONTH_30_RANGE", "MONTH_28_RANGE"]

CONFIGURATION = {
    "MONTHS_WITH_31_DAYS": [1, 3, 5, 7, 8, 10, 12],
    "MONTHS_WITH_30_DAYS": [4, 6, 9, 11],
    "MONTH_31_RANGE": (1, 31),
    "MONTH_30_RANGE": (1, 30),
    "MONTH_28_RANGE": (1, 28)
}

class GenerateDay:
    """Generate a random day in a given month based on the configuration."""
    
    
    def __init__(self, month: int, configuration: dict = CONFIGURATION):
        if not month: 
            raise ValueError("month is not provided.")
        
        if not configuration:
            raise ValueError("configuration is not provided.")
        
        if not isinstance(month, int):
            raise TypeError(f"month must be of type int, but got {type(month).__name__}.")
        
        if not isinstance(configuration, dict):
            raise TypeError(f"configuration must be of type dict, but got {type(configuration).__name__}.")
        
        if not all(key in configuration for key in REQUIRED_CONFIGURATION_KEYS):
            raise ValueError(f"configuration is missing required keys: {', '.join(REQUIRED_CONFIGURATION_KEYS)}")
        
        if not all(isinstance(configuration[key], list) for key in REQUIRED_LIST_KEYS):
            raise TypeError("MONTHS_WITH_31_DAYS and MONTHS_WITH_30_DAYS must be lists.")                
        
        if not all(isinstance(configuration[key], tuple) for key in REQUIRED_TUPLE_KEYS):
            raise TypeError("MONTH_31_RANGE, MONTH_30_RANGE, and MONTH_28_RANGE must be tuples.")
        
        for key in REQUIRED_LIST_KEYS:
            if not all(isinstance(day, int) for day in configuration[key]):
                raise TypeError(f"{key} must contain only integers.")
        
        for key in REQUIRED_LIST_KEYS:
            if not all(1 <= day <= 31 for day in configuration[key]):
                raise ValueError(f"{key} must contain only integers between 1 and 31. The values are {configuration[key]}")
            
        if not (1 <= month <= 12):
            raise ValueError("month must be between 1 and 12.")
        
        if month in configuration["MONTHS_WITH_31_DAYS"]:
            self.dayRange = configuration["MONTH_31_RANGE"]
        elif month in configuration["MONTHS_WITH_30_DAYS"]:
            self.dayRange = configuration["MONTH_30_RANGE"]
        else:
            self.dayRange = configuration["MONTH_28_RANGE"]

    def generate(self):
        return random.randint(self.dayRange[0], self.dayRange[1])
    