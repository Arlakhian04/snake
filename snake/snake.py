from snake.snakeCell import SnakeCell
import pygame as pg
from map_folder.map_const import * 
class Snake:
    def __init__(self,position,cell_list,direction,size,index):
        """Initializer for the snake

        Args:
            position (tuple): Contains both the position x and y of the head of the snake in pixel
            cell_list (numpy array): Contains all the cells after the head
            direction (tuple): Contains the direction of the head in the x and y axis
            size (int): The size of the snake including the head
            index (tuple): Index in the map call_list array
        """
        self.position = position
        self.cell_list = cell_list
        self.direction = direction
        self.size = size
        self.index = index

    def addCell(self,direction):
        """Add a Cell to the cell_list
        """
        if(self.size == 0):
            position_cell = (self.position[0] - CELL_SIZE * self.direction[0],self.position[1] - CELL_SIZE * self.direction[1])
            index_cell = (self.index[0] - self.direction[0],self.index[1] - self.direction[1])
            self.cell_list[self.size] = SnakeCell(position_cell,self.position,self.direction,self.direction,index_cell,self.index,True)
            self.size += 1
        else:
            self.cell_list[self.size - 1].isLast = False
            previous_direction = self.cell_list[self.size - 1].direction
            previous_position = self.cell_list[self.size - 1].position
            position_cell_x = previous_position[0] - CELL_SIZE * previous_direction[0]
            position_cell_y = previous_position[1] - CELL_SIZE * previous_direction[1]
            position_cell = (position_cell_x,position_cell_y)
            previous_index = self.cell_list[self.size - 1].index
            index_cell_x = previous_index[0] - previous_direction[0]
            index_cell_y = previous_index[1] - previous_direction[1]
            index_cell = (index_cell_x,index_cell_y)
            self.cell_list[self.size] = SnakeCell(position_cell,previous_position,direction,previous_direction,index_cell,previous_index,True)
            self.size += 1

    def move(self,map_cell_list,apple):
        map_cell_list[self.index[0],self.index[1]].isCellSnake = False
        self.index = (self.index[0] + self.direction[0],self.index[1] + self.direction[1])
        map_cell_list[self.index[0],self.index[1]].isCellSnake = True

        self.cell_list[0].move(self.position,self.direction,self.index,map_cell_list)
        for i in range(1,self.size):
            self.cell_list[i].move(self.cell_list[i - 1].position,self.cell_list[i - 1].direction,self.cell_list[i - 1].index,map_cell_list)

        if apple.position == self.index:
            self.grow()

    def grow(self):
        self.addCell(self.cell_list[self.size].direction)

    def displaySnake(self,surface):
        color_body = (0,0,255)
        color_head = (190,190,190)
        pg.draw.rect(surface,color_head,(self.position[0],self.position[1], CELL_SIZE,CELL_SIZE))
        for i in range(self.size):
            self.cell_list[i].displayCellSnake(surface,color_body)
        