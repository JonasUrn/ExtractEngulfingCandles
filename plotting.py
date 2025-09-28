from typing import Any, List, Tuple
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def plot_image(img: Any):
    """
    Desription:
        A function to plot a single image
    Params:
        Any image
    """
    plt.imshow(img, cmap="gray")
    plt.axis("off")
    plt.show()


def plot_engulfing(img: Any, engulfing_patterns: List[Tuple]):
    """
    Simple function to plot chart with engulfing candles marked.

    Args:
        image: grayscale image
        engulfing_patterns: list of (candle1, candle2) tuples
    """
    plt.figure(figsize=(12, 8))
    plt.imshow(img, cmap="gray")

    for candle1, candle2 in engulfing_patterns:
        left = min(candle1["center"], candle2["center"]) - 25
        right = max(candle1["center"], candle2["center"]) + 25
        top = min(candle1["top"], candle2["top"])
        bottom = max(candle1["bottom"], candle2["bottom"])

        rect = patches.Rectangle(
            (left, top),
            right - left,
            bottom - top,
            linewidth=3,
            edgecolor="yellow",
            facecolor="none",
        )
        plt.gca().add_patch(rect)

    plt.title(f"Found {len(engulfing_patterns)} engulfing patterns")
    plt.axis("off")
    plt.show()
