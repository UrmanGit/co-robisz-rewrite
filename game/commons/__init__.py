"""Commonly used types and aliases re-exported for convenience."""


from pygame.key import ScancodeWrapper
from pygame.mask import Mask
from pygame.math import Vector2 as v2
from pygame.rect import FRect, Rect
from pygame.surface import Surface
from pygame.typing import ColorLike, RectLike

from ..core.config import BASE_RESOLUTION

__all__ = [
    "v2",
    "Rect",
    "FRect",
    "Surface",
    "Mask",
    "ColorLike",
    "RectLike",
    "ScancodeWrapper",
    "BASE_RESOLUTION",
]
