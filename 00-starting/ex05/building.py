import sys


def counting_time(string: str) -> None:
    """
    Counts and prints the number of characters, uppercase letters,
    lowercase letters, punctuation marks, spaces, and digits
    in the given string.
    """
    print(f"The text contains {len(string)} characters:")
    print(f"{sum(1 for c in string if c.isupper())} upper letters")
    print(f"{sum(1 for c in string if c.islower())} lower letters")
    punct_count = sum(1 for c in string if not c.isalnum() and not c.isspace())
    print(f"{punct_count} punctuation marks")
    print(f"{sum(1 for c in string if c.isspace())} spaces")
    print(f"{sum(1 for c in string if c.isdigit())} digits")


def main():
    """
    Handles command-line argument parsing and user input,
    then calls counting_time to analyze the text.
    """
    try:
        if len(sys.argv) == 2:
            string = sys.argv[1]
        elif len(sys.argv) > 2:
            raise AssertionError("Recieved more than one argument")
        else:
            try:
                string = input("What is the text to count?\n")
                string += "\n"
            except EOFError:
                pass
        counting_time(string)
    except AssertionError as e:
        print("AssertionError:", e)


if __name__ == "__main__":
    main()
