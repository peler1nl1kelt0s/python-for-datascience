import sys
from ft_filter import ft_filter

def main():
    """
        Filtering the given text. It behave like the original built-in 
        function.
    """
    arg_len = len(sys.argv)
    string = ""
    size = 0
    try:
        if arg_len != 3:
            raise AssertionError("AssertionError: the arguments are bad")
        else:
            string = sys.argv[1]
            size = int(sys.argv[2])
        result = list(ft_filter(function=lambda word: len(word) > size, iterable=string.split()))
        print(result)
    except ValueError as msg:
        print(ValueError.__name__ + ":", msg)
    except AssertionError as msg:
        print(AssertionError.__name__ + ":", msg)

if __name__ == "__main__":
    main()
