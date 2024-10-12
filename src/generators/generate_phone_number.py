import random

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

class GeneratePhoneNumber:
    """Generate a postal code."""
    
    def __init__(self, prefixes: list = VALID_PHONE_PREFIXES, randomDigitRange: tuple = (0, 9), max_length: int = 8):
        if not prefixes: raise ValueError("prefixes is not provided.")
        if not isinstance(prefixes, list): raise TypeError("prefixes must be of type list.")
        if len(prefixes) == 0: raise ValueError("prefixes must contain at least one prefix.")
        if not all(isinstance(prefix, str) for prefix in prefixes): raise TypeError("prefixes must be a list of strings.")
        if not all(prefix for prefix in prefixes): raise ValueError("The prefix must not be empty.")
        if not all(prefix.isdigit() for prefix in prefixes): raise ValueError("The prefix must consist of digits only.")
        
        if not randomDigitRange: raise ValueError("randomDigitRange is not provided.")
        if not isinstance(randomDigitRange, tuple): raise TypeError("randomDigitRange must be of type tuple.")
        if len(randomDigitRange) != 2: raise ValueError("randomDigitRange must contain two elements.")
        if not all(isinstance(i, int) for i in randomDigitRange): raise TypeError("randomDigitRange must contain only integers.")
        if not all(0 <= i <= 9 for i in randomDigitRange): raise ValueError("randomDigitRange must contain only integers between 0 and 9.")
        
        if not max_length: raise ValueError("max_length is not provided.")
        if not isinstance(max_length, int): raise TypeError("max_length must be of type int.")
        if max_length < 2: raise ValueError("max_length must be greater than 1.")
        
        self.prefixes = prefixes
        self.randomDigitRange = randomDigitRange
        self.max_length = max_length
        
    def generate(self):
        randomPrefix = random.choice(self.prefixes)
        randomPrefixSubMax = self.max_length - len(randomPrefix)
        
        phoneNumber = randomPrefix
        for i in range(randomPrefixSubMax):
            randomDigit = random.randint(self.randomDigitRange[0], self.randomDigitRange[1])
            phoneNumber += str(randomDigit)
        
        return phoneNumber
        
    