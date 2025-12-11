from game.core.utils import load_animations, load_images, load_image
from game.core.config import DATA
from pygame import Surface

images: dict[str, Surface] = {}
animations: dict[str, list[tuple[Surface, float]]] = {}

def dict_images() -> None:
    global images
    images = load_images(DATA / "images")

def dict_animations() -> None:
    global animations
    animations = load_animations(DATA / "animations")

image = load_image