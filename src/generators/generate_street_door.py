import random

class GenerateStreetDoor:
    """Generate a random door number or type."""
    
    def __init__(self, doorNumberRange: tuple = (1, 50), doorTypes: list = ['th', 'tv', 'mf']):
        if doorNumberRange is not None:
            if not isinstance(doorNumberRange, tuple): raise TypeError("doorNumberRange must be a tuple.")
            if len(doorNumberRange) != 2: raise ValueError("doorNumberRange must contain two elements.")
            if not all(isinstance(i, int) for i in doorNumberRange): raise TypeError("doorNumberRange must contain only integers.")
            if not all(i >= 0 for i in doorNumberRange): raise ValueError("doorNumberRange must contain only positive integers.")
            if not doorNumberRange[0] <= doorNumberRange[1]: raise ValueError("The first element must be less than or equal to the second element.")
            self.doorNumberRange = doorNumberRange
            
        if doorTypes is not None:
            if not isinstance(doorTypes, list): raise TypeError("doorTypes must be a list.")
            if not all(isinstance(i, str) for i in doorTypes): raise TypeError("doorTypes must contain only strings.")
            self.doorTypes = doorTypes
    
    def generate(self):
        choices = self.doorTypes if self.doorTypes is not None else []
        
        if self.doorNumberRange is not None:
            choices.append(str(random.randint(self.doorNumberRange[0], self.doorNumberRange[1])))
        
        return random.choice(choices)
