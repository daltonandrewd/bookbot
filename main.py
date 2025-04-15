from stats import get_num_words, get_num_letters

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = get_num_letters(text)
    print(f"{num_words} words found in the document")
    print(num_letters)
    
def get_book_text(book):
    with open(book) as f:
        return f.read()

main()