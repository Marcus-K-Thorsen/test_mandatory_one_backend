import pytest
from src.generators.generate_year import GenerateYear


@pytest.mark.parametrize("yearRange, excepted", [
    (None, ValueError),                             # Decision 1                (yearRange is not provided)
    ("", ValueError),                               # Decision 2 and 3          (yearRange is provided and not a tuple)
    ((), ValueError),                               # Decision 4 and 5          (yearRange is a tuple and less than 2 values)
    (("2","2"), TypeError),                         # Decision 6 and 7          (yearRange is a tuple and contain 2 non-integers)
    ((0,1), ValueError),                            # Decision 8 and 9          (yearRange is a tuple, contain 2 integers, but the first value is less than 1)
    ((1,0), ValueError),                            # Decision 10 and 11        (yearRange is a tuple, contain 2 integers, but the second value is less than 1)
    ((1,1), 1),                                     # Decision 12 and 13        (yearRange is a tuple, contain 2 integers and the year range is valid)
])
def test_generate_year_with_decision_coverage(yearRange, excepted):
    if isinstance(excepted, int): 
        assert GenerateYear(yearRange).generate() == excepted, f"Expected {yearRange[0]} to be a valid year"
    else: 
        with pytest.raises(excepted): GenerateYear(yearRange), f"Expected {yearRange} to raise exception {excepted}"
      

@pytest.mark.parametrize("yearRange", [
    (1, 1),
    (2, 2),
    (3, 3),
])
def test_generate_year_with_valid_partitions(yearRange):
    generator = GenerateYear(yearRange)
    year = generator.generate()
    
    assert year == yearRange[0], f"Expected {yearRange[0]} to be a valid year" 
    

@pytest.mark.parametrize("yearRange, expected", [
    (None, ValueError),
    ("", ValueError),
    ((), ValueError),
    (("2","2"), TypeError),
    ((-1, -1), ValueError),
    ((0, 0), ValueError),
    ((0, 1), ValueError),
    ((1, 0), ValueError),
])
def test_generate_year_with_no_valid_partitions(yearRange, expected):
    with pytest.raises(expected):
        GenerateYear(yearRange), f"Expected {yearRange} to be an invalid year" 


@pytest.mark.parametrize("yearRange", [
    (1, 1),
    (1, 2),
    (1, 3),
])
def test_generate_year_with_inner_boundaries(yearRange):
    generator = GenerateYear(yearRange)
    year = generator.generate()
    
    assert year <= yearRange[1] and year >= yearRange[0], f"Expected {year} to be inside the valid boundaries"
    

@pytest.mark.parametrize("yearRange", [
    (-1, 0),
    (0, 0),
    (0, 1),
])
def test_generate_year_with_outer_boundaries(yearRange):
    with pytest.raises(ValueError):
        GenerateYear(yearRange), f"Expected {yearRange} to be outside the valid boundaries" 
        

    