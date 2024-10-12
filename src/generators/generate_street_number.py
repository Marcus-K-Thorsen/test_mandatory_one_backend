import random

class GenerateStreetNumber:
    """Generate a random street number between a given range."""
    
    def __init__(self, streetNumberRange: tuple = (1, 999)):
        if not streetNumberRange: raise ValueError("streetNumberRange is not provided.")
        if not isinstance(streetNumberRange, tuple): raise TypeError("streetNumberRange must be a tuple.")
        if len(streetNumberRange) != 2: raise ValueError("streetNumberRange must contain two elements.")
        if not all(isinstance(i, int) for i in streetNumberRange): raise TypeError("streetNumberRange must contain only integers.")
        if not all(i >= 0 for i in streetNumberRange): raise ValueError("streetNumberRange must contain only positive integers.")
        if not streetNumberRange[0] <= streetNumberRange[1]: raise ValueError("The first element must be less than or equal to the second element.")
        
        self.streetNumberRange = streetNumberRange
    
    def generate(self):
        return random.randint(self.streetNumberRange[0], self.streetNumberRange[1])
