import pytest
import os
import sys
from sqlalchemy import select, func
# Add the parent directory to the path to allow importing the generator module
# There must be a better way to import modules xD
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
from src.data.address import PostalCode

from database import get_db
def test_can_read_address():
    # Fetch random postal code and town name from the database
    with get_db() as session:
        stmt = select(PostalCode).order_by(func.rand()).limit(1)
        result = session.execute(stmt).scalar_one()
        postal_code_length = len(result.cPostalCode)
        is_postal_code_Digit = result.cPostalCode.isdigit()
        town_length = len(result.cTownName)
        assert postal_code_length == 4, "postalcode is not 4 numbers long"
        assert is_postal_code_Digit, "postal code is not digit"
        assert town_length > 0, "town name has to be at least 1"

import re
import pytest

# Validation Functions
def validate_first_name(name: str) -> None:
    """
    Validate the first name based on the rules:
    - Must consist of alphabetic Danish strings.
    - Can contain one space, one dot (at the end), or one hyphen.
    - Capital letters should only be used at the beginning, after a hyphen or space.
    """
    if not name:
        raise ValueError("First name cannot be empty.")

    # Updated regex for the valid first name pattern
    # Allows multiple parts separated by a hyphen or space and a dot at the end.
    pattern = r"^[A-ZÆØÅ][a-zæøå]*([ -][A-ZÆØÅ][a-zæøå]*)*\.?$"
    if not re.match(pattern, name):
        raise ValueError(f"Invalid first name: {name}")

def validate_last_name(name: str) -> None:
    """
    Validate the last name based on the rules:
    - Must consist of alphabetic Danish strings.
    - Capital letters should only be used at the start.
    """
    if not name:
        raise ValueError("Last name cannot be empty.")
    
    # Regex for the valid last name pattern
    pattern = r"^[A-ZÆØÅ][a-zæøå]*$"
    if not re.match(pattern, name):
        raise ValueError(f"Invalid last name: {name}")

# Test Functions using pytest

def test_validate_first_name_valid():
    """ Test valid first name cases """
    valid_names = ["Annemette P.", "Anne-Lise N.", "Børge B."]
    for name in valid_names:
        assert validate_first_name(name) is None  # No exception means success


def test_validate_first_name_invalid():
    """ Test invalid first name cases """
    invalid_names = ["", "Anne Lise ", "Anne..Lise", "@anne", "324543", "anne", "Anne-lise"]
    for name in invalid_names:
        with pytest.raises(ValueError):
            validate_first_name(name)


def test_validate_last_name_valid():
    """ Test valid last name cases """
    valid_names = ["Simonsen", "Christoffersen", "Kjær"]
    for name in valid_names:
        assert validate_last_name(name) is None  # No exception means success


def test_validate_last_name_invalid():
    """ Test invalid last name cases """
    invalid_names = ["", "Anne Lise ", "Anne..Lise", "Ann@", "324543", "anne"]
    for name in invalid_names:
        with pytest.raises(ValueError):
            validate_last_name(name)
