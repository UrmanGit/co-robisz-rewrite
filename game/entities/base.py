from pygame.math import Vector2


class Movable:
    def __init__(self, pos: tuple[int, int] | Vector2, speed: int) -> None:
        self.pos: Vector2 = Vector2(pos)
        self.speed: int = speed

    def move(self):
        ... # Todo: Add move function that checks for collisions with hitbox. Add hitboxes 💀

