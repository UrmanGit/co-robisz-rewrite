"""Project-wide configuration constants.

These values define the default resolution, window title, target FPS, and the
base path to the `data` directory containing assets.
"""

import pathlib

# Constants
BASE_RESOLUTION: tuple[int, int] = (1920, 1080)
TITLE: str = "Co robisz? - rewrite (DEV)"
FPS: int = 60
DATA: pathlib.Path = pathlib.Path(__file__).parent.parent.parent / "data"
