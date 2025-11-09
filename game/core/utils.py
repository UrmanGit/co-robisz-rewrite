import pygame as pg
pg.init()

import pathlib
from . import config as cfg

def load_images(path: pathlib.Path) -> dict[str, pg.Surface]:
    images: dict[str, pg.Surface] = {}
    for path in (cfg.DATA / 'images').rglob("*.png"):
        image = pg.image.load(path)
        image = image.convert_alpha() if image.get_alpha() else image.convert()
        relative_path = path.relative_to(cfg.DATA / 'images')
        images[str(relative_path)] = image
    return images

def load_animations(path: pathlib.Path) -> dict[str, list[tuple[pg.Surface, float]]]:
    animations: dict[str, list[tuple[pg.Surface, float]]] = {}
    for path in (cfg.DATA / 'animations').rglob("*.gif"):
        animation = pg.image.load_animation(path)
        for pair in animation:
            pair[0].convert_alpha() if pair[0].get_alpha() else pair[0].convert()
        animations[str(path.relative_to(cfg.DATA / 'animations'))] = animation
    return animations