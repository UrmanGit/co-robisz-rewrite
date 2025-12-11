"""Full-project global constants etc."""

import pathlib

# Constants
BASE_RESOLUTION: tuple[int, int] = (1920, 1080)
TITLE: str = "Co robisz? - rewrite (DEV)"
FPS: int = 60
DATA: pathlib.Path = pathlib.Path(__file__).parent.parent.parent / "data"
