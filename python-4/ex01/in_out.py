def square(x: int | float) -> int | float:
    return x ** 2

def pow(x: int | float) -> int | float:
    return 
def outer(x: int | float, function) -> object:
    count = 0
    def inner() -> float:
        return function(x)
    return inner