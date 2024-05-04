import pygame as pg
import numpy as np
from map_folder.map import buildMap

pg.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

screen = pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pg.display.set_caption('Snake')

screen.fill((0,0,0))

map_snake = buildMap(SCREEN_HEIGHT,SCREEN_WIDTH)

clock = pg.time.Clock()

run = True
while run:

    map_snake.displayMap(screen)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    pg.display.update()
    clock.tick(60)
pg.quit()