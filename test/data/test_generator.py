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