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
        map_cell_list[self.index[1]][self.index[0]].isCellSnake = False
        #print("old position: " + str(self.position[0]) + " " + str(self.position[1]))
        self.position = self.previous_position
        #print("new position: " + str(self.position[0]) + " " + str(self.position[1]))
        #print("old direction: " + str(self.direction[0]) + " " + str(self.direction[1]))
        self.direction = self.previous_direction
        #print("new direction: " + str(self.direction[0]) + " " + str(self.direction[1]))
        #print("old index: " + str(self.index[0]) + " " + str(self.index[1]))
        self.index = self.previous_index
        #print("new index: " + str(self.index[0]) + " " + str(self.index[1]))
        self.previous_position = previous_position
        self.previous_direction = previous_direction
        self.previous_index = previous_index
        #print("new previous position: " + str(self.previous_position[0]) + " " + str(self.previous_position[1]))
        #print("new previous direction: " + str(self.previous_direction[0]) + " " + str(self.previous_direction[1]))
        #print("new previous index: " + str(self.previous_index[0]) + " " + str(self.previous_index[1]))
        map_cell_list[self.index[1]][self.index[0]].isCellSnake = True

    def displayCellSnake(self,surface,color):
        pg.draw.rect(surface,color,(self.position[0],self.position[1], CELL_SIZE,CELL_SIZE))