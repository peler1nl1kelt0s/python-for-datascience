import numpy as np
import cv2 as cv2


def ft_load(path: str) -> np.ndarray:
    """
        Load an image from the specified path and return it as a NumPy array.

        ft_load function gets the jpg or jpeg image and returning rgb
        value.

        Parameters:
            path(str): The path where you storage the image file.
        Returns:
            np.ndarray: A numpy array representing the load image
    """
    try:
        if not path.lower().endswith(("jpg", "jpeg")):
            raise AssertionError("Only JPG and JPEG formats are supported.")
        image = cv2.imread(path)
        if image is None:
            raise AssertionError("Wrong image path!")
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        array = np.array(rgb_image)
        return array
    except AssertionError as msg:
        print("\033[31m", AssertionError.__name__ + ":", msg, "\033[0m")
    except IOError as msg:
        print(IOError.__name__ + ":", msg)
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
