import json

from src.generators.generate_first_name import GenerateFirstName
from src.generators.generate_last_name import GenerateLastName
from src.generators.generate_gender import GenerateGender

cache = {}

class Person():
    """A data class used to return a list of persons."""
    
    @staticmethod
    def loadAll(file_path: str = './src/data/person-names.json', encoding: str = 'utf-8', overwriteCache: bool = False) -> list:
        """Load all persons from a json file."""
        global cache
        
        if file_path is None: raise ValueError("The file path is not provided.")
        if encoding is None: raise ValueError("The encoding is not provided.")
        if overwriteCache is None: raise ValueError("The overwriteCache is not provided.")
        if not isinstance(file_path, str): raise TypeError(f"The file path must be of type str, but got {type(file_path).__name__}.")
        if not isinstance(encoding, str): raise TypeError(f"The encoding must be of type str, but got {type(encoding).__name__}.")
        if not isinstance(overwriteCache, bool): raise TypeError(f"The overwriteCache must be of type bool, but got {type(overwriteCache).__name__}.")
        
        if not overwriteCache and file_path in cache:
            return cache[file_path]
        else:
            with open(file_path, 'r', encoding=encoding) as f:
                data = json.load(f)
                
            if not isinstance(data, dict): raise TypeError("The data must be a dictionary.")
            if 'persons' not in data: raise ValueError("The data must contain the key 'persons'.")
                                   
            personList = data['persons']
            
            # ensure that the name- and gender generators can load
            # the data without any issues. So, if the person-names.json
            # file becomes corrupted, the application will raise an error
            GenerateFirstName(personList)
            GenerateLastName(personList)
            GenerateGender(personList)
            # Also, because CPR expect specific genders, we also need to check
            # check if the person-names.json file only contains male or female values
            for person in personList:
                if person["gender"] not in ["male", "female"]:
                    raise ValueError("The gender value must be either 'male' or 'female'.")
            
            # cache the data to avoid reading the file multiple times
            # and making multiple checks of the integrity of the data.
            cache[file_path] = personList
                
            return personList
