import pathlib

import pyautogui

# Constants
SCREEN_RESOLUTION: pyautogui.Size = pyautogui.size()
TITLE: str = "Co robisz? - rewrite"
FPS: int = 60
DATA: pathlib.Path = pathlib.Path(__file__).parent.parent.parent / "data"

# Variables
window_size: tuple[int, int] = (1600, 900)