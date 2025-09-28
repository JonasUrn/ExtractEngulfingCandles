import numpy as np
from typing import Any


def find_engulfing(img: Any, threshold: int = 50):
    candle_bodies = find_candle_bodies(img, threshold)

    engulfing_candles = []

    if not candle_bodies:
        return []

    if len(candle_bodies) < 2:
        return []

    for i in range(1, len(candle_bodies)):
        if is_engulfing(candle_bodies[i - 1], candle_bodies[i]):
            engulfing_candles.append((candle_bodies[i - 1], candle_bodies[i]))

    return engulfing_candles


def find_candle_bodies(img: np.ndarray, threshold: int = 50):
    width = img.shape[1]
    candle_bodies = []
    pos = 0

    while pos < width:
        while pos < width and not is_candle_column(img[:, pos], threshold):
            pos += 1

        if pos >= width:
            break

        candle_start = pos

        while pos < width and is_candle_column(img[:, pos], threshold):
            pos += 1

        candle_end = pos

        candle_body = extract_candle_body(img, candle_start, candle_end, threshold)
        if candle_body is not None:
            candle_bodies.append(candle_body)

    return candle_bodies


def is_candle_column(column: np.ndarray, threshold: int) -> bool:
    candle_pixels = np.sum(column >= threshold)
    total_pixels = len(column)

    return candle_pixels >= total_pixels * 0.15


def extract_candle_body(
    img: np.ndarray, candle_start: int, candle_end: int, separation_threshold: int = 50
):
    height = img.shape[0]
    candle = img[:, candle_start:candle_end]
    candle_width = candle_end - candle_start

    if candle_width < 3:
        return None

    candle_rows = []
    for y in range(height):
        row = candle[y, :]
        candle_pixels = np.sum(row >= separation_threshold)
        candle_rows.append(candle_pixels)

    max_width = max(candle_rows) if candle_rows else 0
    if max_width < candle_width * 0.5:
        return None

    width_threshold = max_width * 0.2
    candle_body_rows = [
        i for i, width in enumerate(candle_rows) if width >= width_threshold
    ]

    if not candle_body_rows or len(candle_body_rows) < 5:
        return None

    top = min(candle_body_rows)
    bottom = max(candle_body_rows)
    body_height = bottom - top
    center = (candle_start + candle_end) // 2

    if body_height < 10:
        return None

    return {
        "top": top,
        "bottom": bottom,
        "center": center,
        "width": candle_width,
        "height": body_height,
    }


def is_engulfing(candle1: dict, candle2: dict, max_horizontal_gap: int = None):
    if candle1 is None or candle2 is None:
        return False

    if candle2["height"] <= candle1["height"]:
        return False

    if not (
        candle2["top"] <= candle1["top"] and candle2["bottom"] >= candle1["bottom"]
    ):
        return False

    if max_horizontal_gap is None:
        max_horizontal_gap = max(20, (candle1["width"] + candle2["width"]) // 2 * 2)

    horizontal_distance = abs(candle2["center"] - candle1["center"])
    if horizontal_distance > max_horizontal_gap:
        return False

    return True
