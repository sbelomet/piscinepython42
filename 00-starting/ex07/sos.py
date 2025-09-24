import sys


def time_to_go_morse_mode(string):
    NESTED_MORSE = {" ": "/",
                    "A": ".-",
                    "B": "-...",
                    "C": "-.-.",
                    "D": "-..",
                    "E": ".",
                    "F": "..-.",
                    "G": "--.",
                    "H": "....",
                    "I": "..",
                    "J": ".---",
                    "K": "-.-",
                    "L": ".-..",
                    "M": "--",
                    "N": "-.",
                    "O": "---",
                    "P": ".--.",
                    "Q": "--.-",
                    "R": ".-.",
                    "S": "...",
                    "T": "-",
                    "U": "..-",
                    "V": "...-",
                    "W": ".--",
                    "X": "-..-",
                    "Y": "-.--",
                    "Z": "--..",
                    "1": ".----",
                    "2": "..---",
                    "3": "...--",
                    "4": "....-",
                    "5": ".....",
                    "6": "-....",
                    "7": "--...",
                    "8": "---..",
                    "9": "----.",
                    "0": "-----"}
    uppered = string.upper()
    morse = [NESTED_MORSE[c] for c in uppered]
    print(' '.join(morse))


def main():
    try:
        if len(sys.argv) != 2:
            raise AssertionError("One arguments expected (string)")
        if not all(c.isalnum() or c == ' ' for c in sys.argv[1]):
            raise AssertionError("Only letters, numbers and spaces allowed")
        time_to_go_morse_mode(sys.argv[1])
    except AssertionError as e:
        print("AssertionError:", e)


if __name__ == "__main__":
    main()
