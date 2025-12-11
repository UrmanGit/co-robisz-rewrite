import pygame as pg

import game.core.config as config


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
        self.hitbox: pg.Rect = pg.Rect(
            self.pos,
            (config.TILE_SIZE * len(tilemap[0]), config.TILE_SIZE * len(tilemap)),
        )

    def draw(self, screen: pg.Surface) -> None:
        for i, row in enumerate(self.tilemap):
            for j, tile in enumerate(row):
                tile_left = self.pos.x + config.TILE_SIZE * j
                tile_top = self.pos.y + config.TILE_SIZE * i
                screen.blit(self.tiles[tile], (tile_left, tile_top))
