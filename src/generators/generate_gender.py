import random
import re

KEY_NAME = 'gender'

class GenerateGender:
    """Generate a random gender from a predefined list."""
    
    def __init__(self, genderList: list):
        if not genderList: 
            raise ValueError("genderList is not provided.")
        
        if not isinstance(genderList, list): 
            raise ValueError("genderList must be of type list.")
        
        if len(genderList) == 0: 
            raise ValueError("genderList must contain at least one person.")
        
        if not all(isinstance(gender, dict) for gender in genderList):
            raise TypeError("genderList must contain dictionaries.")
        
        if not all(KEY_NAME in gender for gender in genderList):
            raise ValueError(f"The list does not contain the required keys ({KEY_NAME}) or one of the keys is not a string.")
        
        if not all(isinstance(gender[KEY_NAME], str) for gender in genderList):
            raise TypeError("The gender value must be a string.")
        
        if not all(re.match(r"^.+$", gender[KEY_NAME]) for gender in genderList):
            raise ValueError("The gender value must be at least one character long.")
        
        self.genderList = genderList

    def generate(self):
        return random.choice(self.genderList)[KEY_NAME]
    