import numpy as np
from matplotlib import pyplot as plt


def plotting_and_saving(array, name, return_name) -> np.ndarray:
    plt.imshow(array)
    plt.title(name)
    plt.savefig(return_name)
    return array


def rgb_converter_to_zero(array: np.ndarray, index, name, return_name):
    array[:, :, index[0]] = 0
    array[:, :, index[1]] = 0
    return plotting_and_saving(array=array, name=name, return_name=return_name)


def ft_invert(array: np.ndarray) -> np.ndarray:
    """
    Inverts the color of the image received. All the rgb
    subtracting from 255 we get the invert version
    """
    array = array.copy()
    array = 255 - array
    return plotting_and_saving(
        array=array,
        name="Inverted Image",
        return_name="inverted")


def ft_red(array: np.ndarray) -> np.ndarray:
    """
    The image received that convert to red version by setting
    the blue and green equal to zero
    """
    return rgb_converter_to_zero(
        array=array.copy(),
        index=[1, 2],
        name="Red Image",
        return_name="reded")


def ft_green(array: np.ndarray) -> np.ndarray:
    """
    The image received that convert to red version by setting
    the blue and green equal to zero
    """
    return rgb_converter_to_zero(
        array=array.copy(),
        index=[0, 2],
        name="Green Image",
        return_name="greened")


def ft_blue(array: np.ndarray) -> np.ndarray:
    """
    The image received that convert to blue version by setting
    the red and green equal to zero
    """
    return rgb_converter_to_zero(
        array=array.copy(),
        index=[0, 1],
        name="Blue Image",
        return_name="blued")


def ft_grey(array: np.ndarray) -> np.ndarray:
    """
    The image received that convert to grey version by setting mean
    of rgbs and equal to grey.
    """
    array = array.copy()
    grey = np.mean(array, axis=2)

    array[:, :, 0] = grey
    array[:, :, 1] = grey
    array[:, :, 2] = grey

    return plotting_and_saving(
        array=array,
        name="Grey Image",
        return_name="greyed")
