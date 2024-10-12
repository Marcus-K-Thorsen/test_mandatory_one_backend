import random
import re

class GeneratePostalCode:
    """Generate a postal code."""
    def __init__(self, postalCodeList: list):
        if not postalCodeList: raise ValueError("postalCodeList is not provided.")
        if not isinstance(postalCodeList, list): raise TypeError("postalCodeList must be of type list.")
        if len(postalCodeList) == 0: raise ValueError("postalCodeList must contain at least one postal code.")
        if not all(isinstance(postalCode, str) for postalCode in postalCodeList): raise TypeError("postalCodeList must be a list of strings.")
        if not all(re.match(r"^\d{4}$", postalCode) for postalCode in postalCodeList): raise ValueError("The postal code must consist of 4 digits.")
        
        self.postalCodeList = postalCodeList
        
    def generate(self):
        return random.choice(self.postalCodeList)
        