import os
import re
import sys

os.system("cls")


roman_map: dict[str, int] = {
    "M": 1000,
    "CM": 900,
    "D": 500,
    "CD": 400,
    "C": 100,
    "XC": 90,
    "L": 50,
    "XL": 40,
    "X": 10,
    "IX": 9,
    "V": 5,
    "IV": 4,
    "I": 1,
}

roman_pattern = re.compile(
    r"^M{0,3}" r"(CM|CD|D?C{0,3})" r"(XC|XL|L?X{0,3})" r"(IX|IV|V?I{0,3})$"
)


def is_roman_valid(roman: str) -> bool:
    return bool(roman_pattern.match(roman))


def roman_to_decimal(roman: str) -> int:
    decimal: int = 0

    for key, value in roman_map.items():
        while roman.startswith(key):
            decimal += value
            roman = roman.removeprefix(key)

    return decimal


# Ask for user input
user_input: str = input("Input a roman numeral to turn into decimal: ")

# Evaluate if roman is valid
is_valid: bool = is_roman_valid(user_input)

if not is_valid:
    print("Invalid roman numeral")
    sys.exit()

# Convert roman numeral to decimal
decimal: int = roman_to_decimal(user_input)

# Print roman numeral
# Print decimal
print(f"Roman numeral: {user_input}")
print(f"Decimal: {decimal}")
