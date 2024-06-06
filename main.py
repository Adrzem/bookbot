def main():
    book_path = "books/Frankenstein.txt"
    text = get_book_text(book_path)
    words = word_count(text)
    characters = character_count(text)
    print(characters)


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
    


main()