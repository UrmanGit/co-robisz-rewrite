import pygame as pg

from .config import window_size
from ..commons import *

class Game:
    def __init__(self) -> None:
        self.screen = pg.display.set_mode(window_size, pg.DOUBLEBUF | pg.RESIZABLE)
        self.keys: ScancodeWrapper = pg.key.get_pressed()
        self.just_keys: ScancodeWrapper = pg.key.get_just_pressed()
        self.mouse: tuple = pg.mouse.get_pressed()
        self.just_mouse: tuple = pg.mouse.get_just_pressed()
        self.mouse_pos: tuple[int, int] = pg.mouse.get_pos()
        self.clock: pg.Clock = pg.time.Clock()