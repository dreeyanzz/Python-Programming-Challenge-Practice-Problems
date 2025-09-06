import os

os.system("cls")


def is_palindrome(text: str) -> bool:

    # return False if argument is not an
    # instance of str
    if not isinstance(text, str):
        return False

    else:
        filtered = "".join(ch.lower() for ch in text if ch.isalnum())

    return filtered == filtered[::-1]


# Ask for user input
user_input: str = input("Type text to see if it is a palindrome: ")

# Evaluate user_input
isPalindrome: bool = is_palindrome(user_input)

# Check if isPalindrome
if isPalindrome:
    print(f"{user_input} is a palindrome")
else:
    print(f"{user_input} is not a palindrome")
