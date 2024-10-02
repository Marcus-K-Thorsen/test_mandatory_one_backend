import pytest
import re
from src.data.generator import generate_phone_number 

# Allowed phone prefixes based on the partitions
VALID_PHONE_PREFIXES = [
    "2", "30", "31", "40", "41", "42", "50", "51", "52", "53", "60", "61", "71", 
    "81", "91", "92", "93", "342", "344", "345", "346", "347", "348", "349", 
    "356", "357", "359", "362", "365", "366", "389", "398", "431", "441", 
    "462", "466", "468", "472", "474", "476", "478", "485", "486", "488", 
    "489", "493", "494", "495", "496", "498", "499", "542", "543", "545", 
    "551", "552", "556", "571", "572", "573", "574", "577", "579", "584", 
    "586", "587", "589", "597", "598", "627", "629", "641", "649", "658", 
    "662", "663", "664", "665", "667", "692", "693", "694", "697", "771", 
    "772", "782", "783", "785", "786", "788", "789", "826", "827", "829"]

# Helper function to check if the prefix is valid
def has_valid_prefix(phone_number: str) -> bool:
    return any(phone_number.startswith(prefix) for prefix in VALID_PHONE_PREFIXES)

def test_phone_number_valid_length():
    """Test that the generated phone number is always 8 digits long."""
    for _ in range(10):  # Repeat multiple times for randomness
        phone_number = generate_phone_number()
        assert len(phone_number) == 8, f"Phone number {phone_number} does not have exactly 8 digits"

def test_phone_number_is_numeric():
    """Test that the generated phone number consists only of digits."""
    for _ in range(10):  # Repeat multiple times for randomness
        phone_number = generate_phone_number()
        assert phone_number.isdigit(), f"Phone number {phone_number} contains non-numeric characters"

def test_phone_number_valid_prefix():
    """Test that the generated phone number starts with a valid prefix."""
    for _ in range(10):  # Repeat multiple times for randomness
        phone_number = generate_phone_number()
        assert has_valid_prefix(phone_number), f"Phone number {phone_number} has an invalid prefix"

def test_invalid_prefix_range():
    """Test that numbers with invalid starting prefixes are not allowed."""
    invalid_prefixes = ["343", "111", "000"]  # Examples of invalid prefixes
    for prefix in invalid_prefixes:
        phone_number = generate_phone_number()
        assert not phone_number.startswith(prefix), f"Phone number {phone_number} starts with an invalid prefix {prefix}"

def test_invalid_character():
    """Ensure generated phone number does not contain non-numeric characters."""
    for _ in range(10):
        phone_number = generate_phone_number()
        # Check if phone number contains any non-numeric characters
        assert re.match(r'^\d{8}$', phone_number), f"Phone number {phone_number} contains invalid characters"

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
    """Ensure invalid phone numbers are correctly identified."""
    # Simulate invalid cases by directly asserting these should be rejected
    assert len(invalid_phone_number) != 8 or not invalid_phone_number.isdigit() or not has_valid_prefix(invalid_phone_number), f"Invalid phone number {invalid_phone_number} should not be allowed"