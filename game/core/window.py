import game.core.config
from game.commons import *
import pygame as pg

class WindowManager:
    def __init__(self, size: tuple[int, int], _fullscreen: bool, flags: int, base_resolution: tuple[int, int] = game.core.config.BASE_RESOLUTION) -> None:
        """
        Creates a game window.

        :param size: Game window size
        :param _fullscreen: Defines if game window is _fullscreen
        :param flags: Flags used to make a pygame.Surface object
        :param base_resolution: Screen resolution used when _fullscreen = True
        """
        self.size: tuple[int, int] = size
        self._fullscreen: bool = _fullscreen
        self.flags: int = flags
        self.base_resolution: tuple[int, int] = base_resolution
        self.screen: Surface = pg.display.set_mode(self.size if not self._fullscreen else self.base_resolution,
                                                   self.flags | (pg.FULLSCREEN if self._fullscreen else 0))

    def update_screen(self) -> None:
        """Updates the game window."""
        self.screen: Surface = pg.display.set_mode(self.size if not self._fullscreen else self.base_resolution,
                                                   self.flags | (pg.FULLSCREEN if self._fullscreen else 0))

    def toggle_fullscreen(self) -> None:
        """Toggles fullscreen mode. Currently, doesn't support resizable window."""
        self._fullscreen = not self._fullscreen
        self.update_screen()