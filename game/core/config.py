import pathlib

# Constants
BASE_RESOLUTION = (2560, 1440)
TITLE: str = "Co robisz? - rewrite (DEV)"
FPS: int = 60
DATA: pathlib.Path = pathlib.Path(__file__).parent.parent.parent / "data"

# Variables
window_size: tuple[int, int] = (1280, 720)