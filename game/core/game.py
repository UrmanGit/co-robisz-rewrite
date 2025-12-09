"""Core game loop and runtime state management.

This module defines the `Game` class which encapsulates the main loop and
handles events, updates, and drawing.
"""

import pygame as pg

pg.display.init()

import sys

import game.core.assets
import game.core.config
import game.core.window
from game.commons import *


class Game:
    """Container for game state and the main loop."""

    def __init__(self) -> None:
        """Initialize the game and create required resources."""
        # Create a screen
        self.wm = game.core.window.WindowManager(
            game.core.config.BASE_RESOLUTION, False, pg.DOUBLEBUF | pg.SCALED
        )

        # Delayed image loading in assets
        game.core.assets.dict_images()
        game.core.assets.dict_animations()

        # Pygame input and timing
        self.keys: ScancodeWrapper = pg.key.get_pressed()
        self.just_keys: ScancodeWrapper = pg.key.get_just_pressed()
        self.mouse: tuple[bool, bool, bool] = pg.mouse.get_pressed()
        self.just_mouse: tuple[bool, bool, bool, bool, bool] = (
            pg.mouse.get_just_pressed()
        )
        self.mouse_pos: tuple[int, int] = pg.mouse.get_pos()
        self.clock: pg.Clock = pg.time.Clock()

        # Set the window's caption and image
        pg.display.set_caption(game.core.config.TITLE)
        pg.display.set_icon(game.core.assets.image(game.core.config.DATA / "icon.png"))

        # Other stuff - to do later

    def events(self) -> None:
        """Process window and input events (keyboard, mouse, quit, etc.)."""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_F11:
                    self.wm.toggle_fullscreen()

    def update(self) -> None:
        """Update game state and timing."""
        self.clock.tick(game.core.config.FPS)  # Framerate limit

        # Update the dynamic variables
        self.keys: ScancodeWrapper = pg.key.get_pressed()
        self.just_keys: ScancodeWrapper = pg.key.get_just_pressed()
        self.mouse: tuple[bool, bool, bool] = pg.mouse.get_pressed()
        self.just_mouse: tuple[bool, bool, bool, bool, bool] = (
            pg.mouse.get_just_pressed()
        )
        self.mouse_pos: tuple[int, int] = pg.mouse.get_pos()

    def draw(self) -> None:
        """Render the frame to the game window."""
        # Fill the background with a deep-dark-blue color
        self.wm.screen.fill(pg.Color.from_hex("#0C0C12"))
        pg.display.flip()

    def run(self) -> None:
        """Execute the main game loop until the program exits."""
        while True:
            self.events()
            self.update()
            self.draw()
