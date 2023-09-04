
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    dict_to_list = list_to_dict(chars_dict)
    report = print_report(dict_to_list, num_words, book_path)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_character_sums(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def list_to_dict(chars):
    list1 = []
    temp_list = list(zip(chars.keys(), chars.values()))
    for i in temp_list:
        if i[0].isalpha() == True:
            list1.append(i)
    list1.sort()
    return list1

def print_report(dict_to_list, num_words, book_path):
    print(f"--- begin report of {book_path} ---")
    print(f"{num_words} words were found in the document")
    for i in dict_to_list:
        print(f"the {i[0]} character was found {i[1]} times")
    print("--- End report ---")
main()