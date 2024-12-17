def bmi_calculate(height : int | float, weight : int | float) -> float:
    """
        this function calculate Body Mass Index and returning
    """
    return weight / (height * height)

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """
        this function calculate Body Mass Index and returning every for
        given lists as arguments and returning
    """
    result = []
    try:
        if (len(height) != len(weight)):
            raise ValueError("You gived wrong number list!")

        for i in range(len(height)):
            result.append(bmi_calculate(height=height[i],weight=weight[i]))
    except ValueError as msg:
        print(ValueError.__name__ + ":", msg)
    return result

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
        this function create a limit and if a list value above of limit
        then gets true bool value and storage in a list.
    """
    result = []
    for i in bmi:
        if i > limit:
            result.append(True)
        else:
            result.append(False)
    return result
