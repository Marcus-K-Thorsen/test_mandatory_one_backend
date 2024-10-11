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

