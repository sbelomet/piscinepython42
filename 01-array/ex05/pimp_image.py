import numpy as np


def ft_invert(array) -> np.ndarray:
    """Inverts the color of the image received."""
    array[:] = 255 - array
    return array


def ft_red(array) -> np.ndarray:
    """Keep red channel, zero green & blue."""
    if array.ndim == 3 and array.shape[2] >= 3:
        array[:, :, 1:] *= 0
    return array


def ft_green(array) -> np.ndarray:
    """Keep green channel, zero red & blue."""
    if array.ndim == 3 and array.shape[2] >= 3:
        array[:, :, 0] -= array[:, :, 0]
        array[:, :, 2] -= array[:, :, 2]
    return array


def ft_blue(array) -> np.ndarray:
    """Keep blue channel, zero red & green."""
    if array.ndim == 3 and array.shape[2] >= 3:
        array[:, :, 0] = 0
        array[:, :, 1] = 0
    return array


def ft_grey(array) -> np.ndarray:
    """Convert to grayscale."""
    if array.ndim == 3 and array.shape[2] >= 3:
        dtype = array.dtype
        gray = array.mean(axis=2)
        gray.astype(dtype)
        array[:, :, 0] = gray
        array[:, :, 1] = gray
        array[:, :, 2] = gray
    elif array.ndim == 2:
        # already single-channel; nothing to do
        pass
    return array
