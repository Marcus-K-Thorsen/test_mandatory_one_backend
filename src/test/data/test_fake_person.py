import pytest
import re
import os
import sys
# Add the parent directory to the path to allow importing the generator module
# There must be a better way to import modules xD
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
from src.data.fake_person import FakePerson

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

