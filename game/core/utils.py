import pygame as pg
pg.init()

import pathlib
from . import config as cfg

def load_image(path: pathlib.Path) -> pg.Surface:
    return pg.image.load(path)

def load_images(path: pathlib.Path) -> dict[str, pg.Surface]:
    images: dict[str, pg.Surface] = {}
    for path in (cfg.DATA / 'images').rglob("*.png"):
        image = load_image(path)
        image = image.convert_alpha() if image.get_alpha() else image.convert()
        relative_path = path.relative_to(cfg.DATA / 'images')
        images[str(relative_path)] = image
    return images