def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    num_words = get_num_words(text)
    num_characters = get_num_characters(text)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document\n")

    for char in num_characters:
        if char in alphabet:
            print(f"The '{char}' character was found {num_characters[char]} times")

    print("--- End report ---")


def get_num_characters(text):
    dict = {}
    for char in text:
        lowered = char.lower()
        if lowered not in dict:
            dict[lowered] = 0
        dict[lowered] += 1
    return dict


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


alphabet = set(
    [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]
)


main()
