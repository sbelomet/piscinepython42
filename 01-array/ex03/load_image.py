from typing import Any
import numpy as np
from PIL import Image


def ft_load(path: str) -> Any:
    """Load an image file and return its RGB pixel array.

    Prints the image format and its shape. Supports JPEG/JPG at minimum.

    Args:
        path: path to image file.

    Returns:
        A numpy array with shape (height, width, 3) in RGB ordering,
        or None on error.

    Errors are printed with a clear message and None is returned.
    """
    if not isinstance(path, str):
        print("Error: path must be a string")
        return None
    try:
        img = Image.open(path)
    except FileNotFoundError:
        print(f"Error: file not found: {path}")
        return None
    except Exception as e:
        print(
            "Error: cannot open image '{}': {}".format(path, e)
        )
        return None

    fmt = (img.format or "").upper()
    # Print format info
    print(f"Image format: {fmt}")
    if fmt not in ("JPEG", "JPG"):
        # Not required to reject other formats; warn the user
        print(
            f"Warning: format '{fmt}' not explicitly required, proceeding"
        )

    try:
        img = img.convert("RGB")
        arr = np.array(img)
    except Exception as e:
        print("Error: failed to convert image to RGB: {}".format(e))
        return None

    print("The shape of image is: {}".format(arr.shape))
    return arr
