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
        room_pos_x: int = self.wm.screen.width // 2 - len(game.map.tilemaps.magazine_tilemap[0]) * config.TILE_SIZE // 2
        room_pos_y: int = int(self.wm.screen.height // 1.25 - len(game.map.tilemaps.magazine_tilemap) * config.TILE_SIZE // 2)

        self.magazine = game.map.room.Room(
            offset = (room_pos_x, room_pos_y),
            tilemap = game.map.tilemaps.magazine_tilemap,
            tiles = game.map.tilemaps.magazine_tiles
        )

        room_pos_x = self.wm.screen.width // 2 - len(game.map.tilemaps.startroom_tilemap[0]) * config.TILE_SIZE // 2
        room_pos_y = room_pos_y - (len(game.map.tilemaps.startroom_tilemap) - 1) * config.TILE_SIZE - 5 * config.SCALE_FACTOR

        self.startroom = game.map.room.Room(
            offset = (room_pos_x, room_pos_y),
            tilemap = game.map.tilemaps.startroom_tilemap,
            tiles = game.map.tilemaps.startroom_tiles
        )

    def events(self) -> None:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_F11:
                    self.wm.toggle_fullscreen()

    def update(self) -> None:
        dt: int = self.clock.tick(config.FPS)

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
        self.startroom.draw(screen=self.wm.screen)
        pg.display.flip()

    def run(self) -> None:
        while True:
            self.events()
            self.update()
            self.draw()
