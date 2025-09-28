import matplotlib.pyplot as plt

from load_data import load_folder
from plotting import plot_engulfing
from utils import turn_image_grayscale
from algorithms import find_engulfing


if __name__ == "__main__":
    load_grayscale = False
    use_cap = 500

    train_down_data = "Data/Train/Down"
    train_up_data = "Data/Train/Up"
    # test_down_data = "Data/Test/Down"
    # test_up_data = "Data/Test/Up"

    train_down_images = load_folder(train_down_data)
    train_up_images = load_folder(train_up_data)
    train_images = train_down_images
    train_images.extend(train_up_images)

    grayscale_images = []
    if not load_grayscale:
        grayscale_images = [turn_image_grayscale(img) for img in train_images]
    else:
        grayscale_images = train_images

    if use_cap is not None:
        grayscale_images = grayscale_images[0:use_cap]

    results = []
    for i, img in enumerate(grayscale_images):
        res = find_engulfing(img, 50)
        if len(res) > 0:
            results.append((i, res))

    if len(results) == 0:
        print("No engulfing candles found in given images.")

    for r in results:
        plot_engulfing(train_images[r[0]], r[1])
