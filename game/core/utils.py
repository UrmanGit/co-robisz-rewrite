import pygame as pg
pg.init()

import pathlib

def load_image(path: pathlib.Path) -> pg.Surface:
    return pg.image.load(path)

def load_images(path: pathlib.Path) -> dict[str, pg.Surface]:
    ...