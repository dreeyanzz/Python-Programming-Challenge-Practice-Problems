import os

# Clear the terminal
os.system("clear")


def flatten_list(data: any) -> list[any]:
    flattened_list = []

    if isinstance(data, list):
        for element in data:
            flattened_list += flatten_list(element)
    else:
        flattened_list.append(data)

    return flattened_list


thisList: list[any] = [[1, 2], [3, [4, 5]], [6]]
flattened: list[any] = flatten_list(thisList)

print(f"Original list: {thisList}")
print(f"Flattened list: {flattened}")
