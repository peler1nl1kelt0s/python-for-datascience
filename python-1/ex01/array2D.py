import numpy as np

def slice_me(family: list, start: int, end: int) -> list:
    """
        Family: The list that we want to slice
        Start: starting index of slicing process
        end: ending index of slicing process
        -> list: Function returns a list
        This function slice a list how do you want. 
        Example: I wanna slice 1 index to 5 you can give start:1 and end:5
        you will get a list that you wanna slice
    """
    try:
        if start < 0:
            raise AssertionError("Given start value is bad it should be lower than 0!")
        if start >= end:
            end = start + 1
        print(f"My shape is : {np.array(family).shape}")
        print(f"My new shape is : {np.array(family)[start:end].shape}")
        return np.array(family)[start:end].tolist()
    except AssertionError  as msg:
        print(AssertionError.__name__ + ":", msg) 
