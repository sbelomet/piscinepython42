import numpy as np
import matplotlib.pyplot as plt

from load_image import ft_load


def main() -> None:
    """Load image, crop a 400x400 center square, rotate it, save and print info.

    Handles errors with clear messages instead of crashing.
    """
    try:
        arr = ft_load("animal.jpeg")
    except Exception as exc:  # defensive: ft_load should handle errors itself
        print("Error: unexpected error when calling ft_load: {}".format(exc))
        return

    if arr is None:
        # ft_load already printed an error message
        return

    # Convert to grayscale (single channel) for zoom display
    if arr.ndim == 3 and arr.shape[2] >= 3:
        # use standard luminance conversion
        try:
            r = arr[:, :, 0].astype(float)
            g = arr[:, :, 1].astype(float)
            b = arr[:, :, 2].astype(float)
            gray = (0.2989 * r + 0.5870 * g + 0.1140 * b).astype(np.uint8)
        except Exception as exc:
            print("Error converting to grayscale: {}".format(exc))
            return
    else:
        gray = arr if arr.ndim == 2 else arr[:, :]

    # Crop a 400x400 center region (or smaller if image is smaller)
    h, w = gray.shape[:2]
    crop_size = 400
    crop_h = min(crop_size, h)
    crop_w = min(crop_size, w)
    cy = h // 2
    cx = w // 2
    y0 = max(0, cy - crop_h // 2)
    x0 = max(0, cx - crop_w // 2)
    y1 = y0 + crop_h
    x1 = x0 + crop_w
    crop = gray[y0:y1, x0:x1]

    # Expand dims to (h, w, 1) to show a single-channel 3D array
    if crop.ndim == 2:
        crop_expanded = crop[:, :, np.newaxis]
    else:
        crop_expanded = crop

    print("The shape of image is: {}".format(crop_expanded.shape))
    print(crop_expanded)

    # Rotate 90 degrees left
    mat = crop.tolist()
    rotated_list = [list(row) for row in zip(*mat)][::-1]
    rotated = np.array(rotated_list, dtype=crop.dtype)
    # rotated = np.rot90(crop, k=1)

    # Display with axis scale (pixel coordinates)
    try:
        plt.figure(figsize=(6, 6))
        plt.imshow(rotated, cmap="gray", vmin=0, vmax=255)
        # show ticks for scale: start at 0 and go in steps of 50 pixels
        xticks = np.arange(0, rotated.shape[1], 50, dtype=int)
        yticks = np.arange(0, rotated.shape[0], 50, dtype=int)
        plt.gca().set_xticks(xticks)
        plt.gca().set_yticks(yticks)
        plt.gca().set_xticklabels(xticks)
        plt.gca().set_yticklabels(yticks)
        plt.tight_layout()
        out = "rotated.png"
        plt.savefig(out)
        print(f"Saved zoom image to {out}")
    except Exception as exc:
        print("Error saving rotated image: {}".format(exc))
        # continue to print shape/data even if saving failed

    print("New shape after Transpose: {}".format(rotated.shape))
    print(rotated)


if __name__ == "__main__":
    main()
