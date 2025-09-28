import cv2
import glob


def load_folder(path: str, grayscale: bool = False):
    image_paths = glob.glob(f"{path}/*.png")
    images = []
    for path in image_paths:
        try:
            images.append(load_image(path, grayscale))
        except:
            continue
    return images


def load_image(path: str, grayscale: bool = False):
    if grayscale:
        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        if img is None:
            raise ValueError(f"Could not load image from {path}")
        return img
    else:
        img = cv2.imread(path, cv2.IMREAD_COLOR)
        if img is None:
            raise ValueError(f"Could not load image from {path}")
        return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
