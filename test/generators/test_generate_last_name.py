import pytest
from src.generators.generate_last_name import GenerateLastName


@pytest.mark.parametrize("personList, excepted", [
    (None, ValueError),                             # Decision 1                (personList is not provided)
    ({}, ValueError),                               # Decision 2 and 3          (personList is provided and not a list)
    ([], ValueError),                               # Decision 4 and 5          (personList is a list and empty)
    ([""], TypeError),                              # Decision 6 and 7          (personList is a list and does not contain dictionaries)
    ([{None: "Anne"}], ValueError),                 # Decision 8 and 9          (personList is a list, contain dicts, but the keys are not strings)
    ([{"wrongKey": None}], ValueError),             # Decision 10 and 11        (personList is a list, contain dicts, keys are strings but values are not)
    ([{ "wrongKey": "Anne" }], ValueError),         # Decision 12 and 13        (personList is a list, contain dicts, are strings, but the key is not "lastName")
    ([{ "lastName": "Anne Lise " }], ValueError),   # Decision 14 and 15        (personList is a list, contain dicts, are strings, key is "lastName", but value does not follow regex)
    ([{ "lastName": "Anne" }], "Anne"),             # Decision 16               (personList is a list, contain dicts, are strings, key is "lastName", value follows regex)
])
def test_generate_first_name_with_decision_coverage(personList, excepted):
    if isinstance(excepted, str): 
        assert GenerateLastName(personList).generate() == excepted, f"Expected {personList[0].get('lastName')} to be a valid last name"
    else: 
        with pytest.raises(excepted): GenerateLastName(personList), f"Expected {personList} to raise exception {excepted}"
      

@pytest.mark.parametrize("personList", [
    [{ "lastName": "Simonsen" }],
    [{ "lastName": "Christoffersen" }],
    [{ "lastName": "Kjær" }],
])
def test_generate_last_name_with_valid_partitions(personList):
    generator = GenerateLastName(personList)
    lastName = generator.generate()
    
    assert lastName == personList[0].get("lastName"), f"Expected {personList[0].get('lastName')} to be a valid last name"
    

@pytest.mark.parametrize("personList, expected", [
    ([{ "lastName": "" }], ValueError), 
    ([{ "lastName": "Anne Lise " }], ValueError), 
    ([{ "lastName": "Anne..Lise" }], ValueError), 
    ([{ "lastName": "Ann@" }], ValueError), 
    ([{ "lastName": "324543" }], ValueError), 
    ([{ "lastName": "anne" }], ValueError), 
    ([{ "": "Anne" }], ValueError), 
    ([{ "wrongKey": "Anne" }], ValueError),
    ([{ None: "Anne" }], ValueError),
    ([{ "lastName": None }], TypeError),
])
def test_generate_first_name_with_no_valid_partitions(personList, expected):
    with pytest.raises(expected):
        GenerateLastName(personList), f"Expected {personList[0].get('lastName')} to be an invalid last name"


@pytest.mark.parametrize("personList", [
    [{ "lastName": "A" }],
    [{ "lastName": "An" }],
    [{ "lastName": "Ann" }],
])
def test_generate_last_name_with_inner_boundaries(personList):
    generator = GenerateLastName(personList)
    lastName = generator.generate()
    
    assert lastName == personList[0].get("lastName"), f"Expected {personList[0].get('lastName')} to be inside the valid boundaries"
    

@pytest.mark.parametrize("personList", [
    [{ "lastNam": "" }],
    [{ "lastName": "" }],
    [{ "lastName": "a" }],
])
def test_generate_first_name_with_outer_boundaries(personList):
    with pytest.raises(ValueError):
        GenerateLastName(personList), f"Expected {personList[0].get('lastName')} to be outside the valid boundaries"
   
