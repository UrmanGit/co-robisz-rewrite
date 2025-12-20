import pygame as pg
import game.collisions.hitbox as hitbox
from game.collisions.typing import Hitbox


class Movable:
    def __init__(self, pos: tuple[int, int] | pg.Vector2, speed: float) -> None:
        self.pos: pg.Vector2 = pg.Vector2(pos)
        self.speed: float = speed

    def move(self, new_pos: tuple[int, int] | pg.Vector2) -> None:
        self.pos = pg.Vector2(new_pos)

    def move_by(self, add_pos: tuple[int, int] | pg.Vector2) -> None:
        self.pos += pg.Vector2(add_pos)


class Animated:
    def __init__(self,
                 animations_dict: dict[str, list[tuple[pg.Surface, float]]]) -> None:
        self.animations_dict: dict[str, list[tuple[pg.Surface, float]]] = animations_dict
        self.current_animation: str = "down"
        self.current_frame: int = 0
        self.animation_frames: int = len(animations_dict[self.current_animation])
        self.current_delay: float = self.animations_dict[self.current_animation][self.current_frame][1]
        self.current_time = 0
        self.image = self.animations_dict[self.current_animation][self.current_frame][0]

    def animate(self, dt: float, animation: str) -> None:
        if animation not in self.animations_dict:
            raise KeyError(f"Animation {animation} is not in animations dict")

        if animation != self.current_animation:
            print(f"{self.current_animation = }")
            self.current_animation = animation

        self.current_delay: float = self.animations_dict[self.current_animation][self.current_frame][1]

        self.animation_frames: int = len(self.animations_dict[self.current_animation])

        self.current_time += dt
        if self.current_time >= self.current_delay:
            self.current_time = 0
            self.current_frame += 1
            if self.current_frame >= self.animation_frames:
                self.current_frame = 0
            self.image = self.animations_dict[self.current_animation][self.current_frame][0]


class Entity(Movable, Animated):
    def __init__(self,
                 pos: tuple[int, int] | pg.Vector2,
                 speed: float,
                 animations_dict: dict[str, list[tuple[pg.Surface, float]]]) -> None:
        Movable.__init__(self, pos, speed)
        Animated.__init__(self, animations_dict)

        hitbox_width = self.image.width - self.image.width // 4
        hitbox_height = self.image.height // 8

        hitbox_x = self.pos.x + (self.image.width - hitbox_width) // 2
        hitbox_y = self.pos.y + self.image.height - hitbox_height

        self.hitbox: Hitbox = hitbox.EntityHitbox(
            (int(hitbox_x), int(hitbox_y)),
            (hitbox_width, hitbox_height))

    def draw(self, screen: pg.Surface, visible_hitbox: bool = False) -> None:
        screen.blit(self.image, self.pos)
        if visible_hitbox:
            pg.draw.rect(screen, self.hitbox.color, self.hitbox.rect)

    def update(self, alter_pos: tuple[int, int] | pg.Vector2 | None = None) -> None:
        pos: tuple[int, int] | pg.Vector2 = pg.Vector2(alter_pos) if alter_pos is not None else self.pos
        hitbox_width = self.image.width - self.image.width // 4
        hitbox_height = self.image.height // 8

        hitbox_x = pos.x + (self.image.width - hitbox_width) // 2
        hitbox_y = pos.y + self.image.height - hitbox_height

        self.hitbox.update((int(hitbox_x), int(hitbox_y)))
