from core.utils import load_animations, load_images, load_image
from core.config import DATA, SCALE_FACTOR
from pygame import Surface

images: dict[str, Surface] = {}
animations: dict[str, list[tuple[Surface, float]]] = {}


def dict_images() -> None:
    """Loads images to global `images` dict."""
    global images
    images = load_images(DATA / "images", SCALE_FACTOR)


def dict_animations() -> None:
    """Loads animations to global `animations` dict."""
    global animations
    animations = load_animations(DATA / "animations", SCALE_FACTOR)


# A shortcut for loading a single image.
def image(path, scale_factor: int = SCALE_FACTOR) -> Surface:
    """JiT-loads a single image."""
    an_image = load_image(path, scale_factor)
    return an_image
