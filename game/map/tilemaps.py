import pygame as pg
import game.core.assets as assets

# fmt: off
magazine_tilemap: list[list[int]] = [[1, 1, 2, 1],
                                     [0, 0, 0, 0],
                                     [0, 0, 0, 0],
                                     [3, 3, 3, 3]]
# fmt: on
magazine_tiles: dict[int, pg.Surface] = {}

# fmt: off
startroom_tilemap: list[list[int]] = [[1, 1, 1, 1, 1, 1],
                                      [0, 0, 0, 0, 0, 0],
                                      [0, 0, 0, 0, 0, 0],
                                      [4, 5, 5, 5, 5, 3]]
# fmt: on
startroom_tiles: dict[int, pg.Surface] = {}


def load_tiles() -> None:
    global magazine_tiles, startroom_tiles
    magazine_tiles = {
        0: assets.images["rooms/magazine/magazine_floor.png"],
        1: assets.images["rooms/magazine/magazine_wall.png"],
        2: assets.images["rooms/magazine/closed_magazine_door.png"],
        3: assets.images["outer_walls/hor.png"],
    }

    startroom_tiles = {
        5: assets.images["outer_walls/top.png"],
        0: assets.images["rooms/startroom/startroom_floor.png"],
        1: assets.images["rooms/startroom/startroom_wall.png"],
        2: assets.images["outer_walls/hor.png"],
        3: assets.images["outer_walls/hor l r ul ur uld.png"],
        4: assets.images["outer_walls/hor l r ul ur urd.png"],
    }
