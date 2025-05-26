from stats import count
from stats import into_character
from stats import sort_dict
import sys

def main():
    # book_path = './books/frankenstein.txt'
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = count(text)
    word_dict = into_character(text)
    sort = sort_dict(word_dict)
    if len(sys.argv) < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {book_path}')
    print('----------- Word Count ----------')
    print(f'Found {num_words} total words')
    print('--------- Character Count -------')
    for i in sort:
        if i["name"].isalpha() == True:
            print(f'{i["name"]} : {i["num"]}')
    print('============= END ===============')


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

main()