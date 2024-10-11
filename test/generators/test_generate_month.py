import pytest
from src.generators.generate_month import GenerateMonth


@pytest.mark.parametrize("monthRange, excepted", [
    (None, ValueError),                             # Decision 1                (monthRange is not provided)
    ("", ValueError),                               # Decision 2 and 3          (monthRange is provided and not a tuple)
    ((), ValueError),                               # Decision 4 and 5          (monthRange is a tuple and less than 2 values)
    (("2","2"), TypeError),                         # Decision 6 and 7          (monthRange is a tuple and contain 2 non-integers)
    ((0,1), ValueError),                            # Decision 8 and 9          (monthRange is a tuple, contain 2 integers, but the first value is less than 1)
    ((1,0), ValueError),                            # Decision 10 and 11        (monthRange is a tuple, contain 2 integers, but the second value is less than 1)
    ((13,1), ValueError),                           # Decision 12 and 13        (monthRange is a tuple, contain 2 integers, but the first value is greater than 12)
    ((1,13), ValueError),                           # Decision 14 and 15        (monthRange is a tuple, contain 2 integers, but the second value is greater than 12)
    ((1,1), 1),                                     # Decision 16 and 17        (monthRange is a tuple, contain 2 integers and the month range is valid)
])
def test_generate_month_with_decision_coverage(monthRange, excepted):
    if isinstance(excepted, int): 
        assert GenerateMonth(monthRange).generate() == excepted, f"Expected {monthRange[0]} to be a valid month"
    else: 
        with pytest.raises(excepted): GenerateMonth(monthRange), f"Expected {monthRange} to raise exception {excepted}"
      

@pytest.mark.parametrize("monthRange", [
    (1, 1),
    (2, 2),
    (3, 3),
])
def test_generate_month_with_valid_partitions(monthRange):
    generator = GenerateMonth(monthRange)
    month = generator.generate()
    
    assert month == monthRange[0], f"Expected {monthRange[0]} to be a valid month"
    

@pytest.mark.parametrize("monthRange, expected", [
    (None, ValueError),
    ("", ValueError),
    ((), ValueError),
    (("2","2"), TypeError),
    ((-1, -1), ValueError),
    ((0, 0), ValueError),
    ((0, 1), ValueError),
    ((1, 0), ValueError),
])
def test_generate_month_with_no_valid_partitions(monthRange, expected):
    with pytest.raises(expected):
        GenerateMonth(monthRange), f"Expected {monthRange} to be an invalid month"


@pytest.mark.parametrize("monthRange", [
    (1, 1),
    (1, 2),
    (1, 3),
])
def test_generate_month_with_inner_boundaries(monthRange):
    generator = GenerateMonth(monthRange)
    month = generator.generate()
    
    assert month <= monthRange[1] and month >= monthRange[0], f"Expected {month} to be inside the valid boundaries"
    

@pytest.mark.parametrize("monthRange", [
    (-1, 0),
    (0, 0),
    (0, 1),
])
def test_generate_month_with_outer_boundaries(monthRange):
    with pytest.raises(ValueError):
        GenerateMonth(monthRange), f"Expected {monthRange} to be outside the valid boundaries" 
        

