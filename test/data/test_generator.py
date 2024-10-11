import pytest
import re
from src.data.generator import Generator


@pytest.mark.parametrize("month_no, expected", [
    (1, (1, 31)), (2, (1, 28)),
    (3, (1, 31)), (4, (1, 30)),
    (5, (1, 31)), (6, (1, 30)),
    (7, (1, 31)), (8, (1, 31)),
    (9, (1, 30)), (10, (1, 31)),
    (11, (1, 30)), (12, (1, 31))
])
def test_get_day_range_for_month_returns_valid_range(month_no, expected):
    assert Generator.get_day_range_for_month(month_no) == expected, f"Month {month_no} should have {expected[1]} days"
    
    
@pytest.mark.parametrize("date_ranges, expected", [
    ({"startY": 1900, "endY": 1900, "startM": 1, "endM": 1}, "1900-01-01"),
    ({"startY": 1950, "endY": 1950, "startM": 1, "endM": 1}, "1950-01-01"),
    ({"startY": 2000, "endY": 2000, "startM": 1, "endM": 1}, "2000-01-01"),
])
def test_generate_birth_date_returns_correct_format(date_ranges, expected):
    birthDate = Generator.generate_birth_date(
        date_ranges["startY"], 
        date_ranges["endY"], 
        date_ranges["startM"], 
        date_ranges["endM"], 
        {
            "MONTHS_WITH_31_DAYS": [1, 3, 5, 7, 8, 10, 12],
            "MONTHS_WITH_30_DAYS": [4, 6, 9, 11],
            "MONTH_31_RANGE": (1, 1),
            "MONTH_30_RANGE": (1, 1),
            "MONTH_28_RANGE": (1, 1)
        }
    )
    assert birthDate == expected, f"Birthday {birthDate} is not in the correct format (YYYY-MM-DD)"
    
    
@pytest.mark.parametrize("date_ranges", [
    ({"startY": 1901, "endY": 1900, "startM": 1, "endM": 1}),
    ({"startY": 1900, "endY": 1900, "startM": 2, "endM": 1}),
    ({"startY": 0,    "endY": 2000, "startM": 1, "endM": 1}),
    ({"startY": 1900, "endY": 0,    "startM": 1, "endM": 1}),
    ({"startY": 1900, "endY": 2000, "startM": 0, "endM": 1}),
    ({"startY": 1900, "endY": 2000, "startM": 1, "endM": 0}),
])
def test_generate_birth_date_with_invalid_ranges(date_ranges):
    with pytest.raises(ValueError):
        assert Generator.generate_birth_date(
            date_ranges["startY"], 
            date_ranges["endY"], 
            date_ranges["startM"], 
            date_ranges["endM"], 
        ), f"Invalid date ranges {date_ranges} should not be allowed"
        
        
@pytest.mark.parametrize("date_ranges", [
    ({"startY": None, "endY": 2000, "startM": 1, "endM": 0}),
    ({"startY": 1900, "endY": None, "startM": 1, "endM": 0}),
    ({"startY": 1900, "endY": 2000, "startM": None, "endM": 0}),
    ({"startY": 1900, "endY": 2000, "startM": 1, "endM": None}),
])
def test_generate_birth_date_with_invalid_types(date_ranges):
    with pytest.raises(TypeError):
        assert Generator.generate_birth_date(
            date_ranges["startY"], 
            date_ranges["endY"], 
            date_ranges["startM"], 
            date_ranges["endM"], 
        ), f"Date ranges {date_ranges} must be integers"
    

def test_phone_number_is_correct_format():
    phone_number = Generator.generate_phone_number()

    length = len(phone_number)
    isDigit = phone_number.isdigit()
    hasPrefix = Generator.has_valid_prefix(phone_number)

    assert length == 8, f"Phone number {phone_number} does not have exactly 8 digits"
    assert isDigit, f"Phone number {phone_number} contains non-numeric characters"
    assert hasPrefix, f"Phone number {phone_number} has an invalid prefix"

def test_street_is_correct_format():
     # Arrange
    street = Generator.generate_street_name()
    
    # Act & Assert
    assert re.match(r"^[A-Z][a-z]*$", street), f"Street {street} is not in the correct format (First letter uppercase, rest lowercase)"
 
 
def test_postal_code_is_correct_format():
    # Arrange
    postal_code_info = Generator.generate_postal_code()
    print(postal_code_info)
    
    postal_code = postal_code_info.get("cPostalCode")

    # Act & Assert
    assert re.match(r"^\d{4}$", postal_code), f"Postal code {postal_code} is not in the correct format (4 digits)"


def test_town_name_is_valid():
    # Arrange
    postal_code_info = Generator.generate_postal_code()
    town_name = postal_code_info.get("cTownName")

    # Act & Assert
    assert isinstance(town_name, str) and len(town_name) > 0, f"Town name {town_name} is not valid"

#def test_is_cpr_valid():
    #cpr = Generator.generate_cpr("01", "01", "200

"""
# Test invalid cases (these can be expanded if the function is extended to handle more input cases)
@pytest.mark.parametrize("invalid_phone_number", [
    "1234567",   # 7 digits (too short)
    "123456789", # 9 digits (too long)
    "12345abc",  # Non-numeric characters
    "",          # Empty string
    "12345678",  # Invalid prefix
    "34345678",  # Invalid prefix within a restricted range
    "11123456"   # Another invalid prefix
])
def test_invalid_phone_numbers(invalid_phone_number):
    # Simulate invalid cases by directly asserting these should be rejected
    assert len(invalid_phone_number) != 8 or not invalid_phone_number.isdigit() or not has_valid_prefix(invalid_phone_number), f"Invalid phone number {invalid_phone_number} should not be allowed"

"""