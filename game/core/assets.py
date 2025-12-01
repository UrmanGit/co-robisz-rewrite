from game.core.utils import load_animations, load_images, load_image
from game.core.config import DATA
from pygame import Surface

images: dict[str, Surface] = load_images(DATA)
image = (lambda path: load_image(path))
animations: dict[str, list[tuple[Surface, float]]] = load_animations(DATA)