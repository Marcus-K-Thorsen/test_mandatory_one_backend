import random

class GenerateStreetFloor:
    """Generate a random floor number between a given range or 'st'. for zero."""
    
    def __init__(self, floorRange: tuple = (0, 99)):
        if not floorRange: raise ValueError("floorRange is not provided.")
        if not isinstance(floorRange, tuple): raise TypeError("floorRange must be a tuple.")
        if len(floorRange) != 2: raise ValueError("floorRange must contain two elements.")
        if not all(isinstance(i, int) for i in floorRange): raise TypeError("floorRange must contain only integers.")
        if not all(i >= 0 for i in floorRange): raise ValueError("floorRange must contain only positive integers.")
        if not floorRange[0] <= floorRange[1]: raise ValueError("The first element must be less than or equal to the second element.")
        
        self.floorRange = floorRange
    
    def generate(self):
        return "st" if self.floorRange == 0 else random.randint(self.floorRange[0], self.floorRange[1]).__str__()