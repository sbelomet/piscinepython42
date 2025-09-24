import sys
from ft_filter import ft_filter


def look_for_words(string, size):
    words = string.split()
    cleaned_words = [word for word in words if word.isalnum()]
    filtered = list(ft_filter(lambda word: len(word) > size, cleaned_words))
    print(filtered)


def main():
    try:
        if len(sys.argv) != 3:
            raise AssertionError("Two arguments expacted (string and integer)")
        if not sys.argv[2].isdigit():
            raise AssertionError("Two arguments expacted (string and integer)")
        string = sys.argv[1]
        size = int(sys.argv[2])
        look_for_words(string, size)
    except AssertionError as e:
        print("AssertionError:", e)


if __name__ == "__main__":
    main()
