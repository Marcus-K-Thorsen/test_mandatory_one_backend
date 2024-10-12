import pytest
from sqlalchemy import select, func
from src.models.address import PostalCode
from src.models.database import get_db

def test_connect_to_database():
    with get_db() as session:
        assert session is not None, "Cannot connect to database"
        
def test_read_town_name():
    with get_db() as session:
        stmt = select(PostalCode).order_by(func.rand()).limit(1)
        result = session.execute(stmt).scalar_one()
        assert len(result.cTownName) > 0, "Town name is empty"
        
def test_read_postal_code():
    with get_db() as session:
        stmt = select(PostalCode).order_by(func.rand()).limit(1)
        result = session.execute(stmt).scalar_one()
        assert len(result.cPostalCode) == 4, "Postal code is not 4 characters long"
        assert result.cPostalCode.isdigit(), "Postal code is not a digit"

def test_read_postal_code_and_town_name():
    with get_db() as session:
        stmt = select(PostalCode).order_by(func.rand()).limit(1)
        result = session.execute(stmt).scalar_one()
        assert len(result.cPostalCode) == 4, "Postal code is not 4 characters long"
        assert result.cPostalCode.isdigit(), "Postal code is not a digit"
        assert len(result.cTownName) > 0, "Town name is empty"
