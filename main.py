from typing import Union

from fastapi import FastAPI
from src.controllers.cpr_controller import router as CPR_Router

app = FastAPI()

app.include_router(CPR_Router)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}