# Inspired by https://github.com/arturomorarioja/fake_info/blob/main/src/FakeInfo.php
import json
import random
import string
from src.models.address import PostalCode
from src.models.database import get_db
from src.data.generator import Generator
from sqlalchemy import select, func
from random import randint, choice

# Load some random names from a json file
with open('./src/data/person-names.json', 'r', encoding='utf-8') as f:
    PERSON_NAMES = json.load(f)
    
# Get the list of people
PERSON_LIST = PERSON_NAMES['persons']


class FakePerson:
    """
        FakePerson class is used to generate fake person data 
        for testing purposes.
    """
    
    def create():
        return FakePerson(options={
            "personList": PERSON_LIST,
            "birthDaySettings": {
                "startYear": 1900,
                "endYear": 2021,
                "startMonth": 1,
                "endMonth": 12
            },
        })
    
    def __init__(self, options: dict = {}):
        """
            The constructor automatically generates
            the data when an instance of the class is created.
        """
        personList = options.get("personList", PERSON_LIST)
        startYear = options.get("birthDaySettings", {}).get("startYear", 1900)
        endYear = options.get("birthDaySettings", {}).get("endYear", 2021)
        startMonth = options.get("birthDaySettings", {}).get("startMonth", 1)
        endMonth = options.get("birthDaySettings", {}).get("endMonth", 12)
        
        self.firstName = Generator.generate_first_name(personList)
        self.lastName = Generator.generate_last_name(personList)
        self.gender = Generator.generate_gender(personList)
        self.birthDate = Generator.generate_birth_date(startYear, endYear, startMonth, endMonth)
        self.birthDay = self.birthDate[8:10]
        self.birthMonth = self.birthDate[5:7]
        self.birthYear = self.birthDate[:4]
        self.CPR = Generator.generate_cpr(self.birthDay, self.birthMonth, self.birthYear, self.gender)
        self.address = Generator.generate_address()
        self.phoneNumber = Generator.generate_phone_number()
