# food.py
import random
from constants import WIDTH, HEIGHT, CELL_SIZE

class Food:
    def __init__(self):
        self.position = self.generate_food_position()

    def generate_food_position(self):
        """Generate a new grid-aligned position for the food."""
        x = random.randrange(0, WIDTH // CELL_SIZE) * CELL_SIZE
        y = random.randrange(0, HEIGHT // CELL_SIZE) * CELL_SIZE
        print(f"Food spawned at: ({x}, {y})")  # Debugging
        return [x, y]

    def spawn_food(self):
        """Respawn food in a new grid-aligned position."""
        self.position = self.generate_food_position()