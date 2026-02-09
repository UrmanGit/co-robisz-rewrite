import pygame as pg
import core.assets as assets

# fmt: off
magazine_tilemap: list[list[int]] = [[-4, 1, 1, 2, 1, 4],
                                     [-4, 0, 0, 0, 0, 4],
                                     [-4, 0, 0, 0, 0, 4],
                                     [-5, 3, 3, 3, 3, 5]]
# fmt: on
magazine_tiles: dict[int, pg.Surface] = {}

# fmt: off
startroom_tilemap: list[list[int]] = [[-8, 2, 2, 2, 2, 2, 2, 2, 2, 8],
                                      [-4, 1, 1, 1, 1, 1, 1, 1, 1, 4],
                                      [-4, 0, 0, 0, 0, 0, 0, 0, 0, 4],
                                      [-4, 0, 0, 0, 0, 0, 0, 0, 0, 4],
                                      [-4, 0, 0, 0, 0, 0, 0, 0, 0, 4],
                                      [-6, 3, -7, 3, 3, 3, 3, 7, 3, 6]]
# fmt: on
startroom_tiles: dict[int, pg.Surface] = {}


def load_tiles() -> None:
    global magazine_tiles, startroom_tiles
    magazine_tiles = {
        0: assets.images["rooms/magazine/magazine_floor.png"],
        1: assets.images["rooms/magazine/magazine_wall.png"],
        2: assets.images["rooms/magazine/closed_magazine_door.png"],
        3: assets.images["outer_walls/hor.png"],
        -4: assets.images["outer_walls/l vert.png"],
        4: assets.images["outer_walls/r vert.png"],
        -5: assets.images["outer_walls/vert r u ur.png"],
        5: assets.images["outer_walls/vert l u ul.png"],
    }

    startroom_tiles = {
        0: assets.images["rooms/startroom/startroom_floor.png"],
        1: assets.images["rooms/startroom/startroom_wall.png"],
        2: assets.images["outer_walls/u top.png"],
        3: assets.images["outer_walls/hor.png"],
        -4: assets.images["outer_walls/l vert.png"],
        4: assets.images["outer_walls/r vert.png"],
        -6: assets.images["outer_walls/vert r u ur.png"],
        6: assets.images["outer_walls/vert l u ul.png"],
        -7: assets.images["outer_walls/hor l r ul ur urd.png"],
        7: assets.images["outer_walls/hor l r ul ur uld.png"],
        -8: assets.images["outer_walls/corner r d.png"],
        8: assets.images["outer_walls/corner l d.png"],
    }
