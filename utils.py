from typing import Any
import numpy as np
import cv2


def turn_image_grayscale(img: Any) -> np.ndarray:
    if len(img.shape) == 2:
        return img
    elif len(img.shape) == 3 and img.shape[2] == 3:
        return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    else:
        raise ValueError(f"Unexpected image shape: {img.shape}")
