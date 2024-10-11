from typing import Union, Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.data.fake_person import FakePerson

app = FastAPI()
# Setup cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True, 
    allow_methods=["*"],
    allow_headers=["*"],
)

# WHY THESE ENDPOINTS?
# Because the frontend expects them to be defined and to return the data
# in the format that can be seen in the FakePerson class.
# https://github.com/arturomorarioja/js_fake_info_frontend/blob/main/index.html#L29-L35

@app.get("/person")
def read_n_people(n: Optional[int] = None):
    if n is None:
        n = 1
    people = []
    for i in range(n):
        person = FakePerson.create()
        people.append({
            "CPR": person.CPR,
            "firstName": person.firstName,
            "lastName": person.lastName,
            "gender": person.gender,
            "birthDate": person.birthDate,
            "address": person.address,
            "phoneNumber": person.phoneNumber 
        })
    return people

@app.get("/cpr")
def read_cpr():
    person = FakePerson.create()
    return {"CPR": person.CPR}

@app.get("/name-gender")
def read_name_and_gender():
    person = FakePerson.create()
    return {"firstName": person.firstName, "lastName": person.lastName, "gender": person.gender}

@app.get("/name-gender-dob")
def read_name_and_gender_and_birthday():
    person = FakePerson.create()
    return {"firstName": person.firstName, "lastName": person.lastName, "gender": person.gender, "birthDate": person.birthDate}

@app.get("/cpr-name-gender")
def read_cpr_name_and_gender():
    person = FakePerson.create()
    return {"CPR": person.CPR, "firstName": person.firstName, "lastName": person.lastName, "gender": person.gender}

@app.get("/cpr-name-gender-dob")
def read_cpr_name_gender_birthdate():
    person = FakePerson.create()
    return {"CPR": person.CPR, "firstName": person.firstName, "lastName": person.lastName, "gender": person.gender, "birthDate": person.birthDate}

@app.get("/address")
def read_address():
    person = FakePerson.create()
    return {"address": person.address}

@app.get("/phone")
def read_phone():
    person = FakePerson.create()
    return {"phoneNumber": person.phoneNumber}
