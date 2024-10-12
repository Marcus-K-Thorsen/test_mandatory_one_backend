import pytest
from src.generators.generate_phone_number import GeneratePhoneNumber

@pytest.mark.parametrize("options, expected", [
    ({ "prefixes": ["45"], "randomDigitRange": (0, 0), "max_length": 8 }, "45000000"),
    ({ "prefixes": ["45"], "randomDigitRange": (0, 0), "max_length": 9 }, "450000000"),
    ({ "prefixes": ["4"], "randomDigitRange": (0, 0), "max_length": 8 }, "40000000"),
    ({ "prefixes": ["123"], "randomDigitRange": (0, 0), "max_length": 8 }, "12300000"),
    ({ "prefixes": ["123"], "randomDigitRange": (0, 0), "max_length": 9 }, "123000000"),
    ({ "prefixes": ["123"], "randomDigitRange": (0, 0), "max_length": 10 }, "1230000000"),
    ({ "prefixes": ["9"], "randomDigitRange": (1, 1), "max_length": 3 }, "911"),
])
def test_generate_phone_number_with_valid_partitions(options, expected):
    generator = GeneratePhoneNumber(options["prefixes"], options["randomDigitRange"], options["max_length"])
    phoneNumber = generator.generate()
    
    assert phoneNumber == expected, f"Expected {expected} to be a valid phone number"
 

@pytest.mark.parametrize("options, expected", [
    ({ "prefixes": None, "randomDigitRange": (0, 0), "max_length": 8 }, ValueError),
    ({ "prefixes": [], "randomDigitRange": (0, 0), "max_length": 8 }, ValueError),
    ({ "prefixes": [""], "randomDigitRange": (0, 0), "max_length": 8 }, ValueError),
    ({ "prefixes": ["a"], "randomDigitRange": (0, 0), "max_length": 8 }, ValueError),
    ({ "prefixes": ["å"], "randomDigitRange": (0, 0), "max_length": 8 }, ValueError),
    ({ "prefixes": ["45"], "randomDigitRange": None, "max_length": 8 }, ValueError),
    ({ "prefixes": ["45"], "randomDigitRange": [], "max_length": 8 }, ValueError),
    ({ "prefixes": ["45"], "randomDigitRange": ("0", "0"), "max_length": 8 }, TypeError),
    ({ "prefixes": ["45"], "randomDigitRange": (0, 0), "max_length": None }, ValueError),
    ({ "prefixes": ["45"], "randomDigitRange": (0, 0), "max_length": [] }, ValueError),
    ({ "prefixes": ["45"], "randomDigitRange": (0, 0), "max_length": "8" }, TypeError),
    ({ "prefixes": ["45"], "randomDigitRange": (0, 0), "max_length": 0 }, ValueError),
    ({ "prefixes": ["45"], "randomDigitRange": (0, 0), "max_length": -1 }, ValueError),
])
def test_generate_phone_number_with_no_valid_partitions(options, expected):
    with pytest.raises(expected):
        GeneratePhoneNumber(options["prefixes"], options["randomDigitRange"], options["max_length"]), f"Expected {options} to be invalid"


@pytest.mark.parametrize("options, expected", [
    ({ "prefixes": ["0"], "randomDigitRange": (0, 0), "max_length": 2 }, "000"),
    ({ "prefixes": ["1"], "randomDigitRange": (0, 0), "max_length": 2 }, "100"),
    ({ "prefixes": ["3"], "randomDigitRange": (0, 0), "max_length": 2 }, "300"),
])
def test_generate_phone_number_with_inner_boundaries(options, expected):
    generator = GeneratePhoneNumber(options["prefixes"], options["randomDigitRange"], options["max_length"])
    phoneNumber = generator.generate()
    
    assert phoneNumber in expected, f"Expected {phoneNumber} to be inside the valid boundaries"
 

@pytest.mark.parametrize("options, expected", [
    ({ "prefixes": None, "randomDigitRange": (0, 0), "max_length": 2 }, ValueError),
    ({ "prefixes": [], "randomDigitRange": (0, 0), "max_length": 2 }, ValueError),
    ({ "prefixes": [""], "randomDigitRange": (0, 0), "max_length": 2 }, ValueError),
])
def test_generate_phone_number_with_outer_boundaries(options, expected):
    with pytest.raises(expected):
        GeneratePhoneNumber(options["prefixes"], options["randomDigitRange"], options["max_length"]), f"Expected {options} to be outside the valid boundaries"
