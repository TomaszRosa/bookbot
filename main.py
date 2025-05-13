from stats import get_num_words, get_num_chars, sort_dic
import sys

def get_book_text(filepa):
    with open(filepa) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        text = get_book_text(book_path)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {get_num_words(text)} total words")
        print("--------- Character Count -------")
        book_chars = sort_dic(get_num_chars(text))
        for i in range(len(book_chars)):
            item = book_chars[i]
            if item["char"].isalpha():
                print(f"{item['char']}: {item['num']}")
        print("============= END ===============")

main()