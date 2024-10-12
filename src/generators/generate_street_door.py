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
            
        if doorTypes is not None:
            if not isinstance(doorTypes, list): raise TypeError("doorTypes must be a list.")
            if len(doorTypes) == 0: raise ValueError("doorTypes must contain at least one element.")
            if not all(isinstance(i, str) for i in doorTypes): raise TypeError("doorTypes must contain only strings.")
            if not all(i for i in doorTypes): raise ValueError("doorTypes must not contain empty strings.")            
        
        if doorNumberRange is None and doorTypes is None:
            raise ValueError("At least one of the parameters must be provided.")
        
        # Must be defined on the class no
        # matter the value.
        self.doorNumberRange = doorNumberRange
        self.doorTypes = doorTypes
    
    def generate(self):
        choices = self.doorTypes if self.doorTypes is not None else []
        
        if self.doorNumberRange is not None:
            choices.append(str(random.randint(self.doorNumberRange[0], self.doorNumberRange[1])))
        
        return random.choice(choices)
