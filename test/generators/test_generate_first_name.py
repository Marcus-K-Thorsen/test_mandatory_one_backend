import pytest
from src.generators.generate_first_name import GenerateFirstName


@pytest.mark.parametrize("personList, excepted", [
    (None, ValueError),                             # Decision 1                (personList is not provided)
    ({}, ValueError),                               # Decision 2 and 3          (personList is provided and not a list)
    ([], ValueError),                               # Decision 4 and 5          (personList is a list and empty)
    ([""], TypeError),                              # Decision 6 and 7          (personList is a list and does not contain dictionaries)
    ([{None: "Anne"}], ValueError),                 # Decision 8 and 9          (personList is a list, contain dicts, but the keys are not strings)
    ([{"wrongKey": None}], ValueError),             # Decision 10 and 11        (personList is a list, contain dicts, keys are strings but values are not)
    ([{ "wrongKey": "Anne" }], ValueError),         # Decision 12 and 13        (personList is a list, contain dicts, are strings, but the key is not "firstName")
    ([{ "firstName": "Anne Lise " }], ValueError),  # Decision 14 and 15        (personList is a list, contain dicts, are strings, key is "firstName", but value does not follow regex)
    ([{ "firstName": "Anne" }], "Anne"),            # Decision 16               (personList is a list, contain dicts, are strings, key is "firstName", value follows regex)
])
def test_generate_first_name_with_decision_coverage(personList, excepted):
    if isinstance(excepted, str): 
        assert GenerateFirstName(personList).generate() == excepted, f"Expected {personList[0].get('firstName')} to be a valid first name"
    else: 
        with pytest.raises(excepted): GenerateFirstName(personList), f"Expected {personList} to raise exception {excepted}"
      

@pytest.mark.parametrize("personList", [
    [{ "firstName": "Annemette P." }],
    [{ "firstName": "Anne-Lise N." }],
    [{ "firstName": "Børge B." }],
])
def test_generate_first_name_with_valid_partitions(personList):
    generator = GenerateFirstName(personList)
    firstName = generator.generate()
    
    assert firstName == personList[0].get("firstName"), f"Expected {personList[0].get('firstName')} to be a valid first name"
    

@pytest.mark.parametrize("personList, expected", [
    ([{ "firstName": "" }], ValueError), 
    ([{ "firstName": "Anne Lise " }], ValueError), 
    ([{ "firstName": "Anne..Lise" }], ValueError), 
    ([{ "firstName": "Ann@" }], ValueError), 
    ([{ "firstName": "324543" }], ValueError), 
    ([{ "firstName": "anne" }], ValueError), 
    ([{ "": "Anne" }], ValueError), 
    ([{ "wrongKey": "Anne" }], ValueError),
    ([{ None: "Anne" }], ValueError),
    ([{ "firstName": None }], TypeError),
])
def test_generate_first_name_with_no_valid_partitions(personList, expected):
    with pytest.raises(expected):
        GenerateFirstName(personList), f"Expected {personList[0].get('firstName')} to be an invalid first name"


@pytest.mark.parametrize("personList", [
    [{ "firstName": "A" }],
    [{ "firstName": "An" }],
    [{ "firstName": "Ann" }],
])
def test_generate_first_name_with_inner_boundaries(personList):
    generator = GenerateFirstName(personList)
    firstName = generator.generate()
    
    assert firstName == personList[0].get("firstName"), f"Epected {personList[0].get('firstName')} to be inside the valid boundaries"
    

@pytest.mark.parametrize("personList", [
    [{ "firstNam": "" }],
    [{ "firstName": "" }],
    [{ "firstName": "a" }],
])
def test_generate_first_name_with_outer_boundaries(personList):
    with pytest.raises(ValueError):
        GenerateFirstName(personList), f"Expected {personList[0].get('firstName')} to be outside the valid boundaries"
        

    