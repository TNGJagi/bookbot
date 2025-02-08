def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_num_chars(text)

    print(f"{num_words} words found in the document")
    
    for item in num_chars:
        print(f"The '{item["char"]}' character was found {item["count"]} times")
    
def get_num_words(text):
    words = text.split()
    return len(words)

def sort_on(num_chars_list):
    return num_chars_list["count"]

def get_num_chars(text):
    num_chars = {}
    num_chars_list = []
    lc_char = ""
    count = 0
    for char in text:
        lc_char = char.lower()
        if lc_char.isalpha():
            if lc_char in num_chars:
                num_chars[lc_char] += 1
            else:
                num_chars[lc_char] = 1
    
    for char, count in num_chars.items():
        num_chars_list.append({"char": char, "count": count})
    
    num_chars_list.sort(reverse=True, key=sort_on)

    return num_chars_list

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()


