from game.core.utils import load_animations, load_images
from game.core.config import DATA
from pygame import Surface

images: dict[str, Surface] = load_images(DATA)
animations: dict[str, list[tuple[Surface, float]]] = load_animations(DATA)