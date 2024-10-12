from unittest.mock import patch, mock_open
import pytest
import json

from src.models.person import Person

"""
Why Mocking?
This test class mocks the open and json.load functions to test the loadAll method in the Person class
without actually having to read any files from the disk. We expect the builtins.open and json.load
already work, so all we care about is whether the Person class can handle the data correctly.

Also, this approach ensures we don't have to store multiple corrupted JSON files only meant for testing purposes.
"""

@pytest.mark.parametrize("mockJsonFile", [
    {'persons': [{'firstName': 'Name', 'lastName': 'Name', 'gender': 'male'}]},
    {'persons': [{'firstName': 'Name', 'lastName': 'Name', 'gender': 'female'}]},
    {'persons': [{'firstName': 'Name Name', 'lastName': 'Name', 'gender': 'female'}]},
    {'persons': [{'firstName': 'Name N.', 'lastName': 'Name', 'gender': 'female'}]},
])
def test_person_load_all_with_valid_partitions(mockJsonFile):
    # Mock open and json.load
    with patch('builtins.open', mock_open(read_data=json.dumps(mockJsonFile))):
        with patch('json.load', return_value=mockJsonFile):
            personList = Person.loadAll(file_path='./src/data/person-names.json', encoding='utf-8', overwriteCache=True)
    
    
    assert personList == mockJsonFile['persons'], f"Expected {personList} to be a valid list of persons"
    

@pytest.mark.parametrize("mockJsonFile, expected", [
    ({None: [{'firstName': 'Name', 'lastName': 'Name', 'gender': 'male'}]}, ValueError),
    ({"": [{'firstName': 'Name', 'lastName': 'Name', 'gender': 'male'}]}, ValueError),
    ({'persons': None}, ValueError),
    ({'persons': ""}, ValueError),
    ({'persons': [{None: 'Name', 'lastName': 'Name', 'gender': 'male'}]}, ValueError),
    ({'persons': [{'firstName': None, 'lastName': 'Name', 'gender': 'male'}]}, TypeError),
    ({'persons': [{'firstName': 'Name', None: 'Name', 'gender': 'male'}]}, ValueError),
    ({'persons': [{'firstName': 'Name', 'lastName': None, 'gender': 'male'}]}, TypeError),
    ({'persons': [{'firstName': 'Name', 'lastName': 'Name', None: 'male'}]}, ValueError),
    ({'persons': [{'firstName': 'Name', 'lastName': 'Name', 'gender': None}]}, TypeError),
    ({'persons': [{'firstName': 'Name', 'lastName': 'Name', 'gender': 'not_male_or_female'}]}, ValueError),
])
def test_person_load_all_with_no_valid_partitions(mockJsonFile, expected):
    with pytest.raises(expected):
        # Mock open and json.load
        with patch('builtins.open', mock_open(read_data=json.dumps(mockJsonFile))):
            with patch('json.load', return_value=mockJsonFile):
                Person.loadAll(file_path='./src/data/person-names.json', encoding='utf-8', overwriteCache=True)


@pytest.mark.parametrize("mockJsonFile", [
    {'persons': [{'firstName': 'A', 'lastName': 'A', 'gender': 'male'}]},
    {'persons': [{'firstName': 'A', 'lastName': 'A', 'gender': 'female'}]},
    {'persons': [{'firstName': 'Aa', 'lastName': 'Aa', 'gender': 'male'}]},
    {'persons': [{'firstName': 'Aa', 'lastName': 'Aa', 'gender': 'female'}]},
])
def test_generate_birthdate_with_inner_boundaries(mockJsonFile):
    # Mock open and json.load
    with patch('builtins.open', mock_open(read_data=json.dumps(mockJsonFile))):
        with patch('json.load', return_value=mockJsonFile):
            personList = Person.loadAll(file_path='./src/data/person-names.json', encoding='utf-8', overwriteCache=True)
    
    
    assert personList == mockJsonFile['persons'], f"Expected {personList} to be inside the valid boundaries"


@pytest.mark.parametrize("mockJsonFile, expected", [
    ({'persons': []}, ValueError),
    ({'persons': [{'firstName': '', 'lastName': 'A', 'gender': 'male'}]}, ValueError),
    ({'persons': [{'firstName': 'A', 'lastName': '', 'gender': 'male'}]}, ValueError),
    ({'persons': [{'firstName': 'A', 'lastName': '', 'gender': 'mal'}]}, ValueError),
    ({'persons': [{'firstName': '', 'lastName': 'A', 'gender': 'female'}]}, ValueError),
    ({'persons': [{'firstName': 'A', 'lastName': '', 'gender': 'female'}]}, ValueError),
    ({'persons': [{'firstName': 'A', 'lastName': '', 'gender': 'femal'}]}, ValueError),
])
def test_generate_birthdate_with_outer_boundaries(mockJsonFile, expected):
    with pytest.raises(expected):
        # Mock open and json.load
        with patch('builtins.open', mock_open(read_data=json.dumps(mockJsonFile))):
            with patch('json.load', return_value=mockJsonFile):
                Person.loadAll(file_path='./src/data/person-names.json', encoding='utf-8', overwriteCache=True)

     
