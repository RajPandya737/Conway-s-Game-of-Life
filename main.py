import pygame as pg
import numpy as np
import os
import sys
from math import sqrt
from config import *
from grid import Map

os.environ["SDL_VIDEO_CENTERED"]='1'

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.caption = pg.display.set_caption('Game of Life')
        self.clock = pg.time.Clock()
        self.Grid = Map(WIDTH, HEIGHT, SCALER, OFFSET)
        self.Grid.rand_array()
        self.running = True
        


    def new(self):
        self.playing = True


    def update(self):
        self.clock.tick(FPS)
        self.screen.fill(BLACK)
        self.events()
        self.Grid.gameplay(ORANGE, WHITE, self.screen)
        pg.display.update()
        
        
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.playing = False
                self.running = False


    def main(self):
        #runs the game
        while self.playing is True:
            self.update()
        self.running = False


if __name__ == '__main__':
    game = Game()
    game.new()
    while game.running:
        game.main()

    pg.quit()
    sys.exit()





