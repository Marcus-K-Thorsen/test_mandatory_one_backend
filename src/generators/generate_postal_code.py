from src.models.address import PostalCode
from src.models.database import Session
from src.models.database import get_db
import random

class GeneratePostalCode:
    """Generate a postal code."""
        
    def generate(db=get_db(), model=PostalCode):
        with get_db() as session:
            data = session.query(model).all()
            
            if not data: raise ValueError("No postal codes available in the database.")
            postal_code: model = random.choice(data)
        return postal_code.as_dto().get("cPostalCode")