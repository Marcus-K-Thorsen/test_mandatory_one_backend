import pytest
import re
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

