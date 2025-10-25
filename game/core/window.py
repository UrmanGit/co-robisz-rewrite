import config as cfg
from ..commons import *
import pygame as pg

class WindowManager:
    def __init__(self, size: tuple[int, int], fullscreen: bool, flags: int, screen_resolution: tuple[int, int] = cfg.SCREEN_RESOLUTION):
        self.size: tuple[int, int] = size
        self.fullscreen: bool = fullscreen
        self.flags: int = flags
        self.screen_resolution: tuple[int, int] = screen_resolution
        self.screen: Surface = Surface(self.size if not self.fullscreen else self.screen_resolution,
                                       self.flags | (pg.FULLSCREEN if self.fullscreen else 0))

    def update_screen(self) -> None:
        self.screen: Surface = Surface(self.size if not self.fullscreen else self.screen_resolution,
                                       self.flags | (pg.FULLSCREEN if self.fullscreen else 0))

    def toggle_fullscreen(self):
        self.fullscreen = not self.fullscreen
        self.update_screen()

    def update(self, size: tuple[int, int] = None, screen_resolution: tuple[int, int] = cfg.SCREEN_RESOLUTION, fullscreen: bool = None, flags: int = None) -> None:
        self.size = size if size is not None else self.size
        self.screen_resolution = screen_resolution if screen_resolution is not None else self.screen_resolution
        self.fullscreen = fullscreen if fullscreen is not None else self.fullscreen
        self.flags = flags if flags is not None else self.flags
        self.update_screen()