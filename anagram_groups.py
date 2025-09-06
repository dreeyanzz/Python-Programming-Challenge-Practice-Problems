import os

os.system("cls")


def is_anagram(text1: str, text2: str) -> bool:
    isAnagram: bool = sorted(text1.lower().replace(" ", "")) == sorted(
        text2.lower().replace(" ", "")
    )

    return isAnagram


def group_anagrams(words: list[str]) -> list[list[str]]:
    grouped: list[list[str]] = []
    words = words[:]

    while words:

        group: list[str] = []
        current_word = words[0]

        for word in words[:]:
            if is_anagram(current_word, word):
                group.append(word)
                words.remove(word)

        grouped.append(group)

    return grouped


words: list[str] = ["eat", "tea", "tan", "ate", "nat", "bat"]
grouped: list[list[str]] = group_anagrams(words)

print(f"Original words: {words}")
print(f"Grouped word: {grouped}")
