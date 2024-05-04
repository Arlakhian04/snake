import pygame as pg
import numpy as np
from map_folder.cell import Cell

class Map:
    def __init__(self,size,position,cell_list,number_cell):
        """Initializer for the map

        Args:
            size (tuple): Contain the width and height of the map | HEIGHT X WIDTH
            position (tuple): Contain the position of the top-left corner of the map | X x Y
            cell_list (np.array(dtype = Cell)): List of cell
            number_cell (tuple): number of cell in x and in y | Y x X
        """
        self.size = size
        self.position = position
        self.cell_list = cell_list
        self.number_cell = number_cell

    def displayMap(self,screen):
        map_surface = pg.Surface((self.size[1],self.size[0]))
        for i in range(self.number_cell[0]):
            for j in range(self.number_cell[1]):
                #map_surface.blit(self.cell_list[i][j].displayCell(map_surface),(self.cell_list[i][j].position[0],self.cell_list[i][j].position[1]))
                self.cell_list[i][j].displayCell(map_surface)
                
        screen.blit(map_surface,self.position)

def buildMap(SCREEN_HEIGHT,SCREEN_WIDTH):
    #Building the cell list
    number_cell = (15,17) #height x width
    cell_size = 40
    cell_list = np.empty(shape = (number_cell[0],number_cell[1]), dtype = Cell)

    for i in range(number_cell[0]):
        for j in range(number_cell[1]):
            cell_color = (0,0,0)
            if((i + j) % 2 == 0):
                cell_color = (65,152,10)
            else:
                cell_color = (17,124,19)
            cell_list[i,j] = Cell((cell_size * j,cell_size * i), cell_size, False, cell_color,(i,j))

    map_size = (40 * 15, 40 * 17)
    map_position = (SCREEN_WIDTH / 2 - map_size[1] / 2, SCREEN_HEIGHT / 2 - map_size[0] / 2)
    return Map(map_size,map_position,cell_list,number_cell)