from stats import get_word_count, get_character_count, create_sorted_list, sort_on
import sys

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_book = sys.argv[1]
    text = get_book_text(path_to_book)
    print(f"Found {get_word_count(text)} total words")
    sorted_list = create_sorted_list(get_character_count(text))
    for i in range(0, len(sorted_list)):
        if sorted_list[i]['char'].isalpha():
            print(f"{sorted_list[i]['char']}: {sorted_list[i]['num']}")

main()