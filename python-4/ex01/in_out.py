def square(x: int | float) -> int | float:
    x = x ** 2
    return x

def pow(x: int | float) -> int | float:
    return x ** x

def outer(x: int | float, function) -> object:
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