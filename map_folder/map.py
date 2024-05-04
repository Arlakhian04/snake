import pygame as pg
import numpy as np
from map_folder.cell import Cell
from elements.apple import Apple
import random
from map_folder.map_const import *
from snake.snakeCell import *
from snake.snake import *

class Map:
    def __init__(self,size,position,cell_list,number_cell,apple,snake):
        """Initializer for the map

        Args:
            size (tuple): Contain the width and height of the map | HEIGHT X WIDTH
            position (tuple): Contain the position of the top-left corner of the map | X x Y
            cell_list (np.array(dtype = Cell)): List of cell
            number_cell (tuple): number of cell in x and in y | Y x X
            apple (Apple): apple
            snake (Snake):snake
        """
        self.size = size
        self.position = position
        self.cell_list = cell_list
        self.number_cell = number_cell
        self.apple = apple
        self.snake = snake

    def displayMap(self,screen):
        map_surface = pg.Surface((self.size[1],self.size[0]))
        for i in range(self.number_cell[0]):
            for j in range(self.number_cell[1]):
                self.cell_list[i][j].displayCell(map_surface)
        
        self.apple.displayApple(map_surface)
        self.snake.displaySnake(map_surface)
        screen.blit(map_surface,self.position)

def buildMap(SCREEN_HEIGHT,SCREEN_WIDTH):
    #Building the cell list
    cell_list = np.empty(shape = (number_cell[0],number_cell[1]), dtype = Cell)

    for i in range(number_cell[0]):
        for j in range(number_cell[1]):
            cell_color = (0,0,0)
            if((i + j) % 2 == 0):
                cell_color = (65,152,10)
            else:
                cell_color = (17,124,19)
            cell_list[i,j] = Cell((CELL_SIZE * j,CELL_SIZE * i), CELL_SIZE, False, cell_color,(i,j))

    map_size = (40 * 15, 40 * 17)
    map_position = (SCREEN_WIDTH / 2 - map_size[1] / 2, SCREEN_HEIGHT / 2 - map_size[0] / 2)

    apple = Apple((0,0))
    apple.change_location(cell_list)
    snake_init_index = (7,6)
    snake_init_pos = (snake_init_index[0] * CELL_SIZE,snake_init_index[1] * CELL_SIZE)
    snake_cell_list = np.empty(shape = (number_cell[0] * number_cell[1]),dtype = SnakeCell)
    snake_init_direction = (1,0)
    snake = Snake(snake_init_pos,snake_cell_list,snake_init_direction,0,snake_init_index)
    snake.addCell(snake_init_direction)
    snake.addCell(snake_init_direction)
    return Map(map_size,map_position,cell_list,number_cell,apple,snake)