"""Full-project global constants etc."""

import pathlib

# Constants
BASE_RESOLUTION: tuple[int, int] = (1920, 1080)
TITLE: str = "Co robisz? - rewrite (DEV)"
FPS: int = 180
DATA: pathlib.Path = pathlib.Path(__file__).parent.parent.parent / "data"
SCALE_FACTOR: int = 3
TILE_SIZE: int = 24 * SCALE_FACTOR
PLAYER_SPEED: int = 150
