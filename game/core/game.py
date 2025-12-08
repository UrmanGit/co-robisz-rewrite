import pygame as pg
pg.init()

import sys

import game.core.assets
import game.core.config
import game.core.window
from game.commons import *

class Game:
    def __init__(self) -> None:
        """Here you define the variables"""
        # Create a screen
        self.wm = game.core.window.WindowManager(game.core.config.BASE_RESOLUTION, False, pg.DOUBLEBUF | pg.SCALED)

        # Delayed image loading in assets
        game.core.assets.dict_images()
        game.core.assets.dict_animations()

        # Pygame stuff
        self.keys: ScancodeWrapper = pg.key.get_pressed()
        self.just_keys: ScancodeWrapper = pg.key.get_just_pressed()
        self.mouse: tuple[bool, bool, bool] = pg.mouse.get_pressed()
        self.just_mouse: tuple[bool, bool, bool, bool, bool] = pg.mouse.get_just_pressed()
        self.mouse_pos: tuple[int, int] = pg.mouse.get_pos()
        self.clock: pg.Clock = pg.time.Clock()

        # Set the window's caption and image
        pg.display.set_caption(game.core.config.TITLE)
        pg.display.set_icon(game.core.assets.image(game.core.config.DATA / "icon.png"))

        # Other stuff - to do later

    def events(self) -> None:
        """Here you do all the game events, like pressing keys and typing text."""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_F11:
                    self.wm.toggle_fullscreen()

    def update(self) -> None:
        """Here you do all the stuff that updates the variables, objects, state and everything."""
        self.clock.tick(game.core.config.FPS) # Framerate limit

        # Update the dynamic variables
        self.keys: ScancodeWrapper = pg.key.get_pressed()
        self.just_keys: ScancodeWrapper = pg.key.get_just_pressed()
        self.mouse: tuple[bool, bool, bool] = pg.mouse.get_pressed()
        self.just_mouse: tuple[bool, bool, bool, bool, bool] = pg.mouse.get_just_pressed()
        self.mouse_pos: tuple[int, int] = pg.mouse.get_pos()

    def draw(self) -> None:
        """Here you do all the drawing on the game window."""
        self.wm.screen.fill(pg.Color.from_hex("#0C0C12")) # Fill the background with a deep-dark-blue color
        pg.display.flip()

    def run(self) -> None:
        while True:
            self.events()
            self.update()
            self.draw()