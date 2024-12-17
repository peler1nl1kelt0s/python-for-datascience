"""
    squaring your height in metres: 1.70 x 1.70 = 2.89
    dividing your weight in kilograms: 70 ÷ 2.89 = 24.22
"""

def bmi_calculate(height : int | float, weight : int | float) -> float:
    return weight / (height * height)

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
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
    result = []
    for i in bmi:
        if i > limit:
            result.append(True)
        else:
            result.append(False)
    return result
