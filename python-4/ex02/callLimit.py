def callLimit(limit: int):
    """
    This is a decorator function and
    calculate the limit of called a function
    """
    count = 0

    def callLimiter(function):
        def limit_function(*args: any, **kwds: any):
            try:
                nonlocal count
                count += 1
                if count > limit:
                    raise (
                        AssertionError(f"Error {function}call too many times")
                        )
                return function(*args, **kwds)
            except AssertionError as msg:
                print(msg)
                return
        return limit_function
    return callLimiter
