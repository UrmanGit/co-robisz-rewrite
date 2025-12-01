import pygame as pg
pg.init()

import sys

from game.core.window import WindowManager as Wm
import game.core.config as cfg
from game.commons import *

class Game:
    def __init__(self) -> None:
        self.wm = Wm(cfg.window_size, True, pg.DOUBLEBUF | pg.SCALED)
        self.keys: ScancodeWrapper = pg.key.get_pressed()
        self.just_keys: ScancodeWrapper = pg.key.get_just_pressed()
        self.mouse: tuple[bool, bool, bool] = pg.mouse.get_pressed()
        self.just_mouse: tuple[bool, bool, bool, bool, bool] = pg.mouse.get_just_pressed()
        self.mouse_pos: tuple[int, int] = pg.mouse.get_pos()
        self.clock: pg.Clock = pg.time.Clock()
        pg.display.set_caption(cfg.TITLE)
        import game.core.assets as ast
        pg.display.set_icon(ast.image(cfg.DATA / "ikona.png"))

    def events(self) -> None:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_F11:
                    self.wm.toggle_fullscreen()

    def update(self) -> None:
        self.clock.tick(cfg.FPS)

        self.keys: ScancodeWrapper = pg.key.get_pressed()
        self.just_keys: ScancodeWrapper = pg.key.get_just_pressed()
        self.mouse: tuple[bool, bool, bool] = pg.mouse.get_pressed()
        self.just_mouse: tuple[bool, bool, bool, bool, bool] = pg.mouse.get_just_pressed()
        self.mouse_pos: tuple[int, int] = pg.mouse.get_pos()

    def draw(self) -> None:
        self.wm.screen.fill((100, 100, 100))
        pg.display.flip()

    def run(self) -> None:
        while True:
            self.events()
            self.update()
            self.draw()