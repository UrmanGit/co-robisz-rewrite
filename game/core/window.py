"""Window utilities for creating and managing the display surface."""

import pygame as pg
from game.commons import *


class WindowManager:
    """Simple wrapper around `pg.display.set_mode` with fullscreen toggle."""

    def __init__(
        self,
        size: tuple[int, int],
        _fullscreen: bool,
        flags: int,
        base_resolution: tuple[int, int] = BASE_RESOLUTION,
    ) -> None:
        """Create a game window.

        :param size: Initial window size.
        :param _fullscreen: Whether to start in fullscreen mode.
        :param flags: Pygame display flags for the window surface.
        :param base_resolution: Resolution used when `_fullscreen` is True.
        """
        self.size: tuple[int, int] = size
        self._fullscreen: bool = _fullscreen
        self.flags: int = flags
        self.base_resolution: tuple[int, int] = base_resolution
        self.screen: Surface = pg.display.set_mode(
            self.size if not self._fullscreen else self.base_resolution,
            self.flags | (pg.FULLSCREEN if self._fullscreen else 0),
        )

    def update_screen(self) -> None:
        """Update the game window surface to reflect current settings."""
        self.screen: Surface = pg.display.set_mode(
            self.size if not self._fullscreen else self.base_resolution,
            self.flags | (pg.FULLSCREEN if self._fullscreen else 0),
        )

    def toggle_fullscreen(self) -> None:
        """Toggle fullscreen mode.

        Note: resizable window mode is not currently supported.
        """
        self._fullscreen = not self._fullscreen
        self.update_screen()
