import pytest
from src.generators.generate_town_name import GenerateTownName


@pytest.mark.parametrize("townNameList, expected", [
    (['København'], "København"),
    (['Århus'], "Århus"),
    (['Ålborg'], "Ålborg"),
    (['Ålbæk'], "Ålbæk"),
    (['Århus'], "Århus"),
    (['København K'], "København K"),
    (['København NV'], "København NV"),
    (['Lem St.' ], "Lem St."),
    (['Holme-Olstrup'], "Holme-Olstrup"),
    (['Nørre Aaby'], "Nørre Aaby"),
])
def test_generate_town_name_with_valid_partitions(townNameList, expected):
    generator = GenerateTownName(townNameList)
    townName = generator.generate()
    
    assert townName == expected, f"Expected {expected} to be a valid town name"
 

@pytest.mark.parametrize("townNameList, expected", [
    (None, ValueError),
    ("", ValueError),
    (2, TypeError),
    ([], ValueError),
    ([""], ValueError),
    (["a"], ValueError),
    (["123"], ValueError),
    (["12345"], ValueError),
    (["1a1a"], ValueError),
    (["@#$%"], ValueError),
])
def test_generate_town_name_with_no_valid_partitions(townNameList, expected):
    with pytest.raises(expected):
        GenerateTownName(townNameList), f"Expected {townNameList} to be invalid"


@pytest.mark.parametrize("townNameList, expected", [
    (['A'], "A"),
    (['Aa'], "Aa"),
    (['Aaa'], "Aaa"),
    (['Æ'], "Æ"),
    (['Æø'], "Æø"),
    (['Æøå'], "Æøå"),
])
def test_generate_town_name_with_inner_boundaries(townNameList, expected):
    generator = GenerateTownName(townNameList)
    townName = generator.generate()
    
    assert townName in expected, f"Expected {townName} to be inside the valid boundaries"
    

@pytest.mark.parametrize("townNameList, expected", [
    ([], ValueError),
    ([''], ValueError),
    (['a'], ValueError),
    (['å'], ValueError),
])
def test_generate_town_name_with_outer_boundaries(townNameList, expected):
    with pytest.raises(expected):
        GenerateTownName(townNameList), f"Expected {townNameList} to be outside the valid boundaries"
