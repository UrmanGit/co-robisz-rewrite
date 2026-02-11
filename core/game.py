import pygame as pg
pg.init()

import sys

# Game and code assets
import core.config as config
import core.utils as utils
from core.window import WindowManager
import core.assets as assets

# Game stuff
import map.room
import map.tilemaps
import entities.player as player


class Game:
    """A game"""

    def __init__(self) -> None:
        # Create a screen
        self.wm = WindowManager(config.BASE_RESOLUTION, False, pg.DOUBLEBUF | pg.SCALED)

        # Delayed image loading in assets
        assets.dict_images()
        assets.dict_animations()

        # Other delayed loadings
        map.tilemaps.load_tiles()

        # Pygame stuff
        self.keys: pg.key.ScancodeWrapper = pg.key.get_pressed()
        self.just_keys: pg.key.ScancodeWrapper = pg.key.get_just_pressed()
        self.mouse: tuple[bool, bool, bool, bool, bool] = pg.mouse.get_pressed(5) # type: ignore
        self.just_mouse: tuple[bool, bool, bool, bool, bool] = (
            pg.mouse.get_just_pressed()
        )
        self.mouse_pos: tuple[int, int] = pg.mouse.get_pos()
        self.clock: pg.Clock = pg.time.Clock()

        # Window title and icon
        pg.display.set_caption(config.TITLE)
        pg.display.set_icon(assets.image(config.DATA / "icon.png"))

        # Game stuff
        room_pos_x: int = (
            self.wm.screen.width // 2
            - len(map.tilemaps.magazine_tilemap[0]) * config.TILE_SIZE // 2
        )
        room_pos_y: int = int(
            self.wm.screen.height // 1.25
            - len(map.tilemaps.magazine_tilemap) * config.TILE_SIZE // 2
        )

        self.magazine = map.room.Room(
            offset=(room_pos_x, room_pos_y),
            tilemap=map.tilemaps.magazine_tilemap,
            tiles=map.tilemaps.magazine_tiles,
        )

        room_pos_x = (
            self.wm.screen.width // 2
            - len(map.tilemaps.startroom_tilemap[0]) * config.TILE_SIZE // 2
        )
        room_pos_y = (
            room_pos_y
            - (len(map.tilemaps.startroom_tilemap) - 1) * config.TILE_SIZE
            - 5 * config.SCALE_FACTOR
        )

        self.startroom = map.room.Room(
            offset=(room_pos_x, room_pos_y),
            tilemap=map.tilemaps.startroom_tilemap,
            tiles=map.tilemaps.startroom_tiles,
        )

        player_animations_dict: dict[str, list[tuple[pg.Surface, float]]] = {}
        for key in assets.animations:
            new_key = key.split("/")[1].split(".")[0]
            player_animations_dict[new_key] = assets.animations[key]

        self.player = player.Player(
            self.magazine.hitbox.pos + self.magazine.hitbox.size // 2,
            config.PLAYER_SPEED,
            player_animations_dict,
        )

    def events(self) -> None:
        for event in pg.event.get():
            # Quitting the game
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                sys.exit()

            # Keys handling
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_F11:
                    self.wm.toggle_fullscreen()

    def update(self) -> None:
        # Delta time
        dt: int = self.clock.tick(config.FPS)

        # Pygame stuff updating
        self.keys: pg.key.ScancodeWrapper = pg.key.get_pressed()
        self.just_keys: pg.key.ScancodeWrapper = pg.key.get_just_pressed()
        self.mouse: tuple[bool, bool, bool] = pg.mouse.get_pressed()
        self.just_mouse: tuple[bool, bool, bool, bool, bool] = (
            pg.mouse.get_just_pressed()
        )
        self.mouse_pos: tuple[int, int] = pg.mouse.get_pos()

        # Player
        self.player.moving(self.keys, dt, self.magazine)
        self.player.update()

    def draw(self) -> None:
        # Fill the screen with a cool color
        self.wm.screen.fill(utils.hex_col("#0C0C12"))

        # Rooms
        self.startroom.draw(self.wm.screen)
        self.magazine.draw(self.wm.screen)

        # Player
        self.player.draw(self.wm.screen)

        # Update the screen
        pg.display.flip()

    def run(self) -> None:
        # Game loop
        while True:
            self.events()
            self.update()
            self.draw()
