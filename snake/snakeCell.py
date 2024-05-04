class SnakeCell:
    def __init__(self,position,previous_position,direction,previous_direction,isLast):
        """Initializer for each cell of the snake

        Args:
            position (tuple): position of the cell
            previous_position (tuple): position of the previous cell
            direction (tuple): direction of the cell
            previous_direction (tuple): direction of the previous cell
            isLast (bool): bool to know if it is the last cell in the list
        """
        self.position = position
        self.previous_position = previous_position
        self.direction = direction
        self.previous_direction = previous_direction
        self.isLast = isLast