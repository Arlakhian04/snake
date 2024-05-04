from snake.snakeCell import SnakeCell
import pygame as pg
from map_folder.map_const import * 
class Snake:
    def __init__(self,position,cell_list,direction,size,index,apple_eaten):
        """Initializer for the snake

        Args:
            position (tuple): Contains both the position x and y of the head of the snake in pixel
            cell_list (numpy array): Contains all the cells after the head
            direction (tuple): Contains the direction of the head in the x and y axis
            size (int): The size of the snake including the head
            index (tuple): Index in the map call_list array
            apple_eaten (int): Number of apple eaten
        """
        self.position = position
        self.cell_list = cell_list
        self.direction = direction
        self.size = size
        self.index = index
        self.apple_eaten = apple_eaten

    def addCell(self,direction,map_cell_list):
        """Add a Cell to the cell_list
        """
        if(self.size == 0):
            position_cell = (self.position[0] - CELL_SIZE * self.direction[0],self.position[1] - CELL_SIZE * self.direction[1])
            index_cell = (self.index[0] - self.direction[0],self.index[1] - self.direction[1])
            #print("position cell :" + " " + str(position_cell[0]) + " " + str(position_cell[1]))
            #print("index cell: " + str(index_cell[0]) + " " + str(index_cell[1]))
            self.cell_list[self.size] = SnakeCell(position_cell,self.position,self.direction,self.direction,index_cell,self.index,True)
            self.size += 1
        else:
            self.cell_list[self.size - 1].isLast = False
            previous_direction = self.cell_list[self.size - 1].direction
            previous_position = self.cell_list[self.size - 1].position
            position_cell_x = previous_position[0] - CELL_SIZE * previous_direction[0]
            position_cell_y = previous_position[1] - CELL_SIZE * previous_direction[1]
            position_cell = (position_cell_x,position_cell_y)
            #print("position cell :" + " " + str(position_cell_x) + " " + str(position_cell_y))
            previous_index = self.cell_list[self.size - 1].index
            index_cell_x = previous_index[0] - previous_direction[0]
            index_cell_y = previous_index[1] - previous_direction[1]
            index_cell = (index_cell_x,index_cell_y)
            #print ("previous_index: " + str(previous_index))
            #print("index cell: " + str(index_cell_x) + " " + str(index_cell_y))
            self.cell_list[self.size] = SnakeCell(position_cell,previous_position,direction,previous_direction,index_cell,previous_index,True)
            self.size += 1
        
        map_cell_list[index_cell[1]][index_cell[0]].isCellSnake = True

    def move(self,map_cell_list,apple):
        """_summary_

        Args:
            map_cell_list (_type_): _description_
            apple (_type_): _description_

        Returns:
            boolean: True if the snake didn't collide with anything and False if it collided
        """
        map_cell_list[self.index[1]][self.index[0]].isCellSnake = False
        self.index = (self.index[0] + self.direction[0],self.index[1] + self.direction[1])
        if(self.index[0] >= number_cell[1] or self.index[1] >= number_cell[0] or self.index[0] < 0 or self.index[1] < 0):
            return False
        if(map_cell_list[self.index[1]][self.index[0]].isCellSnake):
            if(self.cell_list[self.size - 1].index != self.index):
                return False
        map_cell_list[self.index[1]][self.index[0]].isCellSnake = True
        if apple.position == self.index:
            self.addCell(self.cell_list[self.size - 1].direction,map_cell_list)
            apple.change_location(map_cell_list)
            self.apple_eaten += 1

        #print("index of head: " + str(self.index[0]) + " " + str(self.index[1]))
        self.position = (self.index[0] * CELL_SIZE, self.index[1] * CELL_SIZE)

        self.cell_list[0].move(self.position,self.direction,self.index,map_cell_list)
        for i in range(1,self.size):
            #print("previous position" + str(self.cell_list[i - 1].position))
            self.cell_list[i].move(self.cell_list[i - 1].position,self.cell_list[i - 1].direction,self.cell_list[i - 1].index,map_cell_list)
        
        return True

    def displaySnake(self,surface):
        color_body = (0,0,255)
        color_head = (190,190,190)
        pg.draw.rect(surface,color_head,(self.position[0],self.position[1], CELL_SIZE,CELL_SIZE))
        for i in range(self.size):
            self.cell_list[i].displayCellSnake(surface,color_body)
        