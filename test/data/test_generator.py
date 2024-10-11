import pytest
import re
from src.data.generator import Generator

def test_phone_number_is_correct_format():
    phone_number = Generator.generate_phone_number()

    length = len(phone_number)
    isDigit = phone_number.isdigit()
    hasPrefix = Generator.has_valid_prefix(phone_number)

    assert length == 8, f"Phone number {phone_number} does not have exactly 8 digits"
    assert isDigit, f"Phone number {phone_number} contains non-numeric characters"
    assert hasPrefix, f"Phone number {phone_number} has an invalid prefix"


@pytest.mark.parametrize("month_no, expected", [
    (1, (1, 31)), 
    (2, (1, 28)),
    (3, (1, 31)), 
    (4, (1, 30)),
    (5, (1, 31)), 
    (6, (1, 30)),
    (7, (1, 31)), 
    (8, (1, 31)),
    (9, (1, 30)), 
    (10, (1, 31)),
    (11, (1, 30)), 
    (12, (1, 31))
])
def test_get_day_range_for_month_returns_valid_range(month_no, expected):
    assert Generator.get_day_range_for_month(month_no) == expected, f"Month {month_no} should have {expected[1]} days"


@pytest.mark.parametrize("date_ranges, expected", [
    ({"startY": 1900, "endY": 2021, "startM": 1, "endM": 12}, r"^\d{4}-\d{2}-\d{2}$"),
    ({"startY": 1901, "endY": 2020, "startM": 2, "endM": 11}, r"^\d{4}-\d{2}-\d{2}$"),
])
def test_birthday_is_correct_format(date_ranges, expected):
    birthday = Generator.generate_birth_date(
        date_ranges["startY"], 
        date_ranges["endY"], 
        date_ranges["startM"], 
        date_ranges["endM"]
    )
    assert re.match(expected, birthday), f"Birthday {birthday} is not in the correct format (YYYY-MM-DD)"


@pytest.mark.parametrize("date_ranges", [
    ({"startY": 1900, "endY": 2021, "startM": 1, "endM": 12}), 
    ({"startY": 1901, "endY": 2020, "startM": 2, "endM": 11})
])
def test_birthday_is_within_range(date_ranges):
    birthday = Generator.generate_birth_date(
        date_ranges["startY"], 
        date_ranges["endY"], 
        date_ranges["startM"], 
        date_ranges["endM"]
    )
    
    generated_year = int(birthday[:4])
    generated_month = int(birthday[5:7])
    generated_day = int(birthday[8:10])
    
    assert generated_year >= date_ranges["startY"] and generated_year <= date_ranges["endY"], f"The birthday's year ({birthday}) is outside the range {date_ranges['startY']}-{date_ranges['endY']}"
    assert generated_month >= date_ranges["startM"] and generated_month <= date_ranges["endM"], f"The birthday's month ({birthday}) is outside the range {date_ranges['startM']}-{date_ranges['endM']}"
    assert generated_day >= 1 and generated_day <= 31, f"The birthday's day ({birthday}) is outside the range 1-31"

"""
@pytest.mark.parametrize("name", [
    "",
    "Anne Lise ",
    "Anne..Lise",
    "Ann@",
    "324543",
    "anne",
])
def test_validate_last_name_invalid(name):
    assert FakePerson.validate_last_name(name) == False

@pytest.mark.parametrize("name", [
    "Simonsen",
    "Christoffersen",
    "Kjær",
])
def test_validate_last_name_valid(name):
    assert FakePerson.validate_last_name(name) == True
"""


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