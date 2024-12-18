import numpy as np
import cv2 as cv2

def ft_load(path: str) -> list:
    try:
        image = cv2.imread(path)
        if image is None:
            raise AssertionError("Wrong image path!")
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        array = np.array(rgb_image)
        print("The shape of image is:",array.shape)
        # print(array)
        return f"{array[0, :3]}\n    ... \n {array[-1, -3:]}"
    except AssertionError as msg:
        print(AssertionError.__name__ + ":", msg)
    except IOError as msg:
        print(IOError.__name__ + ":", msg)
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

