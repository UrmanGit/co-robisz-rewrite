import pygame as pg

pg.init()

import sys

import game.core.config as config
import game.core.utils as utils
from game.core.window import WindowManager
import game.core.assets as assets

import game.map.room
import game.map.tilemaps


class Game:
    """A game"""

    def __init__(self) -> None:
        """Here you define the variables"""
        # Create a screen
        self.wm = WindowManager(config.BASE_RESOLUTION, False, pg.DOUBLEBUF | pg.SCALED)

        # Delayed image loading in assets
        assets.dict_images()
        assets.dict_animations()

        # Other delayed loadings
        game.map.tilemaps.load_tiles()

        # Pygame stuff
        self.keys: pg.key.ScancodeWrapper = pg.key.get_pressed()
        self.just_keys: pg.key.ScancodeWrapper = pg.key.get_just_pressed()
        self.mouse: tuple[bool, bool, bool, bool, bool] = pg.mouse.get_pressed(5)
        self.just_mouse: tuple[bool, bool, bool, bool, bool] = (
            pg.mouse.get_just_pressed()
        )
        self.mouse_pos: tuple[int, int] = pg.mouse.get_pos()
        self.clock: pg.Clock = pg.time.Clock()

        # Window title and icon
        pg.display.set_caption(config.TITLE)
        pg.display.set_icon(assets.image(config.DATA / "icon.png"))

        # Main stuff
        self.magazine = game.map.room.Room(
            (config.BASE_RESOLUTION[0] // 2, config.BASE_RESOLUTION[1] // 2),
            tilemap=game.map.tilemaps.magazine_tilemap,
            tiles=game.map.tilemaps.magazine_tiles,
        )

    def events(self) -> None:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_F11:
                    self.wm.toggle_fullscreen()

    def update(self) -> None:
        self.clock.tick(config.FPS)

        self.keys: pg.key.ScancodeWrapper = pg.key.get_pressed()
        self.just_keys: pg.key.ScancodeWrapper = pg.key.get_just_pressed()
        self.mouse: tuple[bool, bool, bool] = pg.mouse.get_pressed()
        self.just_mouse: tuple[bool, bool, bool, bool, bool] = (
            pg.mouse.get_just_pressed()
        )
        self.mouse_pos: tuple[int, int] = pg.mouse.get_pos()

    def draw(self) -> None:
        self.wm.screen.fill(utils.hex_col("#0C0C12"))
        self.magazine.draw(screen=self.wm.screen)
        pg.display.flip()

    def run(self) -> None:
        while True:
            self.events()
            self.update()
            self.draw()
