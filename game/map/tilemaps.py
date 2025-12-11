import pygame as pg
import game.core.assets as assets

magazine_tilemap: list[list[int]] = [[1, 1, 2, 1],
                                     [0, 0, 0, 0],
                                     [3, 3, 3, 3]]
magazine_tiles: dict[int, pg.Surface] = {}


def load_tiles() -> None:
    global magazine_tiles
    magazine_tiles = {
        0: assets.images["rooms/magazine/magazine_floor.png"],
        1: assets.images["rooms/magazine/magazine_wall.png"],
        2: assets.images["rooms/magazine/closed_magazine_door.png"],
        3: assets.images["outer_walls/hor.png"],
    }
