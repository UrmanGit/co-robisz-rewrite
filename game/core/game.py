import pygame as pg

from .window import WindowManager as wm
import config as cfg
from ..commons import *

class Game:
    def __init__(self) -> None:
        self.screen = wm(cfg.window_size, False, pg.DOUBLEBUF)
        self.keys: ScancodeWrapper = pg.key.get_pressed()
        self.just_keys: ScancodeWrapper = pg.key.get_just_pressed()
        self.mouse: tuple = pg.mouse.get_pressed()
        self.just_mouse: tuple = pg.mouse.get_just_pressed()
        self.mouse_pos: tuple[int, int] = pg.mouse.get_pos()
        self.clock: pg.Clock = pg.time.Clock()
