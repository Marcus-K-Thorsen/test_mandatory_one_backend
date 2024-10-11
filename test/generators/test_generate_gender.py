import pytest
from src.generators.generate_gender import GenerateGender


@pytest.mark.parametrize("genderList, excepted", [
    (None, ValueError),                             # Decision 1                (genderList is not provided)
    ({}, ValueError),                               # Decision 2 and 3          (genderList is provided and not a list)
    ([], ValueError),                               # Decision 4 and 5          (genderList is a list and empty)
    ([""], TypeError),                              # Decision 6 and 7          (genderList is a list and does not contain dictionaries)
    ([{None: "male"}], ValueError),                 # Decision 8 and 9          (genderList is a list, contain dicts, but the keys are not strings)
    ([{"wrongKey": None}], ValueError),             # Decision 10 and 11        (genderList is a list, contain dicts, keys are strings but values are not)
    ([{ "wrongKey": "male" }], ValueError),         # Decision 12 and 13        (genderList is a list, contain dicts, are strings, but the key is not "gender")
    ([{ "gender": "" }], ValueError),               # Decision 14 and 15        (genderList is a list, contain dicts, are strings, key is "gender", but value does not follow regex)
    ([{ "gender": "male" }], "male"),               # Decision 16               (genderList is a list, contain dicts, are strings, key is "gender", value follows regex)
])
def test_generate_first_name_with_decision_coverage(genderList, excepted):
    if isinstance(excepted, str): 
        assert GenerateGender(genderList).generate() == excepted, f"Expected {genderList[0].get('gender')} to be a valid gender"
    else: 
        with pytest.raises(excepted): GenerateGender(genderList), f"Expected {genderList} to raise exception {excepted}"


@pytest.mark.parametrize("genderList", [
    [{ "gender": "male" }],
    [{ "gender": "female" }],
    [{ "gender": "masculus" }],
    [{ "gender": "femina" }],
])
def test_generate_gender_with_valid_partitions(genderList):
    generator = GenerateGender(genderList)
    gender = generator.generate()
    
    assert gender == genderList[0].get("gender"), f"Expected {genderList[0].get('gender')} to be a valid gender"
    

@pytest.mark.parametrize("genderList, expected", [
    ([{ "gender": "" }], ValueError), 
    ([{ "": "male" }], ValueError), 
    ([{ "wrongKey": "male" }], ValueError),
    ([{ None: "male" }], ValueError),
    ([{ "gender": None }], TypeError),
])
def test_generate_gender_with_no_valid_partitions(genderList, expected):
    with pytest.raises(expected):
        GenerateGender(genderList), f"Expected {personList[0].get('gender')} to be an invalid gender"


@pytest.mark.parametrize("genderList", [
    [{ "gender": "m" }],
    [{ "gender": "ma" }],
    [{ "gender": "mal" }],
])
def test_generate_gender_with_inner_boundaries(genderList):
    generator = GenerateGender(genderList)
    gender = generator.generate()
    
    assert gender == genderList[0].get("gender"), f"Expected {genderList[0].get('gender')} to be inside the valid boundaries"
    

@pytest.mark.parametrize("genderList", [
    [{ "gend": "" }],
    [{ "gende": "" }],
    [{ "gender": "" }],
])
def test_generate_gender_with_outer_boundaries(genderList):
    with pytest.raises(ValueError):
        GenerateGender(genderList), f"Expected {genderList[0].get('gender')} to be outside the valid boundaries"
        

