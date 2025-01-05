def mean(*args: any):
    return sum(args) / len(args)

def median(*args: any):
    arg = list(args)

def quartile(*args: any):
    pass

def std(*args: any):
    mean_value = mean(*args)
    variance = sum([(i - mean_value) ** 2 for i in args])
    return (variance / len(args)) ** (1/2)

def var(*args: any):
    mean_value = mean(*args)
    variance = sum([(i - mean_value) ** 2 for i in args])
    return (variance / len(args))

def ft_statistics(*args: any, **kwargs: any) -> None:
    if len(args) == 0:
        print("ERROR")
        return
    for key, value in kwargs.items():
        if value == "median":
            print("median : ", median(*args))
        elif value == "mean":
            print("mean : ", mean(*args))
        elif value == "quartile":
            print("quartile : ", quartile(*args))
        elif value == "std":
            print("std : ", std(*args))
        elif value == "var":
            print("var : ", var(*args))
        else:
            print("ERROR")
