import random
import string
from database import Session
from data.address import PostalCode



def generate_birth_date() -> str:
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
    PHONE_PREFIXES = [
        "2", "30", "31", "40", "41", "42", "50", "51", "52", "53", "60", "61", "71", 
        "81", "91", "92", "93", "342", "344", "345", "346", "347", "348", "349", 
        "356", "357", "359", "362", "365", "366", "389", "398", "431", "441", 
        "462", "466", "468", "472", "474", "476", "478", "485", "486", "488", 
        "489", "493", "494", "495", "496", "498", "499", "542", "543", "545", 
        "551", "552", "556", "571", "572", "573", "574", "577", "579", "584", 
        "586", "587", "589", "597", "598", "627", "629", "641", "649", "658", 
        "662", "663", "664", "665", "667", "692", "693", "694", "697", "771", 
        "772", "782", "783", "785", "786", "788", "789", "826", "827", "829"]
    
    # Select a random phone prefix from the predefined list
    phone = random.choice(PHONE_PREFIXES)
    
    # Calculate the remaining length needed to complete 8 digits
    prefix_length = len(phone)
    for _ in range(8 - prefix_length):
        phone += str(random.randint(0, 9))  # Append random digits
        
    return phone

def generate_postal_code(session: Session) -> dict:
    """Fetch a random postal code and town name from the database."""
    # Using SQLAlchemy to select a random row from the addresses table
    postal_code: PostalCode = random.choice(session.query(PostalCode).all)
    return postal_code.as_dto

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