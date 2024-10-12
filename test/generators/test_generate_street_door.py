import pytest
from src.generators.generate_street_door import GenerateStreetDoor


@pytest.mark.parametrize("doorNumberRange, doorTypes, expected", [
    ((1, 1), None, "1"),
    ((2, 2), None, "2"),
    (None, ["th"], "th"),
    (None, ["tv"], "tv"),
    (None, ["mf"], "mf"),
])
def test_generate_street_door_with_valid_partitions(doorNumberRange, doorTypes, expected):
    generator = GenerateStreetDoor(doorNumberRange, doorTypes)
    streetDoor = generator.generate()
    
    assert streetDoor == expected, f"Expected {expected} to be a valid street door number"
    

@pytest.mark.parametrize("doorNumberRange, doorTypes, expected", [
    ("", ["th"], TypeError),
    ((1, 1), "", TypeError),
    ((1), ["th"], TypeError),
    ((1, 1, 1), ["th"], ValueError),
    ((1, 1), [], ValueError),
    ((1, 1), [""], ValueError),
    ((2, 1), [""], ValueError),
])
def test_generate_street_door_with_no_valid_partitions(doorNumberRange, doorTypes, expected):
    with pytest.raises(expected):
        GenerateStreetDoor(doorNumberRange, doorTypes), f"Expected {doorNumberRange} or {doorTypes} to be invalid"


@pytest.mark.parametrize("doorNumberRange, doorTypes, expected", [
    (None, ["th"], ["th"]),
    ((1, 1), None, ["1"]),
    ((1, 1), ["th"], ["1", "th"]),
])
def test_generate_street_door_with_inner_boundaries(doorNumberRange, doorTypes, expected):
    generator = GenerateStreetDoor(doorNumberRange, doorTypes)
    streetDoor = generator.generate()
    
    assert streetDoor in expected, f"Expected {streetDoor} to be inside the valid boundaries"
    

@pytest.mark.parametrize("doorNumberRange, doorTypes, expected", [
    (None, None, ValueError),
    ((-1, -1), None, ValueError),
    (None, [], ValueError),
])
def test_generate_street_door_with_outer_boundaries(doorNumberRange, doorTypes, expected):
    with pytest.raises(expected):
        GenerateStreetDoor(doorNumberRange, doorTypes), f"Expected {doorNumberRange} or {doorTypes} to be outside the valid boundaries"
        

    