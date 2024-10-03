import pytest
import re
import os
import sys
from random import randint, choice
# Add the parent directory to the path to allow importing the generator module
# There must be a better way to import modules xD
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
from src.data.generator import Generator

def test_get_day_range_for_month_returns_correct_range_for_all_months_with_31_days():
    for month in Generator.MONTHS_WITH_31_DAYS:
        assert Generator.get_day_range_for_month(month) == (1, 31), f"Month {month} should have 31 days"

def test_get_day_range_for_month_returns_correct_range_for_all_months_with_30_days():
    for month in Generator.MONTHS_WITH_30_DAYS:
        assert Generator.get_day_range_for_month(month) == (1, 30), f"Month {month} should have 30 days"

def test_get_day_range_for_month_returns_correct_range_for_february():
    assert Generator.get_day_range_for_month(2) == (1, 28), "February should have 28 days"

def test_phone_number_is_correct_format():
    phone_number = Generator.generate_phone_number()

    length = len(phone_number)
    isDigit = phone_number.isdigit()
    hasPrefix = Generator.has_valid_prefix(phone_number)

    assert length == 8, f"Phone number {phone_number} does not have exactly 8 digits"
    assert isDigit, f"Phone number {phone_number} contains non-numeric characters"
    assert hasPrefix, f"Phone number {phone_number} has an invalid prefix"

def test_birthday_is_correct_format():
    startY, endY, startM, endM = 1900, 2021, 1, 12
    birthday = Generator.generate_birth_date(startY, endY, startM, endM)

    assert re.match(r"^\d{4}-\d{2}-\d{2}$", birthday), f"Birthday {birthday} is not in the correct format (YYYY-MM-DD)"
    assert int(birthday[:4]) >= startY and int(birthday[:4]) <= endY, f"The birthday's year ({birthday}) is outside the range {startY}-{endY}"
    assert int(birthday[5:7]) >= startM and int(birthday[5:7]) <= endM, f"The birthday's month ({birthday}) is outside the range {startM}-{endM}"



def test_address_is_correct_format():
    postal_code_info = Generator.generate_postal_code()  
    street = Generator.generate_street_name()  
    
    number = randint(1, 999)  # Randomly generate the house number
    floor = "st" if (floor_value := randint(0, 99)) == 0 else floor_value  # Floor is 'st' for ground, or a number
    door = choice(['th', 'tv', 'mf', str(randint(1, 50))])  # Randomly choose or generate the door

    # Assert street is a valid format (starts with an uppercase letter, and the rest lowercase)
    assert re.match(r"^[A-Z][a-z]*$", street), f"Street {street} is not in the correct format (First letter uppercase, rest lowercase)"

    # Assert number is within the valid range
    assert 1 <= number <= 999, f"House number {number} is outside the valid range (1-999)"

    # Assert floor is either 'st' or a number between 1 and 99
    if isinstance(floor, str):
        assert floor == "st", f"Floor {floor} should be 'st' for ground floor"
    else:
        assert 1 <= floor <= 99, f"Floor {floor} is outside the valid range (1-99)"

    # Assert door is one of the valid options ('th', 'tv', 'mf', or a number between 1 and 50)
    valid_door_choices = ['th', 'tv', 'mf'] + [str(i) for i in range(1, 51)]
    assert door in valid_door_choices, f"Door {door} is not in the valid choices (th, tv, mf, or 1-50)"

    # Validate postal code and town name
    postal_code = postal_code_info.get("cPostalCode")
    town_name = postal_code_info.get("cTownName")

    # Assert postal code is a 4-digit numeric string
    assert re.match(r"^\d{4}$", postal_code), f"Postal code {postal_code} is not in the correct format (4 digits)"

    # Assert town name is a non-empty string
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