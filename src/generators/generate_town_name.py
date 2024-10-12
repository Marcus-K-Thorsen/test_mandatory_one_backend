import random

class GenerateTownName:
    """Generate a town name."""
    
    def __init__(self, townNameList: list):
        if not townNameList: raise ValueError("townNameList is not provided.")
        if not isinstance(townNameList, list): raise TypeError("townNameList must be of type list.")
        if len(townNameList) == 0: raise ValueError("townNameList must contain at least one town name.")
        if not all(isinstance(townName, str) for townName in townNameList): raise TypeError("townNameList must be a list of strings.")
        if not all(townName for townName in townNameList): raise ValueError("The town name must not be empty.")
        if not all(townName[0].isupper() for townName in townNameList): raise ValueError("The town name must start with an uppercase letter.")
        
        self.townNameList = townNameList
        
    def generate(self):
        return random.choice(self.townNameList)
