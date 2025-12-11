import pygame as pg
import pathlib

from pygame import Color


def load_images(path: pathlib.Path, scale_factor: int) -> dict[str, pg.Surface]:
    """Recursively loads all .png files from a given folder"""
    images: dict[str, pg.Surface] = {}
    for file_path in path.rglob("*.png"):
        image = pg.image.load(file_path)
        image = image.convert_alpha() if image.get_alpha() else image.convert()
        image = pg.transform.scale_by(image, scale_factor)
        relative_path = file_path.relative_to(path)
        images[str(relative_path).replace("\\", "/")] = image
    return images


def load_image(path: pathlib.Path, scale_factor: int) -> pg.Surface:
    """Load a single image"""
    image = pg.image.load(path)
    image = image.convert_alpha() if image.get_alpha() else image.convert()
    image = pg.transform.scale_by(image, scale_factor)
    return image


def load_animations(path: pathlib.Path, scale_factor: int) -> dict[str, list[tuple[pg.Surface, float]]]:
    """Recursively loads all .gif files from a given folder"""
    animations: dict[str, list[tuple[pg.Surface, float]]] = {}

    for file_path in path.rglob("*.gif"):
        # Loading the animation as normal
        animation: list[tuple[pg.Surface, float]] = pg.image.load_animation(file_path)

        for i, pair in enumerate(animation):
            # 1. Rip the pair apart
            frame, delay = pair

            # 2. Convert the frame and resize it
            frame.convert_alpha() if frame.get_alpha() else frame.convert()
            frame = pg.transform.scale_by(frame, scale_factor)

            # 3. Put everything together like nothing happened
            animation[i] = (frame, delay)

            # 4. Surgery completed successfully

        relative_path = file_path.relative_to(path)
        animations[str(relative_path).replace("\\", "/")] = animation
    return animations


def hex_col(hex_string: str) -> Color:
    """
    Returns a color from a hex string.
    :param hex_string: Hex string (e.g. "#08061B")
    """
    return pg.Color.from_hex(hex_string)
