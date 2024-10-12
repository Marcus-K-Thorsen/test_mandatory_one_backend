import random

WORDS1 = ['Rosen', 'Skov', 'Kastanje', 'Sø', 'Eng']
WORDS2 = ['Vej', 'Gade', 'Allé', 'Boulevard', 'Stræde']

class GenerateStreetName:
    """Generate a random street number by combining two random selected words from two lists."""
    
    def __init__(self, word1_list: list = WORDS1, word2_list: list = WORDS2):
        if not word1_list: raise ValueError("word1_list is not provided.")
        if not isinstance(word1_list, list): raise TypeError("word1_list must be a list.")
        if not all(isinstance(i, str) for i in word1_list): raise TypeError("word1_list must contain only strings.")
        if not all(i.isalpha() for i in word1_list): raise ValueError("word1_list must contain only alphabetic characters.")
        
        if not word2_list: raise ValueError("word2_list is not provided.")
        if not isinstance(word2_list, list): raise TypeError("word2_list must be a list.")
        if not all(isinstance(i, str) for i in word2_list): raise TypeError("word2_list must contain only strings.")
        if not all(i.isalpha() for i in word2_list): raise ValueError("word2_list must contain only alphabetic characters.")
        
        self.word1_list = word1_list
        self.word2_list = word2_list
    
    def generate(self):
        word1 = random.choice(self.word1_list)
        word2 = random.choice(self.word2_list)

        return f"{word1} {word2}"

