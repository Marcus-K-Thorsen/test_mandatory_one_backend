import pytest
from src.generators.generate_first_name import GenerateFirstName


@pytest.mark.parametrize("personList", [
    [{ "firstName": "Annemette P." }],
    [{ "firstName": "Anne-Lise N." }],
    [{ "firstName": "Børge B." }],
])
def test_generate_first_name_with_valid_partitions(personList):
    generator = GenerateFirstName(personList)
    firstName = generator.generate()
    
    assert firstName == personList[0].get("firstName"), f"First name {expected} is not valid" 
    

@pytest.mark.parametrize("personList", [
    [{ "firstName": "" }],
    [{ "firstName": "Anne Lise " }],
    [{ "firstName": "Anne..Lise" }],
    [{ "firstName": "Ann@" }],
    [{ "firstName": "324543" }],
    [{ "firstName": "anne" }],
    [{ "": "Anne" }],
    [{ "wrongKey": "Anne" }],
])
def test_generate_first_name_with_no_valid_partitions(personList):
    with pytest.raises(ValueError):
        GenerateFirstName(personList), f"First name {personList[0].get('firstName')} is not invalid"


@pytest.mark.parametrize("personList", [
    [{ "firstNam": "" }],
    [{ "firstName": "" }],
    [{ "firstName": "a" }],
])
def test_generate_first_name_with_outer_boundaries(personList):
    with pytest.raises(ValueError):
        GenerateFirstName(personList), f"First name {personList[0].get('firstName')} is not outside the boundaries"
        
        
@pytest.mark.parametrize("personList", [
    [{ "firstName": "A" }],
    [{ "firstName": "An" }],
    [{ "firstName": "Ann" }],
])
def test_generate_first_name_with_inner_boundaries(personList):
    generator = GenerateFirstName(personList)
    firstName = generator.generate()
    
    assert firstName == personList[0].get("firstName"), f"First name {expected} is not valid"
    