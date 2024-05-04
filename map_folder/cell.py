import pygame as pg
class Cell:
    def __init__(self,position,width,isCellSnake,color,index):
        """Initializer for Cell

        Args:
            position (tuple): position of the top-left corner of the cell inside the map | X x Y
            width (int): width of the cell
            isCellSnake (bool): True if there is a snakeCell on it
            color (tuple): _color of the cell
            index (tuple): index in the cell_list of map
        """
        self.position = position
        self.width = width
        self.isCellSnake = isCellSnake
        self.color = color
        self.index = index

    def displayCell(self,surface):
        pg.draw.rect(surface,self.color,(self.position[0],self.position[1], self.width, self.width))
        