def mean(args: list):
    """
    This function returns mean of a list
    """
    return sum(args) / len(args)


def sort(arg: list):
    """
    This function returns sorted of a list
    """
    result = []
    while arg:
        min_val = float('inf')
        min_index = -1
        for i in range(len(arg)):
            if arg[i] < min_val:
                min_val = arg[i]
                min_index = i
        result.append(min_val)
        arg.pop(min_index)
    return result


def median(args: list):
    """
    This function returns median of a list
    """
    sorted = sort(args.copy())
    mid = len(sorted) // 2
    if len(sorted) % 2 == 0:
        return (sorted[mid - 1] + sorted[mid]) / 2
    else:
        return sorted[mid]


def quartile(args: list):
    """
    This function returns quartile of a list
    """
    sorted = sort(args)
    q1 = float(median(sorted[:len(sorted) // 2 + 1]))
    q3 = float(median(sorted[len(sorted) // 2:]))
    return [q1, q3]


def std(args: list):
    """
    This function returns standart devision of a list
    """
    mean_value = mean(args)
    variance = sum([(i - mean_value) ** 2 for i in args])
    return (variance / len(args)) ** (1/2)


def var(args: list):
    """
    This function returns variance of a list
    """
    mean_value = mean(args)
    variance = sum([(i - mean_value) ** 2 for i in args])
    return (variance / len(args))


def ft_statistics(*args: any, **kwargs: any) -> None:
    """
    This function Calculate all of things like
    standar devision, variance, median, mean etc.
    """
    try:
        if not args:
            data = None
        else:
            data = [float(x) for x in args]
            if len(data) == 0:
                data = None
    except (ValueError, TypeError):
        data = None

    valid_stats = {"mean", "median", "quartile", "std", "var"}

    if data is None:
        for stat in kwargs.values():
            if stat in valid_stats:
                print("ERROR")
        return
    args = list(args)
    for key, value in kwargs.items():
        if value == "median":
            print("median : ", median(args.copy()))
        elif value == "mean":
            print("mean : ", mean(args.copy()))
        elif value == "quartile":
            print("quartile : ", quartile(args.copy()))
        elif value == "std":
            print("std : ", std(args.copy()))
        elif value == "var":
            print("var : ", var(args.copy()))
