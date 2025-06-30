from stats import get_num_words, get_num_chars, sorted_char_counts
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        print (file_contents)

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    path_to_file = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(path_to_file)} total words")
    print("--------- Character Count -------")
    counts = sorted_char_counts(path_to_file)
    for char, count in counts:
        if char.isalpha():
            print(f"{char}: {count}")