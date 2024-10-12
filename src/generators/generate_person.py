import random

from src.models.person import Person
from src.models.address import PostalCode
from src.models.database import get_db

from src.generators.generate_year import GenerateYear
from src.generators.generate_month import GenerateMonth
from src.generators.generate_day import GenerateDay
from src.generators.generate_first_name import GenerateFirstName
from src.generators.generate_last_name import GenerateLastName
from src.generators.generate_gender import GenerateGender
from src.generators.generate_birthdate import GenerateBirthdate
from src.generators.generate_cpr import GenerateCPR
from src.generators.generate_address import GenerateAddress
from src.generators.generate_phone_number import GeneratePhoneNumber

class GeneratePerson:
    """Generate a fake person data for testing purposes."""
    
    def __init__(self, options: dict = {}):
        """
            The constructor automatically generates
            the data when an instance of the class is created.
        """
        if not isinstance(options, dict): raise TypeError("options must be a dictionary.")
        
        # first name must be in the options
        if not "firstName" in options: raise ValueError("firstName is not provided.")
        if not isinstance(options["firstName"], str): raise TypeError("firstName must be a string.")
        
        # last name must be in the options
        if not "lastName" in options: raise ValueError("lastName is not provided.")
        if not isinstance(options["lastName"], str): raise TypeError("lastName must be a string.")
        
        # gender must be in the options
        if not "gender" in options: raise ValueError("gender is not provided.")
        if not isinstance(options["gender"], str): raise TypeError("gender must be a string.")
        
        # birthDate must be in the options
        if not "birthDate" in options: raise ValueError("birthDate is not provided.")
        if not isinstance(options["birthDate"], str): raise TypeError("birthDate must be a string.")
        
        # CPR must be in the options
        if not "CPR" in options: raise ValueError("CPR is not provided.")
        if not isinstance(options["CPR"], str): raise TypeError("CPR must be a string.")
        
        # address must be in the options
        if not "address" in options: raise ValueError("address is not provided.")
        if not isinstance(options["address"], GenerateAddress): raise TypeError("address must be a GenerateAddress.")
        
        # phoneNumber must be in the options
        if not "phoneNumber" in options: raise ValueError("phoneNumber is not provided.")
        if not isinstance(options["phoneNumber"], str): raise TypeError("phoneNumber must be a string.")
        
        self.firstName = options["firstName"]
        self.lastName = options["lastName"]
        self.gender = options["gender"]
        self.birthDate = options["birthDate"]
        self.CPR = options["CPR"]
        self.address = options["address"]
        self.phoneNumber = options["phoneNumber"]

    def generate():
        """Factory method to create a new FakePerson instance."""
        
        # Get all postal codes from the database
        with get_db() as session:
            postalCodeInstances = session.query(PostalCode).all()
        
        # Convert the postal code instances to a list of postal codes
        postalCodeList = [postalCodeInstance.cPostalCode for postalCodeInstance in postalCodeInstances]
        # Convert the postal code instances to a list of town names
        townNameList = [postalCodeInstance.cTownName for postalCodeInstance in postalCodeInstances]
        
        # Get a random person from the person-names.json file
        personList = [random.choice(Person.loadAll())]
        
        # Generate a random date
        year = GenerateYear((1900, 2024)).generate()
        month = GenerateMonth((1, 12)).generate()
        day = GenerateDay(month).generate()
        
        # Generate the person data
        firstName = GenerateFirstName(personList).generate()
        lastName = GenerateLastName(personList).generate()
        gender = GenerateGender(personList).generate()
        birthDate = GenerateBirthdate(year, month, day).generate()
        CPR = GenerateCPR(gender, {"day": day, "month": month, "year": year}).generate()
        phoneNumber = GeneratePhoneNumber().generate()
        address = GenerateAddress.generate(postalCodeList, townNameList)

        return GeneratePerson(options={
            "firstName": firstName,
            "lastName": lastName,
            "birthDate": birthDate,
            "CPR": CPR,
            "gender": gender,
            "address": address,
            "phoneNumber": phoneNumber
        })