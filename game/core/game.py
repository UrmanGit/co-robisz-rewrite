import pygame as pg
pg.init()

import sys

from game.commons import *
import game.core.config as config
import game.core.utils as utils
from game.core.window import WindowManager
import game.core.assets as assets

class Game:
    def __init__(self) -> None:
        """Here you define the variables"""
        # Create a screen
        self.wm = WindowManager(config.BASE_RESOLUTION, False, pg.DOUBLEBUF | pg.SCALED)

        # Delayed image loading in assets
        assets.dict_images()
        assets.dict_animations()

        # Pygame stuff
        self.keys: ScancodeWrapper = pg.key.get_pressed()
        self.just_keys: ScancodeWrapper = pg.key.get_just_pressed()
        self.mouse: tuple[bool, bool, bool] = pg.mouse.get_pressed()
        self.just_mouse: tuple[bool, bool, bool, bool, bool] = pg.mouse.get_just_pressed()
        self.mouse_pos: tuple[int, int] = pg.mouse.get_pos()
        self.clock: pg.Clock = pg.time.Clock()
        pg.display.set_caption(config.TITLE)
        import game.core.assets as ast
        pg.display.set_icon(ast.image(config.DATA / "icon.png"))

    def events(self) -> None:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_F11:
                    self.wm.toggle_fullscreen()

    def update(self) -> None:
        self.clock.tick(config.FPS)

        self.keys: ScancodeWrapper = pg.key.get_pressed()
        self.just_keys: ScancodeWrapper = pg.key.get_just_pressed()
        self.mouse: tuple[bool, bool, bool] = pg.mouse.get_pressed()
        self.just_mouse: tuple[bool, bool, bool, bool, bool] = pg.mouse.get_just_pressed()
        self.mouse_pos: tuple[int, int] = pg.mouse.get_pos()

    def draw(self) -> None:
        self.wm.screen.fill(utils.hex_col("#0C0C12"))
        pg.display.flip()

    def run(self) -> None:
        while True:
            self.events()
            self.update()
            self.draw()