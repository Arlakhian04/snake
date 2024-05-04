class Snake:
    def __init__(self,position,cell_list,direction,size):
        """Initializer for the snake

        Args:
            position (tuple): Contains both the position x and y of the head of the snake
            cell_list (numpy array): Contains all the cells after the head
            direction (tuple): Contains the direction of the head in the x and y axis
            size (int): The size of the snake including the head
        """
        self.position = position
        self.cell_list = cell_list
        self.direction = direction
        self.size = size