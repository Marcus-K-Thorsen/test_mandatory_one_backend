import pytest
import re
from src.generators.generate_cpr import GenerateCPR


# Use predictable ranges for testing
CPR_OPTIONS = {
    "last_three_digit_range": (1, 1),
    "male_last_digit_list": [3],
    "female_last_digit_list": [2]
}


@pytest.mark.parametrize("options, expected", [
    ({ "gender": "male", "date": { "day": 1, "month": 1, "year": 1 } }, "0101011113"),
    ({ "gender": "male", "date": { "day": 2, "month": 3, "year": 4 } }, "0203041113"),
    ({ "gender": "female", "date": { "day": 1, "month": 1, "year": 1 } }, "0101011112"),
    ({ "gender": "female", "date": { "day": 2, "month": 3, "year": 4 } }, "0203041112"),
])
def test_generate_cpr_with_valid_partitions(options, expected):
    generator = GenerateCPR(options["gender"], options["date"], CPR_OPTIONS)
    cpr = generator.generate()
    
    assert cpr == expected, f"Expected {expected} to be a valid CPR number"
    

@pytest.mark.parametrize("options, expected", [
    ({ "gender": "", "date": { "day": 1, "month": 1, "year": 1 } }, ValueError),
    ({ "gender": None, "date": { "day": 1, "month": 1, "year": 1 } }, ValueError),
    ({ "gender": "male", "date": { "day": 0, "month": 1, "year": 1 } }, ValueError),
    ({ "gender": "male", "date": { "day": 1, "month": 0, "year": 1 } }, ValueError),
    ({ "gender": "male", "date": { "day": 1, "month": 1, "year": 0 } }, ValueError),
    ({ "gender": "male", "date": { "day": None, "month": 1, "year": 0 } }, ValueError),
    ({ "gender": "male", "date": { "day": 1, "month": None, "year": 0 } }, ValueError),
    ({ "gender": "male", "date": { "day": 1, "month": 1, "year": None } }, ValueError),
    ({ "gender": "not_male_or_female", "date": { "day": 1, "month": 1, "year": 1 } }, ValueError),
])
def test_generate_cpr_with_no_valid_partitions(options, expected):
    with pytest.raises(expected):
        GenerateCPR(options["gender"], options["date"], CPR_OPTIONS), f"Expected {options} to be invalid"


@pytest.mark.parametrize("options, expected", [
    ({ "gender": "male", "date": { "day": 1, "month": 1, "year": 1 } }, "0101011113"),
    ({ "gender": "female", "date": { "day": 1, "month": 1, "year": 1 } }, "0101011112"),
    ({ "gender": "male", "date": { "day": 31, "month": 12, "year": 2000 } }, "3112001113"),
    ({ "gender": "female", "date": { "day": 31, "month": 12, "year": 2000 } }, "3112001112"),
])
def test_generate_cpr_with_inner_boundaries(options, expected):
    generator = GenerateCPR(options["gender"], options["date"], CPR_OPTIONS)
    cpr = generator.generate()
    
    assert cpr == expected, f"Expected {expected} to be inside the valid boundaries"
   

@pytest.mark.parametrize("options", [
    { "gender": "male", "date": { "day": 0, "month": 0, "year": 0 } },
    { "gender": "female", "date": { "day": 0, "month": 0, "year": 0 } },
    { "gender": "male", "date": { "day": 0, "month": 0, "year": 1 } },
    { "gender": "female", "date": { "day": 0, "month": 0, "year": 1 } },
    { "gender": "male", "date": { "day": 0, "month": 1, "year": 1 } },
    { "gender": "female", "date": { "day": 0, "month": 1, "year": 1 } },
    { "gender": "male", "date": { "day": 32, "month": 12, "year": 1 } },
    { "gender": "female", "date": { "day": 32, "month": 12, "year": 1 } },
    { "gender": "male", "date": { "day": 32, "month": 13, "year": 1 } },
    { "gender": "female", "date": { "day": 32, "month": 13, "year": 1 } },
])
def test_generate_cpr_with_outer_boundaries(options):
    with pytest.raises(ValueError):
        GenerateCPR(options["gender"], options["date"], CPR_OPTIONS), f"Expected {options} to be outside the valid boundaries"
     

    