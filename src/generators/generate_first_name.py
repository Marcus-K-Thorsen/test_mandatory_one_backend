import random
import re

KEY_NAME = 'firstName'

class GenerateFirstName:
    """Generate a random first name from a predefined list."""
    
    def __init__(self, personList: list):
        # Throw an error if the list is empty
        if not personList: raise ValueError("The list is empty.")
        
        # Throw an error if the list is not a list
        if not isinstance(personList, list): raise ValueError("The list is not a list.")
        
        # Throw an error if the objects in the list
        # do not have the required keys
        if not all(KEY_NAME in person for person in personList):
            raise ValueError(f"The list does not contain the required keys ({KEY_NAME}).")
        
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
        # Get a random person from the list        
        randomPerson = random.choice(self.personList)
        
        # Return the first name of the random person
        return randomPerson[KEY_NAME]
    