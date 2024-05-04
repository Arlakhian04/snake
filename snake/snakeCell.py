import pygame as pg
from map_folder.map_const import CELL_SIZE 

class SnakeCell:
    def __init__(self,position,previous_position,direction,previous_direction,index,previous_index,isLast):
        """Initializer for each cell of the snake

        Args:
            position (tuple): position of the cell
            previous_position (tuple): position of the previous cell
            direction (tuple): direction of the cell
            previous_direction (tuple): direction of the previous cell
            index (tuple): Index in the map call_list array
            isLast (bool): bool to know if it is the last cell in the list
        """
        self.position = position
        self.previous_position = previous_position
        self.direction = direction
        self.previous_direction = previous_direction
        self.index = index
        self.previous_index = previous_index
        self.isLast = isLast

    def move(self,previous_position,previous_direction,previous_index,map_cell_list):
        """Function to move the cell

        Args:
            previous_position (tuple): Position of the previous cell
            previous_direction (tuple): Direction of the previous cell
            previous_index (tuple): Index of the previous cell
            map_cell_list (np.array(dtype = Cell)): Array with all the cells of the map
        """
        map_cell_list[self.index[0],self.index[1]].isCellSnake = False
        self.position = self.previous_direction
        self.direction = self.previous_direction
        self.index = self.previous_index
        self.previous_position = previous_position
        self.previous_direction = previous_direction
        self.previous_index = previous_index
        map_cell_list[self.index[0],self.index[1]].isCellSnake = True

    def displayCellSnake(self,surface,color):
        pg.draw.rect(surface,color,(self.position[0],self.position[1], CELL_SIZE,CELL_SIZE))