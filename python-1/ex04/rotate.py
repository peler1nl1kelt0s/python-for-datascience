from load_image import ft_load
# import cv2 as cv2
import sys
from matplotlib import pyplot as plt
import numpy as np


def rotate_90_right(matrix):
    """
        This function gets a matrix and rotate 90 degree to left.
        Arguments: gets list
        rows: rows of list
        cols: columns of list
        rotated: firstly initializing is empty but after that
        being rotated image
    """
    rows, cols = len(matrix), len(matrix[0])
    rotated = np.array([[0] * rows for _ in range(cols)])
    for i in range(rows):
        for j in range(cols):
            rotated[cols - j - 1][i] = matrix[i][j]
    return rotated


def main():
    """
        This program get the animal jpeg image and rotate the center
        of image.
        ft_load: to load the image like numpy rgb array
        new_height: we want to zoom height
        new_width: we want to zoom width
        center_x: center x of the image
        center_y: center y of the image
        start_y: zooming y starts this point
        start_x: zooming x starts this point
        end_y: zooming y ending this point
        end_x: zooming x ending this point
        zoomed_image: the value that after zoomed
    """
    try:
        if len(sys.argv) != 2:
            raise AssertionError("Wrong number of arguments!")
        image = ft_load(sys.argv[1])
        if image is None:
            raise AssertionError("Wrong image path!")
        new_height, new_width = 400, 400
        center_x, center_y = image.shape[0] // 2, image.shape[1] // 2
        start_y = center_y - new_height // 2
        start_x = center_x - new_width // 2
        end_y = center_y + new_height // 2
        end_x = center_x + new_width // 2
        zoom_image = image[start_y:end_y, start_x:end_x, 0]
        print("The shape of image is: (400, 400, 1) or (400, 400)")
        print(zoom_image)
        rotated_image = rotate_90_right(zoom_image)
        print(f"New shape after Transpose: {rotated_image.shape}")
        print(rotated_image)
        plt.imshow(rotated_image, cmap="gray")
        plt.title("Rotated Image")
        plt.savefig("rotated.jpeg")
    except AssertionError as msg:
        print("\033[31m", AssertionError.__name__ + ":", msg, "\033[0m")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")


if __name__ == "__main__":
    main()
