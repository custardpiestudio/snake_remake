# snake.py
from constants import CELL_SIZE

class Snake:
    def __init__(self):
        self.position = [100, 50]  # Starting position
        self.body = [[100, 50], [90, 50], [80, 50]]  # Initial body segments
        self.direction = 'RIGHT'  # Initial direction
        self.change_to = self.direction

    def change_direction(self, direction):
        """Change the direction of the snake if not in the opposite direction."""
        if direction == 'UP' and self.direction != 'DOWN':
            self.change_to = 'UP'
        if direction == 'DOWN' and self.direction != 'UP':
            self.change_to = 'DOWN'
        if direction == 'LEFT' and self.direction != 'RIGHT':
            self.change_to = 'LEFT'
        if direction == 'RIGHT' and self.direction != 'LEFT':
            self.change_to = 'RIGHT'

    def move(self):
        """Move the snake in the current direction."""
        self.direction = self.change_to
        if self.direction == 'UP':
            self.position[1] -= CELL_SIZE
        if self.direction == 'DOWN':
            self.position[1] += CELL_SIZE
        if self.direction == 'LEFT':
            self.position[0] -= CELL_SIZE
        if self.direction == 'RIGHT':
            self.position[0] += CELL_SIZE

        # Debugging: Ensure the position is grid-aligned
        print(f"New Snake Head Position: {self.position}")

        # Insert new head position and remove the tail
        self.body.insert(0, list(self.position))
        self.body.pop()

    def grow(self):
        """Grow the snake (do not remove the tail)."""
        self.body.insert(0, list(self.position))
    