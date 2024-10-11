import random

def test_random_int():
    result = random.randint(1, 10)
    assert 1 <= result <= 10

def test_random_choice():
    choices = ['apple', 'banana', 'cherry']
    result = random.choice(choices)
    assert result in choices

def test_random_sample():
    population = list(range(10))
    sample = random.sample(population, 3)
    assert len(sample) == 3
    for item in sample:
        assert item in population