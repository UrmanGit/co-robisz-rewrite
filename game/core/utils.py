import pygame as pg
import pathlib

from pygame import Color


def load_images(basepath: pathlib.Path) -> dict[str, pg.Surface]:
    images: dict[str, pg.Surface] = {}
    for path in (basepath / 'images').rglob("*.png"):
        image = pg.image.load(path)
        image = image.convert_alpha() if image.get_alpha() else image.convert()
        relative_path = path.relative_to(basepath / 'images')
        images[str(relative_path)] = image
    return images

def load_image(basepath: pathlib.Path) -> pg.Surface:
    image = pg.image.load(basepath)
    image = image.convert_alpha() if image.get_alpha() else image.convert()
    return image

def load_animations(basepath: pathlib.Path) -> dict[str, list[tuple[pg.Surface, float]]]:
    animations: dict[str, list[tuple[pg.Surface, float]]] = {}
    for path in (basepath / 'animations').rglob("*.gif"):
        animation = pg.image.load_animation(path)
        for pair in animation:
            pair[0].convert_alpha() if pair[0].get_alpha() else pair[0].convert()
        relative_path = path.relative_to(basepath / 'animations')
        animations[str(relative_path)] = animation
    return animations

def hex_col(hex_string: str) -> Color:
    """
    Returns a color from a hex string.
    :param hex_string: Hex string (e.g. "#08061B")
    """
    return pg.Color.from_hex(hex_string)