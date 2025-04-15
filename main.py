import sys
from stats import get_num_words, get_num_letters, format_data

def main():
    if len(sys.argv)< 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = get_num_letters(text)
    list_letters = format_data(num_letters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for entry in list_letters:
        if entry["letter"].isalpha() == True:
            print(f"{entry["letter"]}: {entry["num"]}")
    print("============= END ===============")
    
def get_book_text(book):
    with open(book) as f:
        return f.read()

main()