# snake.py

class Snake:
    def __init__(self):
        self.position = [100, 50] # Starting Position
        self.body = [[100, 50], [90, 50,], [80, 50]] # Initial Body Segments
        self.direction  = 'RIGHT' # Initial Diretion
        self.change_to = self.direction

    def change_direction(self, direction):
        # Change direction of the snake if not in the opposite direction.
        if direction == 'UP' and self.direction != 'DOWN':
            self.change_to = 'UP'
        if direction == 'DOWN' and self.direction != 'UP':
            self.change_to = 'DOWN'
        if direction == 'LEFT' and self.direction != 'RIGHT':
            self.change_to = 'LEFT'
        if direction == 'RIGHT' and self.direction != 'LEFT':
            self.change_to = 'RIGHT'

    def move(self):
        # Move the snake in the current direction
        if self.direction == 'UP':
            self.position[1] -= 20
        if self.direction == 'DOWN':
            self.position[1] += 20
        if self.direction == 'LEFT':
            self.position[0] -= 20
        if self.direction == 'RIGHT':
            self.position[0] += 20

        # Insert the new head posiitona nd remove the tail
        self.body.insert(0, list(self.position))
        self.body.pop()

    def grow(self):
        # Grow the sanke (do not remove the tail)
        self.body.insert(0, list(self.position))
    