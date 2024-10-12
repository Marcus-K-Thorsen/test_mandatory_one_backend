import pytest
from src.generators.generate_street_name import GenerateStreetName


@pytest.mark.parametrize("wordList1, wordList2, expected", [
    (["hello"], ["world"], "hello world"),
    (["world"], ["hello"], "world hello"),
    (["street"], ["name"], "street name"),
])
def test_generate_street_name_with_valid_partitions(wordList1, wordList2, expected):
    generator = GenerateStreetName(wordList1, wordList2)
    streetName = generator.generate()
    
    assert streetName == expected, f"Expected {wordList1[0]} combined with {wordList2[0]} to be a valid street name"
    

@pytest.mark.parametrize("wordList1, wordList2, expected", [
    (None, ["world"], ValueError),
    (["hello"], None, ValueError),
    (None, None, ValueError),
    ("", ["world"], ValueError),
    (["hello"], "", ValueError),
    ("", "", ValueError),
    ((), ["world"], ValueError),
    (["hello"], (), ValueError),
])
def test_generate_street_name_with_no_valid_partitions(wordList1, wordList2, expected):
    with pytest.raises(expected):
        GenerateStreetName(wordList1, wordList2), f"Expected {wordList1} combined with {wordList2} to be invalid"


@pytest.mark.parametrize("wordList1, wordList2, expected", [
    (["h"], ["w"], "h w"),
    (["he"], ["wo"], "he wo"),
    (["hel"], ["wor"], "hel wor"),
])
def test_generate_street_name_with_inner_boundaries(wordList1, wordList2, expected):
    generator = GenerateStreetName(wordList1, wordList2)
    streetName = generator.generate()
    
    assert streetName == expected, f"Expected {wordList1[0]} combined with {wordList2[0]} to be inside the valid boundaries"
    

@pytest.mark.parametrize("wordList1, wordList2", [
    ([""], []),
    ([""], [""]),
    (["h"], [""]),
])
def test_generate_street_name_with_outer_boundaries(wordList1, wordList2):
    with pytest.raises(ValueError):
        GenerateStreetName(wordList1, wordList2), f"Expected {wordList1} combined with {wordList2} to be outside the valid boundaries"
        
