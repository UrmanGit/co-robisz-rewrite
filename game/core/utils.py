import pygame as pg
import pathlib
import game.core.config as cfg

def load_images(path: pathlib.Path) -> dict[str, pg.Surface]:
    images: dict[str, pg.Surface] = {}
    for path in (path / 'images').rglob("*.png"):
        image = pg.image.load(path)
        image = image.convert_alpha() if image.get_alpha() else image.convert()
        relative_path = path.relative_to(path / 'images')
        images[str(relative_path)] = image
    return images

def load_animations(path: pathlib.Path) -> dict[str, list[tuple[pg.Surface, float]]]:
    animations: dict[str, list[tuple[pg.Surface, float]]] = {}
    for path in (path / 'animations').rglob("*.gif"):
        animation = pg.image.load_animation(path)
        for pair in animation:
            pair[0].convert_alpha() if pair[0].get_alpha() else pair[0].convert()
        relative_path = path.relative_to(path / 'animations')
        animations[str(relative_path)] = animation
    return animations