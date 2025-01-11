def square(x: int | float) -> int | float:
    """
    This function returns square of a
    integer or float variable
    """
    x = x ** 2
    return x

def pow(x: int | float) -> int | float:
    """
    This function returns powder with yourself
    """
    return x ** x

def outer(x: int | float, function) -> object:
    """
    This is a decarator function.
    This returns a function and continue with
    before result.
    """
    count = 0
    def inner() -> float:
        nonlocal count
        if count == 0:
            result = function(x)
        else:
            result = function(inner.previus_result)
        inner.previus_result = result
        count += 1
        return result
    return inner