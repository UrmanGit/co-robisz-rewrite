from builtins import *
import pygame as pg
import config as cfg

class Game:
    def __init__(self):
        self.screen: pg.Surface = pg.display.set_mode(cfg.SIZE, pg.DOUBLEBUF)
        self.clock: pg.Clock = pg.time.Clock()
        # Changing variables
        self.keys: pg.key.ScancodeWrapper = pg.key.get_pressed()
        self.just_keys: pg.key.ScancodeWrapper = pg.key.get_just_pressed()
        self.mouse: tuple = pg.mouse.get_pressed()
        self.just_mouse: tuple = pg.mouse.get_just_pressed()
        self.mouse_pos: tuple = pg.mouse.get_pos()

        self.running: bool = True

    def events(self) -> None:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                self.running = False

    def update(self) -> None:
        self.clock.tick(60)

        # Updating the variables
        self.keys = pg.key.get_pressed()
        self.just_keys = pg.key.get_just_pressed()
        self.mouse = pg.mouse.get_pressed()
        self.just_mouse = pg.mouse.get_just_pressed()
        self.mouse_pos = pg.mouse.get_pos()

    def draw(self) -> None:
        self.screen.fill((80, 80, 80))
        pg.display.flip()

    def main(self) -> None:
        while self.running:
            self.events()
            self.update()
            self.draw()

    def run(self) -> None:
        pg.init()
        self.main()

if __name__ == "__main__":
    game: Game = Game()
    game.run()
