def get_num_words(book):
    return len(book.split())

def get_num_chars(book):
    string = book.lower()
    di = {}
    for char in string:
        if char not in di:
            di[char] = 1
        else:
            di[char] += 1
    return di

def sort_on(dict):
    return dict["num"]

def sort_dic(dict):
    chars_list = []
    for char, count in dict.items():
        chars_list.append({"char": char, "num": count})
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list
