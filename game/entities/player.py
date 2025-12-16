from . import base
import pygame as pg
import game.map.room as room
from math import sqrt


class Player(base.Entity):
    def __init__(self, pos, speed, animations_dict) -> None:
        super().__init__(pos, speed, animations_dict)

    def moving(self, keys: pg.key.ScancodeWrapper, dt: float, current_room: room.Room):
        speed = self.speed * (dt / 1000)

        room_hitbox = current_room.hitbox.rect

        new_pos: pg.Vector2 = pg.Vector2(0, 0)
        up: bool = keys[pg.K_w]
        down: bool = keys[pg.K_s]
        left: bool = keys[pg.K_a]
        right: bool = keys[pg.K_d]

        animation = False
        if up and not (left or right or down):
            new_pos = pg.Vector2(0, -speed)
            self.current_animation = "up"
            animation = True
        elif down and not (left or right or up):
            new_pos = pg.Vector2(0, speed)
            self.current_animation = "down"
            animation = True
        elif left and not (right or up or down):
            new_pos = pg.Vector2(-speed, 0)
            self.current_animation = "left"
            animation = True
        elif right and not (left or up or down):
            new_pos = pg.Vector2(speed, 0)
            self.current_animation = "right"
            animation = True
        elif up and right and not (left or down):
            new_pos = pg.Vector2(speed, -speed) / sqrt(2)
            self.current_animation = "rightup"
            animation = True
        elif down and right and not (left or up):
            new_pos = pg.Vector2(speed, speed) / sqrt(2)
            self.current_animation = "rightdown"
            animation = True
        elif up and left and not (right or down):
            new_pos = pg.Vector2(-speed, -speed) / sqrt(2)
            self.current_animation = "leftup"
            animation = True
        elif down and left and not (right or up):
            new_pos = pg.Vector2(-speed, speed) / sqrt(2)
            self.current_animation = "leftdown"
            animation = True
        else:
            self.image = self.animations_dict[self.current_animation][0][0]

        if animation:
            self.animate(dt, self.current_animation)

        future_pos = self.pos + new_pos
        self.update(future_pos)

        if room_hitbox.right < self.hitbox.rect.right or self.hitbox.rect.left < room_hitbox.left: new_pos.x = 0
        if room_hitbox.bottom < self.hitbox.rect.bottom or self.hitbox.rect.top < room_hitbox.top: new_pos.y = 0

        future_pos = self.pos + new_pos
        self.pos = future_pos
        self.update(future_pos)
