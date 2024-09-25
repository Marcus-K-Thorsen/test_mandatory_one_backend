from database import Session, get_db as get_db_session
from fastapi import APIRouter, Depends, HTTPException
from src.data.address import PostalCode

router: APIRouter = APIRouter()

def get_db():
    with get_db_session() as session:
        yield session

@router.get("/cpr")
def get_cpr(session: Session = Depends(get_db)):
    addresses = [address.as_dto() for address in session.query(PostalCode).all()]
    return {"data": addresses}
