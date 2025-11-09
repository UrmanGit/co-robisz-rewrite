from pathlib import Path
import pygame as pg
from pprint import pprint
pg.init()

# display = pg.display.set_mode((800, 600))

from game.core.utils import load_images
from game.core.config import DATA

example = load_images(DATA)
#pprint(example)