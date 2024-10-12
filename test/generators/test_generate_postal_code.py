import pytest
from src.generators.generate_postal_code import GeneratePostalCode


@pytest.mark.parametrize("postalCodeList, expected", [
    (['1234'], "1234"),
    (['1111'], "1111"),
    (['2222'], "2222"),
    (['3333'], "3333"),
])
def test_generate_postal_code_with_valid_partitions(postalCodeList, expected):
    generator = GeneratePostalCode(postalCodeList)
    postalCode = generator.generate()
    
    assert postalCode == expected, f"Expected {expected} to be a valid postal code"
 

@pytest.mark.parametrize("postalCodeList, expected", [
    (None, ValueError),
    ("", ValueError),
    ([], ValueError),
    ([""], ValueError),
    (["123"], ValueError),
    (["12345"], ValueError),
    (["aaaa"], ValueError),
    (["1a1a"], ValueError),
    (["@#$%"], ValueError),
])
def test_generate_postal_code_with_no_valid_partitions(postalCodeList, expected):
    with pytest.raises(expected):
        GeneratePostalCode(postalCodeList), f"Expected {postalCodeList} to be invalid"


@pytest.mark.parametrize("postalCodeList, expected", [
    (['0000'], "0000"),
    (['0001'], "0001"),
    (['0002'], "0002"),
])
def test_generate_postal_code_with_inner_boundaries(postalCodeList, expected):
    generator = GeneratePostalCode(postalCodeList)
    postalCode = generator.generate()
    
    assert postalCode in expected, f"Expected {postalCode} to be inside the valid boundaries"
    

@pytest.mark.parametrize("postalCodeList, expected", [
    (['0'], ValueError),
    (['00'], ValueError),
    (['000'], ValueError),
])
def test_generate_postal_code_with_outer_boundaries(postalCodeList, expected):
    with pytest.raises(expected):
        GeneratePostalCode(postalCodeList), f"Expected {doorNumberRange} or {doorTypes} to be outside the valid boundaries"
