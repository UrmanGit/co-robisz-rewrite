import pygame as pg
import pathlib

def load_images(path: pathlib.Path) -> dict[str, pg.Surface]:
    """Recursively loads all .png files from given folder"""
    images: dict[str, pg.Surface] = {}
    for file_path in path.rglob("*.png"):
        image = pg.image.load(file_path)
        image = image.convert_alpha() if image.get_alpha() else image.convert()
        relative_path = file_path.relative_to(path)
        images[str(relative_path)] = image
    return images

def load_image(path: pathlib.Path) -> pg.Surface:
    image = pg.image.load(path)
    image = image.convert_alpha() if image.get_alpha() else image.convert()
    return image

def load_animations(path: pathlib.Path) -> dict[str, list[tuple[pg.Surface, float]]]:
    animations: dict[str, list[tuple[pg.Surface, float]]] = {}
    for file_path in path.rglob("*.gif"):
        animation = pg.image.load_animation(file_path)
        for pair in animation:
            pair[0].convert_alpha() if pair[0].get_alpha() else pair[0].convert()
        relative_path = file_path.relative_to(path / 'animations')
        animations[str(relative_path)] = animation
    return animations