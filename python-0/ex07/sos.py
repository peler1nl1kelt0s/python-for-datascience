import sys

NESTED_MORSE = {
    " ": "/ ",
    "A": ".- ", "B": "-... ", "C": "-.-. ", "D": "-.. ", "E": ". ",
    "F": "..-. ", "G": "--. ", "H": ".... ", "I": ".. ", "J": ".--- ",
    "K": "-.- ", "L": ".-.. ", "M": "-- ", "N": "-. ", "O": "--- ",
    "P": ".--. ", "Q": "--.- ", "R": ".-. ", "S": "... ", "T": "- ",
    "U": "..- ", "V": "...- ", "W": ".-- ", "X": "-..- ", "Y": "-.-- ",
    "Z": "--.. ",
    "0": "----- ", "1": ".---- ", "2": "..--- ", "3": "...-- ",
    "4": "....- ", "5": "..... ", "6": "-.... ", "7": "--... ",
    "8": "---.. ", "9": "----. "
}

def encode_to_morse(text):
    """
        This function converts text to morse alphabets. For example:
        if you give "hello" string you will get the morse of the "hello" like
        .... . .-.. .-.. ---
    """
    result = []
    for char in text:
        if char not in NESTED_MORSE:
            raise AssertionError("the arguments are bad")
        result.append(NESTED_MORSE[char])
    
    assert isinstance(text, str), "the arguments are bad"

    return "".join(result).rstrip()

def main():
    """
        The main function gets arguments and parse and give the text
        to encode_to_morse function.
    """
    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")
        
        morse_code = encode_to_morse(sys.argv[1].upper())
        print(morse_code)
    except AssertionError as e:
        print(f"AssertionError: {e}")

if __name__ == "__main__":
    main()