from sqlalchemy import Column, String
from src.models.database import Base


class PostalCode(Base):
    __tablename__ = "postal_code"
    cPostalCode: str = Column(String, primary_key=True, index=True, nullable=True)
    cTownName: str = Column(String)
    
    def as_dto(self) -> dict:
        return {
            "cPostalCode":self.cPostalCode,
            "cTownName":self.cTownName
        }