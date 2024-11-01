import string

def main():
    book_path = "books/frankenstein.txt"
    text = book_contents(book_path)
    word_count = count_words(text)
    char_count = count_characters(text)
    char_list = sorted_list(char_count)
    return write_report(word_count, char_list)

def book_contents(book):
    with open(book) as f:
        return f.read()

def count_words(book):
    words = book.split()
    word_count = len(words)
    return word_count

def count_characters(book):
    book_lc = book.lower()
    char_dict = dict.fromkeys(string.ascii_lowercase, 0)
    for char in book_lc:
        if char == "\n":
            pass
        elif char == "\r":
            pass
        elif char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_by_number(i):
    return i["num"]

def sorted_list(dict):
    char_ls = []
    for c in dict:
        char_ls.append({"char": c, "num": dict[c]})
        # print(f"The {c} character is used {chars[c]} times.")
    char_ls.sort(reverse=True, key=sort_by_number)
    return char_ls

def write_report(words, list):
    print("=== Book report ===")
    print(f"Book has {words} word(s) total.")
    print("")
    for c in list:
        print(f"The '{c['char']}' character is used '{c['num']}' times.")
    print("=== End report ===")

main()
