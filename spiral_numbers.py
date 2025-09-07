import os

os.system("cls")


def generate_spiral(size: int) -> list[list[int]]:

    spiral: list[list[int]] = [[0] * size for _ in range(size)]

    number: int = 1

    top, bottom = 0, size - 1
    left, right = 0, size - 1

    while top <= bottom and left <= right:

        # Fill top row
        for i in range(left, right + 1):
            spiral[top][i] = number
            number += 1
        top += 1

        # Fill right column
        for i in range(top, bottom + 1):
            spiral[i][right] = number
            number += 1
        right -= 1

        # Fill bottom row
        if top <= bottom:
            for i in range(right, left - 1, -1):
                spiral[bottom][i] = number
                number += 1
            bottom -= 1

        # Fill left column
        if left <= right:
            for i in range(bottom, top - 1, -1):
                spiral[i][left] = number
                number += 1
            left += 1

    return spiral


# Ask for user input
user_input: str = input("Enter the size of the spiral: ")

# Convert user input to decimal
size: int = int(user_input)

spiral: list[list[int]] = generate_spiral(size)

# Display Spiral
for x in spiral:
    print(x)
