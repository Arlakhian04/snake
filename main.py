import pygame as pg
import numpy as np
from map_folder.map import *
from snake.snake import Snake
from map_folder.map_const import *
from snake.snakeCell import *

pg.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

screen = pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pg.display.set_caption('Snake')

screen.fill((0,0,0))

map_snake = buildMap(SCREEN_HEIGHT,SCREEN_WIDTH)

clock = pg.time.Clock()

run = True
started = False
timer = 0
next_direction = map_snake.snake.direction
reset = False
while run:

    map_snake.displayMap(screen)

    #Winning
    if map_snake.snake.size == (map_snake.size[0] * map_snake.size[1] - 1):
        run = False

    key = pg.key.get_pressed()
    if (key[pg.K_r] and started) or reset:
        map_snake = buildMap(SCREEN_HEIGHT,SCREEN_WIDTH)
        started = False
        timer = 0
        reset = False
    if key[pg.K_d] and map_snake.snake.direction != (-1,0):
        next_direction = (1,0)
        started = True
    elif key[pg.K_a] and map_snake.snake.direction != (1,0):
        next_direction = (-1,0)
        started = True
    elif key[pg.K_s] and map_snake.snake.direction != (0,-1):
        next_direction = (0,1)
        started = True
    elif key[pg.K_w] and map_snake.snake.direction != (0,1):
        next_direction = (0,-1)
        started = True
    
    if timer >= 10 and not started:
        map_snake.snake.direction = next_direction
        if(not map_snake.snake.move(map_snake.cell_list,map_snake.apple)):
            reset = True
            index = map_snake.snake.index
            #print(str(index))
            #print(str(map_snake.cell_list[index[1]][index[0]].isCellSnake))
        timer = 0
        next_direction = map_snake.snake.direction

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    pg.display.update()
    clock.tick(6 * 16)
    if timer % 100 == 0:
        print(str(timer))
    timer += 1
pg.quit()