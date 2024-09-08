def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()
    
def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}

    for char in text:
        lowered = char.lower()
        chars[lowered] = chars.get(lowered, 0) + 1

    return chars

def sort_on(list):
    return list["num"]

def chars_dict_to_sorted_list(chars_dict):
    sorted_list = []

    for char in chars_dict:
        sorted_list.append({"char": char, "num": chars_dict[char]})

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

main()