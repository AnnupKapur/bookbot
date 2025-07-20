import sys

from stats import count_words
from stats import count_chars
from utils import get_book_text
from reports import words_chars_report

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    words_chars_report(file_path)

main()
