import pygame as pg

magazine_tilemap: list[list[int]] = [
    [1, 1, 2, 1],
    [0, 0, 0, 0],
    [3, 3, 3, 3]
]
magazine_tiles: dict[int, pg.Surface] | dict[int, None] = {
    1: None,
    2: None,
    3: None
}