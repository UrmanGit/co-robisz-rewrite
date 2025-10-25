import config as cfg
from ..commons import *
import pygame as pg

class WindowManager:
    def __init__(self, size: tuple[int, int], _fullscreen: bool, flags: int, screen_resolution: tuple[int, int] = cfg.SCREEN_RESOLUTION) -> None:
        """
        Creates a game window.

        :param size: Game window size
        :param _fullscreen: Defines if game window is _fullscreen
        :param flags: Flags used to make a pygame.Surface object
        :param screen_resolution: Screen resolution used when _fullscreen = True
        """
        self.size: tuple[int, int] = size
        self._fullscreen: bool = _fullscreen
        self.flags: int = flags
        self.screen_resolution: tuple[int, int] = screen_resolution
        self.screen: Surface = Surface(self.size if not self._fullscreen else self.screen_resolution,
                                       self.flags | (pg.FULLSCREEN if self._fullscreen else 0))

    def update_screen(self) -> None:
        self.screen: Surface = Surface(self.size if not self._fullscreen else self.screen_resolution,
                                       self.flags | (pg.FULLSCREEN if self._fullscreen else 0))

    def toggle__fullscreen(self) -> None:
        """
        Toggles _fullscreen mode.
        """
        self._fullscreen = not self._fullscreen
        self.update_screen()