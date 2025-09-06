import os

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
    "XI": 9,
    "V": 5,
    "IV": 4,
    "I": 1,
}


def decimal_to_roman(decimal: int) -> str:
    roman: str = ""

    for key, value in roman_map.items():
        while decimal >= value:
            roman += key
            decimal -= value

    return roman


# Ask for user input
user_input = input("Put a decimal number to turn into roman numeral: ")

# Convert user input into decimal
decimal: int = int(user_input)

# Convert decimal into roman numeral
roman_numeral = decimal_to_roman(decimal)

# Print decimal
# Print roman numeral
print(f"Decimal: {decimal}")
print(f"Roman: {roman_numeral}")
