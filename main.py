from typing import Union, Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.generators.generate_person import GeneratePerson

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True, 
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/person")
def read_n_people(n: Optional[int] = None):
    if n is None:
        n = 1
    people = []
    for i in range(n):
        person = GeneratePerson.generate()
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
    return {"CPR": GeneratePerson.generate().CPR}

@app.get("/name-gender")
def read_name_and_gender():
    person = GeneratePerson.generate()
    return {"firstName": person.firstName, "lastName": person.lastName, "gender": person.gender}

@app.get("/name-gender-dob")
def read_name_and_gender_and_birthday():
    person = GeneratePerson.generate()
    return {"firstName": person.firstName, "lastName": person.lastName, "gender": person.gender, "birthDate": person.birthDate}

@app.get("/cpr-name-gender")
def read_cpr_name_and_gender():
    person = GeneratePerson.generate()
    return {"CPR": person.CPR, "firstName": person.firstName, "lastName": person.lastName, "gender": person.gender}

@app.get("/cpr-name-gender-dob")
def read_cpr_name_gender_birthdate():
    person = GeneratePerson.generate()
    return {"CPR": person.CPR, "firstName": person.firstName, "lastName": person.lastName, "gender": person.gender, "birthDate": person.birthDate}

@app.get("/address")
def read_address():
    person = GeneratePerson.generate()
    return {"address": person.address}

@app.get("/phone")
def read_phone():
    person = GeneratePerson.generate()
    return {"phoneNumber": person.phoneNumber}
