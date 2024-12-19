from load_image import ft_load
import cv2 as cv2


def main():
    """
        This program get the animal jpeg image and zooming to the center
        of image.
    """
    try:
        image = ft_load("animal.jpeg")
        if image is None:
            raise AssertionError("Wrong image path!")
        print(image)
        new_height, new_width = 400, 400
        center_x, center_y = image.shape[0] // 2, image.shape[1] // 2
        start_y = center_y - new_height // 2
        start_x = center_x - new_width // 2
        end_y = center_y + new_height // 2
        end_x = center_x + new_width // 2
        zoomed_image = image[start_y:end_y, start_x:end_x, 0]
        cv2.imwrite("zoomed.jpeg", zoomed_image)
        print("New shape after slicing: (400, 400, 1) or", zoomed_image.shape)
        print(zoomed_image)
    except AssertionError as msg:
        print("\033[31m", AssertionError.__name__ + ":", msg, "\033[0m")


if __name__ == "__main__":
    main()
