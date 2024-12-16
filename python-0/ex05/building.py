import sys


def string_counter(value):
    """
    This function count the string what it have like,

    1-) Number of upper-case characters
    2-) Number of lower-case characters
    3-) Number of punctuation characters
    4-) Number of digits
    5-) Number of spaces
    """
    total_text = len(value)
    upper_letters = sum(1 for char in value if char.isupper())
    lower_letters = sum(1 for char in value if char.islower())
    digits = sum(1 for char in value if char.isdigit())
    punctuation_characters = ".,?!:;\"'()[]{}=+-*/×&|"
    spaces = sum(1 for char in value if char.isspace())
    punchs = sum(1 for char in value if char in punctuation_characters)

    print(f"The text contains {total_text} characters:")
    print(f"{upper_letters} upper letters")
    print(f"{lower_letters} lower letters")
    print(f"{punchs} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


def main():
    """
        Analyzes the given text and print it. If string have lower letters,
        upper letters, punctuation marks, spaces and digits.
        this program analyzes and show them.
    """
    arg_len = len(sys.argv)
    arg = ""
    try:
        if arg_len < 2:
            try:
                print("What is the text to count?")
                arg = input()
            except EOFError:
                pass
        elif arg_len == 2:
            arg = sys.argv[1]
        else:
            raise AssertionError("Too many arguments provided")
        string_counter(arg)
    except AssertionError as msg:
        print(AssertionError.__name__ + ":", msg)


if __name__ == "__main__":
    main()
