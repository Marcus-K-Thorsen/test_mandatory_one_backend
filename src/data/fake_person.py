# Inspired by https://github.com/arturomorarioja/fake_info/blob/main/src/FakeInfo.php
import json
import random
import string
from sqlalchemy import select, func
from random import randint, choice
from src.models.address import PostalCode
from src.models.database import get_db
from src.data.generator import Generator

from src.generators.generate_first_name import GenerateFirstName
from src.generators.generate_last_name import GenerateLastName
from src.generators.generate_gender import GenerateGender
from src.generators.generate_birthdate import GenerateBirthdate


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
                "yearRange": (1900, 2024),
                "monthRange": (1, 12),
            },
        })
    
    def __init__(self, options: dict = {}):
        """
            The constructor automatically generates
            the data when an instance of the class is created.
        """
        personList = options.get("personList", PERSON_LIST)
        yearRange = options.get("birthDaySettings", {}).get("yearRange", (1900, 2024))
        monthRange = options.get("birthDaySettings", {}).get("monthRange", (1, 12))
        
        self.firstName = GenerateFirstName(personList).generate()
        self.lastName = GenerateLastName(personList).generate()
        self.gender = GenerateGender(personList).generate()
        self.birthDate = GenerateBirthdate(yearRange, monthRange).generate()
        self.birthDay = self.birthDate[8:10]
        self.birthMonth = self.birthDate[5:7]
        self.birthYear = self.birthDate[:4]
        self.CPR = Generator.generate_cpr(self.birthDay, self.birthMonth, self.birthYear, self.gender)
        self.address = Generator.generate_address()
        self.phoneNumber = Generator.generate_phone_number()
