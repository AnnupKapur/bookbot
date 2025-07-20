from stats import count_words
from stats import count_chars
from stats import sorted_count_chars
from utils import get_book_text

def words_chars_report(book_path): 
    book_text = get_book_text(book_path)
    word_count = count_words(book_text)
    chars = count_chars(book_text)
    chars_sorted = sorted_count_chars(chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char, count in chars_sorted:
        print(f"{char}: {count}")
    print("============= END ===============")
