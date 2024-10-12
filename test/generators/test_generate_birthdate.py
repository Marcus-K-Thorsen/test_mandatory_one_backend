import pytest
from src.generators.generate_birthdate import GenerateBirthdate

@pytest.mark.parametrize("options, expected", [
    ({'year': 1, 'month': 1, 'day': 1}, "0001-01-01"),
    ({'year': 10, 'month': 1, 'day': 1}, "0010-01-01"),
    ({'year': 100, 'month': 1, 'day': 1}, "0100-01-01"),
    ({'year': 1000, 'month': 1, 'day': 1}, "1000-01-01"),
    ({'year': 1000, 'month': 5, 'day': 1}, "1000-05-01"),
    ({'year': 1000, 'month': 10, 'day': 1}, "1000-10-01"),
    ({'year': 1000, 'month': 11, 'day': 1}, "1000-11-01"),
    ({'year': 1000, 'month': 12, 'day': 1}, "1000-12-01"),
])
def test_generate_birthdate_with_valid_partitions(options, expected):
    generator = GenerateBirthdate(options['year'], options['month'], options['day'])
    birthdate = generator.generate()
    
    assert birthdate == expected, f"Expected {expected} to be a valid birthdate" 
    

@pytest.mark.parametrize("options, expected", [
    ({'year': None, 'month': 1, 'day': 1}, ValueError),
    ({'year': "", 'month': 1, 'day': 1}, ValueError),
    ({'year': 1, 'month': None, 'day': 1}, ValueError),
    ({'year': 1, 'month': "", 'day': 1}, ValueError),
    ({'year': 1, 'month': 1, 'day': None}, ValueError),
    ({'year': 1, 'month': 1, 'day': ""}, ValueError),
    ({'year': 0, 'month': 1, 'day': 1}, ValueError),
    ({'year': 1, 'month': 0, 'day': 1}, ValueError),
    ({'year': 1, 'month': 1, 'day': 0}, ValueError),
    ({'year': 1, 'month': 1, 'day': 32}, ValueError),
    ({'year': 1, 'month': 2, 'day': 29}, ValueError),
    ({'year': 1, 'month': 4, 'day': 31}, ValueError),
    ({'year': 1, 'month': 6, 'day': 31}, ValueError),
    ({'year': 1, 'month': 9, 'day': 31}, ValueError),
    ({'year': 1, 'month': 11, 'day': 31}, ValueError),
])
def test_generate_birthdate_with_no_valid_partitions(options, expected):
    with pytest.raises(expected):
        GenerateBirthdate(options['year'], options['month'], options['day']), f"Expected {options} to be invalid"


@pytest.mark.parametrize("options, expected", [
    ({'year': 1, 'month': 1, 'day': 1}, "0001-01-01"),
    ({'year': 10, 'month': 1, 'day': 1}, "0010-01-01"),
    ({'year': 100, 'month': 1, 'day': 1}, "0100-01-01"),
    ({'year': 1000, 'month': 1, 'day': 1}, "1000-01-01"),
    ({'year': 1000, 'month': 5, 'day': 1}, "1000-05-01"),
    ({'year': 1000, 'month': 10, 'day': 1}, "1000-10-01"),
    ({'year': 1000, 'month': 11, 'day': 1}, "1000-11-01"),
    ({'year': 1000, 'month': 12, 'day': 1}, "1000-12-01"),
])
def test_generate_birthdate_with_inner_boundaries(options, expected):
    generator = GenerateBirthdate(options['year'], options['month'], options['day'])
    birthdate = generator.generate()
    
    assert birthdate == expected, f"Expected {expected} to be inside the valid boundaries"


@pytest.mark.parametrize("options, expected", [
    ({'year': -1, 'month': 1, 'day': 1}, ValueError),
    ({'year': 1, 'month': -1, 'day': 1}, ValueError),
    ({'year': 1, 'month': 1, 'day': -1}, ValueError),
    ({'year': 1, 'month': 1, 'day': 32}, ValueError),
    ({'year': 1, 'month': 2, 'day': 29}, ValueError),
    ({'year': 1, 'month': 4, 'day': 31}, ValueError),
    ({'year': 1, 'month': 6, 'day': 31}, ValueError),
    ({'year': 1, 'month': 9, 'day': 31}, ValueError),
    ({'year': 1, 'month': 11, 'day': 31}, ValueError),
])
def test_generate_birthdate_with_outer_boundaries(options, expected):
    with pytest.raises(expected):
        GenerateBirthdate(options['year'], options['month'], options['day']), f"Expected {options} to be outside the valid boundaries" 
     
