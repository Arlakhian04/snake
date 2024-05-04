import pygame as pg
from map_folder.map_const import * 
import random
class Apple:
    def __init__(self,position):
        """Initializer for Apple

        Args:
            position (tuple): position given as index in the cell_list of map | X x Y
            cell_size (int): size of the cells
        """
        self.position = position

    def displayApple(self,surface):
        position_on_map = (CELL_SIZE * self.position[0] + int(CELL_SIZE / 2),CELL_SIZE * self.position[1] + int(CELL_SIZE / 2))
        pg.draw.circle(surface,(255,0,0),position_on_map,int(CELL_SIZE / 3))

    def change_location(self,cell_list):
        self.position = (-1,-1)
        while self.position[0] == -1:
            x = random.randint(1,number_cell[1] - 1)
            y = random.randint(1,number_cell[0] - 1)
            if(not cell_list[y][x].isCellSnake):
                self.position = (x,y)
                print (str(self.position))
        