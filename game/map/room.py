import pygame as pg

import game.core.config as config
import game.collisions as collisions

from game.typing import Hitbox


class Room:
    def __init__(
        self,
        offset: tuple[int, int],
        tilemap: list[list[int]],
        tiles: dict[int, pg.Surface],
    ) -> None:
        self.pos: pg.Vector2 = pg.Vector2(offset)
        self.tilemap: list[list[int]] = tilemap
        self.tiles: dict[int, pg.Surface] = tiles
        self.hitbox: Hitbox = collisions.hitbox.RoomHitbox(
            (int(self.pos.x) + config.TILE_SIZE, int(self.pos.y) + config.TILE_SIZE),
            size = (config.TILE_SIZE * (len(tilemap[0]) - 2), config.TILE_SIZE * (len(tilemap) - 2)),
        )

    def draw(self, screen: pg.Surface, show_hitbox: bool = False) -> None:
        for i, row in enumerate(self.tilemap):
            for j, tile in enumerate(row):
                tile_left = self.pos.x + config.TILE_SIZE * j
                tile_top = self.pos.y + config.TILE_SIZE * i
                screen.blit(self.tiles[tile], (tile_left, tile_top))

        if show_hitbox:
            self.hitbox.draw(screen)
