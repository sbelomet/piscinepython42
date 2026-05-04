from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey

import os
from PIL import Image
import numpy as np


def main() -> None:
    try:
        src = ft_load("landscape.jpg")
    except Exception as exc:  # defensive: ft_load should handle errors itself
        print("Error: unexpected error when calling ft_load: {}".format(exc))
        return

    if src is None:
        # ft_load already printed an error message
        return

    outdir = "output"
    os.makedirs(outdir, exist_ok=True)

    funcs = [
        (ft_invert, "invert.png"),
        (ft_red, "red.png"),
        (ft_green, "green.png"),
        (ft_blue, "blue.png"),
        (ft_grey, "grey.png"),
    ]

    for func, fname in funcs:
        arr = np.array(src, copy=True)
        try:
            res = func(arr)
        except Exception as e:
            print(f"Error running {func.__name__}: {e}")
            continue
        if res is None:
            res = arr
        Image.fromarray(res).save(os.path.join(outdir, fname))
        print(f"Saved {fname} in {outdir}")

    print("")
    print(ft_invert.__doc__)
    print(ft_red.__doc__)
    print(ft_green.__doc__)
    print(ft_blue.__doc__)
    print(ft_grey.__doc__)


if __name__ == "__main__":
    main()
