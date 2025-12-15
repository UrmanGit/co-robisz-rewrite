from pygame import Vector2, Rect, Surface, draw
from pygame.typing import ColorLike


class BaseHitbox:
    def __init__(self, pos: tuple[int, int] | Vector2, size: tuple[int, int] | Vector2, color: ColorLike):
        self.pos: Vector2 = Vector2(pos)
        self.size: Vector2 = Vector2(size)
        self.color: ColorLike = color

        self.rect: Rect = Rect(self.pos, self.size)

    def draw(self, screen: Surface) -> None:
        draw.rect(screen, self.color, self.rect)


class RoomHitbox(BaseHitbox):
    def __init__(self, pos: tuple[int, int] | Vector2,
                 size: tuple[int, int] | Vector2,
                 color: ColorLike = "red"):
        BaseHitbox.__init__(self, pos, size, color)

    def draw(self, screen: Surface) -> None:
        draw.rect(screen, self.color, self.rect, 2)


class EntityHitbox(BaseHitbox):
    def __init__(self,
                 pos: tuple[int, int] | Vector2,
                 size: tuple[int, int] | Vector2,
                 color: ColorLike = "green") -> None:
        BaseHitbox.__init__(self, pos, size, color)

    def update(self, pos: tuple[int, int] | Vector2) -> None:
        self.pos = Vector2(pos)
        self.rect.pos = self.pos


class FurnitureHitbox(BaseHitbox):
    def __init__(self,
                 pos: tuple[int, int] | Vector2,
                 size: tuple[int, int] | Vector2
                 ) -> None:
        BaseHitbox.__init__(self, pos, size, "aqua")

    def move(self, pos: tuple[int, int] | Vector2) -> None:
        self.pos = Vector2(pos)
        self.rect.pos = self.pos
