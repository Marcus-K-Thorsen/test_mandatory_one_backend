# Inspired by https://github.com/arturomorarioja/fake_info/blob/main/src/FakeInfo.php
import json
import random

# Load the data from the json file
with open('./src/data/person-names.json') as f:
    data = json.load(f)
    


class FakePerson:
    """
        FakePerson class is used to generate fake person data 
        for testing purposes.
    """
    
    def create():
        randomPerson = random.choice(data['persons'])
        return FakePerson(randomPerson=randomPerson)
    
    def __init__(self, randomPerson):
        """
            The constructor automatically generates
            the data when an instance of the class is created.
        """
        self.firstName = randomPerson['firstName']
        self.lastName = randomPerson['lastName']
        self.gender = randomPerson['gender']
        self.set_birth_date()
        self.set_cpr()
        self.set_address()
        self.set_phone_number()
        self.set_address()
        self.set_phone_number()

    def set_birth_date(self):
        """
            Set the birth date of the person.
        """
        # Get a random year between 1900 and 2021
        year = random.randint(1900, 2021)
        # Get a random month between 1 and 12
        month = random.randint(1, 12)
        # Get a random day depending on the month
        if month in [1, 3, 5, 7, 8, 10, 12]:
            day = random.randint(1, 31)
        elif month in [4, 6, 9, 11]:
            day = random.randint(1, 30)
        else:
            # Leap years are not taken into account
            # so as not to overcomplicate the code
            day = random.randint(1, 28)
        if len(str(month)) == 1:
            month = f"0{month}"
        if len(str(day)) == 1:
            day = f"0{day}"
        self.birthDate = f"{year}-{month}-{day}"

    def set_cpr(self):
        """
            Set the cpr of the person.
        """
        if not hasattr(self, 'birthDate'):
            raise Exception("Birth date must be set before generating CPR")
        if not hasattr(self, 'gender'):
            raise Exception("Gender must be set before generating CPR")

        # last digit must be even for females and odd for males
        last_digit = random.randint(0, 9)
        if self.gender == "male" and last_digit % 2 == 0:
            last_digit = (last_digit + 1) % 10
        elif self.gender == "female" and last_digit % 2 != 0:
            last_digit = (last_digit + 1) % 10

        # Get day as the 8th and 9th character of the birth date
        day = self.birthDate[8:10]
        # Get month as the 5th and 6th character of the birth date
        month = self.birthDate[5:7]
        # Get year as the 2nd and 3rd character of the birth date
        year = self.birthDate[2:4]
        # Format: DDMMYY-XXXX
        self.CPR = f"{day}{month}{year}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{last_digit}"

    def set_address(self):
        """
            Set the address of the person.
        """
        # the address variable must be named 'address'
        # to match how the frontend expects the data
        # https://github.com/arturomorarioja/js_fake_info_frontend/blob/main/js/script.js#L70-L76
        # Also, if you need help making the method generating the address,
        # look at: https://github.com/arturomorarioja/fake_info/blob/main/src/FakeInfo.php#L108-L162
        self.address = {
            "street": "Random street",
            "number": 1,
            "floor": 1,
            "door": "th",
            "postal_code": "2222",
            "town_name": "Random town name",
        }

    def set_phone_number(self):
        """
            Set the phone number of the person.
        """
        # the phone number variable must be named 'phoneNumber'
        # to match how the frontend expects the data
        # https://github.com/arturomorarioja/js_fake_info_frontend/blob/main/js/script.js#L79-L82
        # Also, if you need help making the method generating the phone number,
        # look at: https://github.com/arturomorarioja/fake_info/blob/main/src/FakeInfo.php#L196-L205
        PHONE_PREFIXES = [
        "2", "30", "31", "40", "41", "42", "50", "51", "52", "53", "60", "61", "71", 
        "81", "91", "92", "93", "342", "344", "345", "346", "347", "348", "349", 
        "356", "357", "359", "362", "365", "366", "389", "398", "431", "441", 
        "462", "466", "468", "472", "474", "476", "478", "485", "486", "488", 
        "489", "493", "494", "495", "496", "498", "499", "542", "543", "545", 
        "551", "552", "556", "571", "572", "573", "574", "577", "579", "584", 
        "586", "587", "589", "597", "598", "627", "629", "641", "649", "658", 
        "662", "663", "664", "665", "667", "692", "693", "694", "697", "771", 
        "772", "782", "783", "785", "786", "788", "789", "826", "827", "829"
    ]
    
        # Select a random phone prefix from the predefined list
        phone = random.choice(PHONE_PREFIXES)
    
        # Calculate the remaining length needed to complete 8 digits
        prefix_length = len(phone)
        for _ in range(8 - prefix_length):
            phone += str(random.randint(0, 9))  # Append random digits
    
        self.phone_number = phone

