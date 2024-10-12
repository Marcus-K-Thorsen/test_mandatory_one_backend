import json

personList = None

class Person():
    """A data class used to return a list of persons."""
    
    @staticmethod
    def loadAll(file_path: str = './src/data/person-names.json', encoding: str = 'utf-8'):
        """Load all persons from a json file."""
        global personList
        
        if personList is not None:
            return personList
        else:
            with open(file_path, 'r', encoding=encoding) as f:
                data = json.load(f)
            
            personList = data['persons']
            return personList
