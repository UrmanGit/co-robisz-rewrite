import game.core.utils
import game.core.config
import pygame as pg

images: dict[str, pg.Surface] = {}
animations: dict[str, list[tuple[pg.Surface, float]]] = {}

def dict_images() -> None:
    global images
    images = game.core.utils.load_images(game.core.config.DATA)

def dict_animations() -> None:
    global animations
    animations = game.core.utils.load_animations(game.core.config.DATA)

image = (lambda path: game.core.utils.load_image(path))