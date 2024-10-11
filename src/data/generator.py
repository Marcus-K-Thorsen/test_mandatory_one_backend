import random
import string
import re

from src.models.address import PostalCode
from src.models.database import Session
from src.models.database import get_db

VALID_PHONE_PREFIXES = [
    "2", "30", "31", "40", "41", "42", "50", "51", "52", "53", "60", "61", "71", 
    "81", "91", "92", "93", "342", "344", "345", "346", "347", "348", "349", 
    "356", "357", "359", "362", "365", "366", "389", "398", "431", "441", 
    "462", "466", "468", "472", "474", "476", "478", "485", "486", "488", 
    "489", "493", "494", "495", "496", "498", "499", "542", "543", "545", 
    "551", "552", "556", "571", "572", "573", "574", "577", "579", "584", 
    "586", "587", "589", "597", "598", "627", "629", "641", "649", "658", 
    "662", "663", "664", "665", "667", "692", "693", "694", "697", "771", 
    "772", "782", "783", "785", "786", "788", "789", "826", "827", "829"]

DATE_CONFIGURATION = {
    "MONTHS_WITH_31_DAYS": [1, 3, 5, 7, 8, 10, 12],
    "MONTHS_WITH_30_DAYS": [4, 6, 9, 11],
    "MONTH_31_RANGE": (1, 31),
    "MONTH_30_RANGE": (1, 30),
    "MONTH_28_RANGE": (1, 28)
}

class Generator:

    def get_day_range_for_month(month: int, dateConfiguration: dict = DATE_CONFIGURATION) -> str:
        """Get the range of days for a given month."""
        if month in dateConfiguration["MONTHS_WITH_31_DAYS"]:
            return dateConfiguration["MONTH_31_RANGE"]
        elif month in dateConfiguration["MONTHS_WITH_30_DAYS"]:
            return dateConfiguration["MONTH_30_RANGE"]
        else:
            # Leap years are not taken into account
            # so as not to overcomplicate the code
            return dateConfiguration["MONTH_28_RANGE"]

    def generate_random_day_for_month(month: int, dateConfiguration: dict = DATE_CONFIGURATION) -> str:
        """Generate a random day for a given month."""
        day_range = Generator.get_day_range_for_month(month, dateConfiguration)
        return random.randint(day_range[0], day_range[1])

    def generate_birth_date(startY: int, endY: int, startM: int, endM: int, dateConfiguration: dict = DATE_CONFIGURATION) -> str:
        if not isinstance(startY, int): raise TypeError(f"The input 'startY: {startY}' is of type: '{type(startY)}' when it needs to be an 'int'.")
        if not isinstance(endY, int): raise TypeError(f"The input 'endY: {endY}' is of type: '{type(endY)}' when it needs to be an 'int'.")
        if not isinstance(startM, int): raise TypeError(f"The input 'startM: {startM}' is of type: '{type(startM)}' when it needs to be an 'int'.")
        if not isinstance(endM, int): raise TypeError(f"The input 'endM: {endM}' is of type: '{type(endM)}' when it needs to be an 'int'.")
        
        if startY > endY: raise ValueError("The start year must be less than or equal to the end year.")
        if startM > endM: raise ValueError("The start month must be less than or equal to the end month.")
        
        if startY < 1: raise ValueError("The start year must be at least 1.")
        if startM < 1 or startM > 12: raise ValueError("The start month must be between 1 and 12.")
        
        if endM < 1 or endM > 12: raise ValueError("The end month must be between 1 and 12.")
        if endY < 1: raise ValueError("The end year must be at least 1.")
        
        # Generate a random year, month, and day
        year = random.randint(startY, endY)
        month = random.randint(startM, endM)
        day = Generator.generate_random_day_for_month(month, dateConfiguration)
        
        # Add leading zeros to month and day if needed
        if len(str(month)) == 1: month = f"0{month}"
        if len(str(day)) == 1: day = f"0{day}"

        return f'{year}-{month}-{day}'

    def generate_cpr(day: str, month: str, year: str, gender: str) -> str:
        # Checking that the given inputs are all strings
        if not isinstance(day, str):
            raise TypeError(f"The input 'day: {day}' is of type: '{type(day)}' when it needs to be a 'str'.")
        if not isinstance(month, str):
            raise TypeError(f"The input 'month: {month}' is of type: '{type(month)}' when it needs to be a 'str'.")
        if not isinstance(year, str):
            raise TypeError(f"The input 'year: {year}' is of type: '{type(year)}' when it needs to be a 'str'.")
        if not isinstance(gender, str):
            raise TypeError(f"The input 'gender: {gender}' is of type: '{type(gender)}' when it needs to be a 'str'.")
        
        # Checking that the given inputs are the right format
        if len(year) > 4 or len(year) < 3 or year[0] == "0" or not year.isdigit():
            raise ValueError(f"The input 'year: {year}' is not in the correct format.")
        
        if len(month) != 2 or not month.isdigit() or int(month) > 12:
            raise ValueError(f"The input 'month: {month}' is not in the correct format.")
        
        if len(day) != 2 or not day.isdigit() or int(day) < 1 or (month in ["01", "03", "05", "07", "08", "10", "12"] and int(day) > 31) or (month in ["04", "06", "09", "11"] and int(day) > 30) or (month == "02" and int(day) > 28):
            raise ValueError(f"The input 'day: {day}' is not in the correct format.")
        
        if gender not in ['male', 'female']:
            raise ValueError(f"The input 'gender: {gender}' is not in the correct format.")
        
        year = year[2:4]
        last_three_digits = f"{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}"
        if gender == "male":
            last_digit = random.choice([1, 3, 5, 7, 9])
        else:
            last_digit = random.choice([0, 2, 4, 6, 8])
        
        return f"{day}{month}{year}{last_three_digits}{last_digit}"

    def generate_phone_number() -> str:
        """Generate a random phone number with a valid prefix."""
        
        # Select a random phone prefix from the predefined list
        phone = random.choice(VALID_PHONE_PREFIXES)
        
        # Calculate the remaining length needed to complete 8 digits
        prefix_length = len(phone)
        for _ in range(8 - prefix_length):
            phone += str(random.randint(0, 9))  # Append random digits
            
        return phone

    def has_valid_prefix(phone_number: str) -> bool:
        """Check if a phone number has a valid prefix."""
        return any(phone_number.startswith(prefix) for prefix in VALID_PHONE_PREFIXES)

    def generate_postal_code() -> dict:
        """Fetch a random postal code and town name from the database."""
        with get_db() as session:
            postal_codes = session.query(PostalCode).all()
            if not postal_codes:  
                raise ValueError("No postal codes available in the database.")
            postal_code: PostalCode = random.choice(postal_codes)  
        return postal_code.as_dto()  

    def generate_street_name(max_length=6) -> str:
        """
        Generates a random street name containing only letters.
        The string will have a maximum of 6 letters, with the first letter capitalized.
        """
        # Ensure we get a string between 1 and max_length
        length = random.randint(1, max_length)
        
        # Generate random lowercase letters for the remaining part
        random_letters = ''.join(random.choices(string.ascii_lowercase, k=length - 1))
        
        # Return the street name with the first letter capitalized
        return random.choice(string.ascii_uppercase) + random_letters
    
    def generate_street_number() -> int:
        """Generate a random street number between 1 and 999."""
        return random.randint(1, 999)
    
    def generate_floor() -> str:
        """Generate a random floor number or 'st'."""
        floor = random.randint(0, 99)
        return "st" if floor == 0 else floor
    
    def generate_door() -> str:
        """Generate a random door number or type."""
        return random.choice(['th', 'tv', 'mf', str(random.randint(1, 50))])
    
    def generate_address() -> dict:
        """
        Set the address of the person, using a random postal code and town from the database.
        """
        postal_code_info = Generator.generate_postal_code()
        return {
            "street": Generator.generate_street_name(),
            "number": Generator.generate_street_number(),
            "floor": Generator.generate_floor(),
            "door": Generator.generate_door(),
            "postal_code": postal_code_info.get("cPostalCode"),
            "town_name": postal_code_info.get("cTownName"),
        }