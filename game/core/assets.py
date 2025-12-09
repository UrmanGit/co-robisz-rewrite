"""Asset registries and helpers for preloading game resources.

This module exposes two global dictionaries: `images` and `animations`,
which are populated by `dict_images()` and `dict_animations()` respectively.
It also provides the `image` alias for convenient single-image loading.
"""

import pygame as pg

from .config import DATA
from .utils import load_animations, load_image, load_images

# Global registries populated at runtime
images: dict[str, pg.Surface] = {}
animations: dict[str, list[tuple[pg.Surface, float]]] = {}

# Convenience alias for loading a single image
image = load_image


def dict_images() -> None:
    """Load and assign all PNG images to the global `images` dictionary."""
    global images
    images = load_images(DATA)


def dict_animations() -> None:
    """Load and assign all GIF animations to the global `animations` dictionary."""
    global animations
    animations = load_animations(DATA)
