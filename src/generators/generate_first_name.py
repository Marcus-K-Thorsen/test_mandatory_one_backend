import random
import re

KEY_NAME = 'firstName'

class GenerateFirstName:
    """Generate a random first name from a predefined list."""
    
    def __init__(self, personList: list):
        if not personList: 
            raise ValueError("personList is not provided.")
        
        if not isinstance(personList, list): 
            raise ValueError("personList must be of type list.")
        
        if len(personList) == 0: 
            raise ValueError("personList must contain at least one person.")
        
        if not all(isinstance(person, dict) for person in personList):
            raise TypeError("personList must contain dictionaries.")
        
        if not all(KEY_NAME in person for person in personList):
            raise ValueError(f"The list does not contain the required keys ({KEY_NAME}) or one of the keys is not a string.")
        
        if not all(isinstance(person[KEY_NAME], str) for person in personList):
            raise TypeError("The first name must be a string.")
        
        # Throw an error if the format of the first name
        # doesn't follow the rules:
        # - Must consist of alphabetic Danish strings.
        # - Can contain one space, one dot (at the end), or one hyphen.
        # - Capital letters should only be used at the beginning, after a hyphen or space.
        if not all(re.match(r"^[A-ZÆØÅ][a-zæøå]*([ -][A-ZÆØÅ][a-zæøå]*)*\.?$", person[KEY_NAME]) for person in personList):
            raise ValueError("The first name does not follow the rules.")
        
        # Set the list of persons
        self.personList = personList

    def generate(self):
        return random.choice(self.personList)[KEY_NAME]
    