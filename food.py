# food.py
import random
from constants import WIDTH, HEIGHT, CELL_SIZE

class Food:
    def __init__(self):
        self.position = [random.randrange(1, (WIDTH // CELL_SIZE)) * CELL_SIZE, random.randrange(1, (HEIGHT // CELL_SIZE)) * CELL_SIZE]
        self.spawned = True

    def spawn_food(self):
        # Generate new food position.
        self.position = [random.randrange(1, (WIDTH // CELL_SIZE)) * CELL_SIZE, random.randrange(1, (HEIGHT // CELL_SIZE)) * CELL_SIZE]
        self.spawned = True