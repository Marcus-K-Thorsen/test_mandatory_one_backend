import pytest
import re
import os
import sys
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