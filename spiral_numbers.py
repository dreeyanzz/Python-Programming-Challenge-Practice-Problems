import os

os.system("cls")


def generate_spiral(size: int):

    spiral = [[0] * size for _ in range(size)]
    num = 1
    top, bottom = 0, size - 1
    left, right = 0, size - 1

    while top <= bottom and left <= right:
        # Fill top row
        for i in range(left, right + 1):
            spiral[top][i] = num
            num += 1
        top += 1

        # Fill right column
        for i in range(top, bottom + 1):
            spiral[i][right] = num
            num += 1
        right -= 1

        # Fill bottom row
        if top <= bottom:
            for i in range(right, left - 1, -1):
                spiral[bottom][i] = num
                num += 1
            bottom -= 1

        # Fill left column
        if left <= right:
            for i in range(bottom, top - 1, -1):
                spiral[i][left] = num
                num += 1
            left += 1

    return spiral


# Ask for user input
user_input: str = input("Input the size of the matrix: ")

# Convert user input into decimal
size: int = int(user_input)

# Generate spiral and store it
spiral_number = generate_spiral(size)

# Print spiral
for row in spiral_number:
    print(row)
