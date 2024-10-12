import pytest
from src.generators.generate_street_number import GenerateStreetNumber


@pytest.mark.parametrize("streetNumberRange", [
    (1, 1),
    (2, 2),
    (3, 3),
])
def test_generate_street_number_with_valid_partitions(streetNumberRange):
    generator = GenerateStreetNumber(streetNumberRange)
    streetNumber = generator.generate()
    
    assert streetNumber == streetNumberRange[0], f"Expected {streetNumberRange[0]} to be a valid street number"
    

@pytest.mark.parametrize("streetNumberRange, expected", [
    (None, ValueError),
    ("", ValueError),
    ((), ValueError),
    ((1), TypeError),
    (("2","2"), TypeError),
    ((-1, -1), ValueError),
    ((0, -1), ValueError),
    ((-1, 0), ValueError),
    ((2, 1), ValueError),
])
def test_generate_street_number_with_no_valid_partitions(streetNumberRange, expected):
    with pytest.raises(expected):
        GenerateStreetNumber(streetNumberRange), f"Expected {streetNumberRange} to be an invalid street number"


@pytest.mark.parametrize("streetNumberRange", [
    (1, 1),
    (1, 2),
    (1, 3),
])
def test_generate_street_number_with_inner_boundaries(streetNumberRange):
    generator = GenerateStreetNumber(streetNumberRange)
    streetNumber = generator.generate()
    
    assert streetNumber <= streetNumberRange[1] and streetNumber >= streetNumberRange[0], f"Expected {streetNumberRange} to be inside the valid boundaries"
    

@pytest.mark.parametrize("streetNumberRange", [
    (-1, -2),
    (-1, -1),
    (-1, 0),
])
def test_generate_street_number_with_outer_boundaries(streetNumberRange):
    with pytest.raises(ValueError):
        GenerateStreetNumber(streetNumberRange), f"Expected {streetNumberRange} to be outside the valid boundaries" 
        

    