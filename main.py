def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    
def get_book_text(book):
    with open(book) as f:
        return f.read()

from stats import get_num_words


main()