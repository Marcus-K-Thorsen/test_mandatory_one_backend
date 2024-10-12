import pytest
from src.generators.generate_street_floor import GenerateStreetFloor


@pytest.mark.parametrize("floorRange, expected", [
    ((0, 0), "st"),
    ((1, 1), "1"),
    ((2, 2), "2"),
    ((3, 3), "3"),
])
def test_generate_street_floor_with_valid_partitions(floorRange, expected):
    generator = GenerateStreetFloor(floorRange)
    streetFloor = generator.generate()
    
    assert streetFloor == expected, f"Expected {floorRange} to be a valid street floor range"
    

@pytest.mark.parametrize("floorRange, expected", [
    (None, ValueError),
    ("", ValueError),
    ((), ValueError),
    (("2","2"), TypeError),
    ((-1, -1), ValueError),
    ((2, 1), ValueError),
])
def test_generate_street_floor_with_no_valid_partitions(floorRange, expected):
    with pytest.raises(expected):
        GenerateStreetFloor(floorRange), f"Expected {floorRange} to be an invalid street floor range"


@pytest.mark.parametrize("floorRange, expected", [
    ((0, 1), ["st", "1"]),
    ((0, 2), ["st", "1", "2"]),
    ((0, 3), ["st", "1", "2", "3"]),
])
def test_generate_street_floor_with_inner_boundaries(floorRange, expected):
    generator = GenerateStreetFloor(floorRange)
    streetFloor = generator.generate()
    
    assert streetFloor in expected, f"Expected {streetFloor} to be inside the valid boundaries"
    

@pytest.mark.parametrize("floorRange", [
    (-1, -2),
    (-1, -1),
    (-1, 0),
])
def test_generate_street_floor_with_outer_boundaries(floorRange):
    with pytest.raises(ValueError):
        GenerateStreetFloor(floorRange), f"Expected {floorRange} to be outside the valid boundaries" 
        
