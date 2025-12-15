from . import hitbox
import typing


T = typing.TypeVar("T", bound=hitbox.BaseHitbox)
Hitbox = T
