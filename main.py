def main():
    book_path = "books/Frankenstein.txt"
    book = "Frankenstein.txt"
    text = get_book_text(book_path)
    words = word_count(text)
    characters = character_count(text)
    sorted_list = sort_char(characters)

    print(f"--- Begin report of {book_path} ---")
    print(f"{words} words found in the document")
    print("")

    for char in sorted_list:
        for cha in char:
            print(f"The '{cha}' character was found {char[cha]} times")

    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        book_text = f.read()
        return book_text

def word_count(text):
    num_words = text.split()
    return len(num_words)

def character_count(text):
    character_dict = {}
    lwc_text = text.lower()
    for c in lwc_text:
        if c in character_dict:
            character_dict[c] += 1
        else:
            character_dict[c] = 1
    return character_dict


def sort_char(characters):
    sorted_char = {}
    char_list = []
    def sort_on(characters):
            for char in characters:
                return characters[char]
    for char in characters:
        if char.isalpha() == True:
            sorted_char[char] = characters[char]
    for char in sorted_char:
        char_list.append({char:sorted_char[char]})
    char_list.sort(reverse = True, key=sort_on)
    return char_list



main()