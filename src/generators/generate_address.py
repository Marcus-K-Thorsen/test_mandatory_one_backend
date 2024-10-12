import random

from src.models.person import Person
from src.data.generator import Generator

from src.generators.generate_street_name import GenerateStreetName
from src.generators.generate_street_number import GenerateStreetNumber
from src.generators.generate_street_floor import GenerateStreetFloor
from src.generators.generate_street_door import GenerateStreetDoor
from src.generators.generate_postal_code import GeneratePostalCode
from src.generators.generate_town_name import GenerateTownName

class GenerateAddress:
    """Generate a fake address."""
    
    def __init__(self, options: dict = {}):
        """
            The constructor automatically generates
            the data when an instance of the class is created.
        """
        if not isinstance(options, dict): raise TypeError("options must be a dictionary.")
        
        # street must be in the options
        if not "street" in options: raise ValueError("street is not provided.")
        if not isinstance(options["street"], str): raise TypeError("street must be a string.")
        
        # number must be in the options
        if not "number" in options: raise ValueError("number is not provided.")
        if not isinstance(options["number"], int): raise TypeError("number must be an integer.")
        
        # floor must be in the options
        if not "floor" in options: raise ValueError("floor is not provided.")
        if not isinstance(options["floor"], str): raise TypeError("floor must be a string.")
        
        # door must be in the options
        if not "door" in options: raise ValueError("door is not provided.")
        if not isinstance(options["door"], str): raise TypeError("door must be a string.")
        
        # postal_code must be in the options
        if not "postal_code" in options: raise ValueError("postal_code is not provided.")
        if not isinstance(options["postal_code"], str): raise TypeError("postal_code must be a string.")
        
        # town_name must be in the options
        if not "town_name" in options: raise ValueError("town_name is not provided.")
        if not isinstance(options["town_name"], str): raise TypeError("town_name must be a string.")
        
        self.street = options["street"]
        self.number = options["number"]
        self.floor = options["floor"]
        self.door = options["door"]
        self.postal_code = options["postal_code"]
        self.town_name = options["town_name"]

    def generate():
        """Factory method to create a new Address instance."""

        return GenerateAddress(options={
            "street": GenerateStreetName().generate(),
            "number": GenerateStreetNumber().generate(),
            "floor": GenerateStreetFloor().generate(),
            "door": GenerateStreetDoor().generate(),
            "postal_code": GeneratePostalCode.generate(),
            "town_name": GenerateTownName.generate()
        })