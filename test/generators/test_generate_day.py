import pytest
from src.generators.generate_day import GenerateDay


CONF = {
    # Ensure the day always return 1 for simplicity of the test
    "MONTH_31_RANGE": (1, 1),
    "MONTH_30_RANGE": (1, 1),
    "MONTH_28_RANGE": (1, 1),
    "MONTHS_WITH_31_DAYS": [1, 3, 5, 7, 8, 10, 12],
    "MONTHS_WITH_30_DAYS": [4, 6, 9, 11]
}


@pytest.mark.parametrize("month", [
    1, 2, 3,
    4, 5, 6,
    7, 8, 9,
    10, 11, 12
])
def test_generate_day_with_valid_partitions(month):
    generator = GenerateDay(month, CONF)
    day = generator.generate()
    
    assert day == 1, f"Expected {month} to be a valid month" 
    

@pytest.mark.parametrize("month, expected", [
    (None, ValueError),
    ("", ValueError),
    ([], ValueError),
    (0, ValueError),
    (13, ValueError),
])
def test_generate_day_with_no_valid_partitions(month, expected):
    with pytest.raises(expected):
        GenerateDay(month, CONF), f"Expected {month} to be an invalid month" 


@pytest.mark.parametrize("month", [
    1,
    2,
    11,
    12
])
def test_generate_day_with_inner_boundaries(month):
    generator = GenerateDay(month, CONF)
    day = generator.generate()
    
    assert day == 1, f"Expected {month} to be inside the valid boundaries"
    

@pytest.mark.parametrize("month", [
    -1,
    0,
    32,
    33
])
def test_generate_year_with_outer_boundaries(month):
    with pytest.raises(ValueError):
        GenerateDay(month, CONF), f"Expected {month} to be outside the valid boundaries" 
        

    