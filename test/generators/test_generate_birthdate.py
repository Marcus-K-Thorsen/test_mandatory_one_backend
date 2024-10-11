import pytest
from src.generators.generate_birthdate import GenerateBirthdate


DAY_CONF = {
    # Ensure the day always return 1 for simplicity of the test
    "MONTH_31_RANGE": (1, 1),
    "MONTH_30_RANGE": (1, 1),
    "MONTH_28_RANGE": (1, 1),
    "MONTHS_WITH_31_DAYS": [1, 3, 5, 7, 8, 10, 12],
    "MONTHS_WITH_30_DAYS": [4, 6, 9, 11]
}


@pytest.mark.parametrize("options, expected", [
    ({'yearRange': (1, 1), 'monthRange': (1, 1)}, "1-01-01"),
    ({'yearRange': (10, 10), 'monthRange': (1, 1)}, "10-01-01"),
    ({'yearRange': (100, 100), 'monthRange': (1, 1)}, "100-01-01"),
    ({'yearRange': (1000, 1000), 'monthRange': (1, 1)}, "1000-01-01"),
    ({'yearRange': (1000, 1000), 'monthRange': (5, 5)}, "1000-05-01"),
    ({'yearRange': (1000, 1000), 'monthRange': (10, 10)}, "1000-10-01"),
    ({'yearRange': (1000, 1000), 'monthRange': (11, 11)}, "1000-11-01"),
    ({'yearRange': (1000, 1000), 'monthRange': (12, 12)}, "1000-12-01"),
])
def test_generate_birthdate_with_valid_partitions(options, expected):
    generator = GenerateBirthdate(options['yearRange'], options['monthRange'], DAY_CONF)
    birthdate = generator.generate()
    
    assert birthdate == expected, f"Expected {expected} to be a valid birthdate" 
    

@pytest.mark.parametrize("options, expected", [
    ({'yearRange': None, 'monthRange': (1, 1)}, ValueError),
    ({'yearRange': "", 'monthRange': (1, 1)}, ValueError),
    ({'yearRange': (1, 1), 'monthRange': None}, ValueError),
    ({'yearRange': (1, 1), 'monthRange': ""}, ValueError),
    ({'yearRange': (0, 1), 'monthRange': (1, 1)}, ValueError),
    ({'yearRange': (1, 0), 'monthRange': (1, 1)}, ValueError),
    ({'yearRange': (1, 1), 'monthRange': (0, 1)}, ValueError),
    ({'yearRange': (1, 1), 'monthRange': (1, 0)}, ValueError),
    ({'yearRange': (1, 1), 'monthRange': (1, 13)}, ValueError),
    ({'yearRange': (1, 1), 'monthRange': (13, 1)}, ValueError),
])
def test_generate_birthdate_with_no_valid_partitions(options, expected):
    with pytest.raises(expected):
        GenerateBirthdate(options['yearRange'], options['monthRange'], DAY_CONF), f"Expected {month} to be an invalid month" 


@pytest.mark.parametrize("options, expected", [
    ({'yearRange': (1, 1), 'monthRange': (1, 1)}, "1-01-01"),
    ({'yearRange': (2, 2), 'monthRange': (2, 2)}, "2-02-01"),
    ({'yearRange': (3, 3), 'monthRange': (3, 3)}, "3-03-01"),
    ({'yearRange': (3, 3), 'monthRange': (11, 11)}, "3-11-01"),
    ({'yearRange': (3, 3), 'monthRange': (12, 12)}, "3-12-01"),
    ({'yearRange': (2000, 2000), 'monthRange': (1, 1)}, "2000-01-01"),
    ({'yearRange': (2000, 2000), 'monthRange': (2, 2)}, "2000-02-01"),
    ({'yearRange': (2000, 2000), 'monthRange': (3, 3)}, "2000-03-01"),
    ({'yearRange': (2000, 2000), 'monthRange': (11, 11)}, "2000-11-01"),
    ({'yearRange': (2000, 2000), 'monthRange': (12, 12)}, "2000-12-01"),
])
def test_generate_birthdate_with_inner_boundaries(options, expected):
    generator = GenerateBirthdate(options['yearRange'], options['monthRange'], DAY_CONF)
    birthdate = generator.generate()
    
    assert birthdate == expected, f"Expected {expected} to be inside the valid boundaries"


@pytest.mark.parametrize("options", [
    {'yearRange': (-1, 1), 'monthRange': (1, 1)},
    {'yearRange': (1, -1), 'monthRange': (1, 1)},
    {'yearRange': (1, 1), 'monthRange': (-1, 1)},
    {'yearRange': (1, 1), 'monthRange': (1, -1)},
    {'yearRange': (1, 1), 'monthRange': (1, 13)},
    {'yearRange': (1, 1), 'monthRange': (13, 1)},
])
def test_generate_birthdate_with_outer_boundaries(options):
    with pytest.raises(ValueError):
        GenerateBirthdate(options['yearRange'], options['monthRange'], DAY_CONF), f"Expected {options} to be outside the valid boundaries" 
     

    