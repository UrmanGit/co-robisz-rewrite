import pyautogui

SIZE: tuple = (1600, 900)
FULLSCREEN_SIZE: tuple = pyautogui.size()

def scale_factor(screen_height: int) -> int:
    return int((screen_height * 3) / 1080)