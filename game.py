# game.py
import pygame
from constants import BLACK, GREEN, RED, WHITE, CELL_SIZE, EAT_RANGE
from snake import Snake
from food import Food

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.snake = Snake()
        self.food = Food()
        self.score = 0

    def display_score(self):
        """Display the score on the screen."""
        font = pygame.font.Font(None, 35)
        score_surface = font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_surface, (400, 20))

    def check_collision(self):
        """Check for collisions with walls or itself."""
        # Wall collision
        if (self.snake.position[0] < 0 or self.snake.position[0] >= 800 or
            self.snake.position[1] < 0 or self.snake.position[1] >= 600):
            return True

        # Self collision
        for block in self.snake.body[1:]:
            if self.snake.position == block:
                return True
        return False

    def run(self):
        """Run the game loop."""
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.snake.change_direction('UP')
                    if event.key == pygame.K_DOWN:
                        self.snake.change_direction('DOWN')
                    if event.key == pygame.K_LEFT:
                        self.snake.change_direction('LEFT')
                    if event.key == pygame.K_RIGHT:
                        self.snake.change_direction('RIGHT')

            # Move the snake
            self.snake.move()

            # Debugging: Print snake and food positions
            print(f"Snake Position (Head): {self.snake.position}")
            print(f"Food Position: {self.food.position}")

            # Check if snake eats the food (using proximity range)
            if (abs(self.snake.position[0] - self.food.position[0]) <= EAT_RANGE and
                    abs(self.snake.position[1] - self.food.position[1]) <= EAT_RANGE):
                print("Food eaten!")  # Debug message
                self.score += 10
                self.food.spawn_food()  # Respawn the food
                self.snake.grow()       # Grow the snake

            # Check for wall or self-collision
            if self.check_collision():
                print("Collision detected!")  # Debug message
                running = False

            # Draw everything
            self.screen.fill(BLACK)
            for block in self.snake.body:
                pygame.draw.rect(self.screen, GREEN, pygame.Rect(block[0], block[1], CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(self.screen, RED, pygame.Rect(self.food.position[0], self.food.position[1], CELL_SIZE, CELL_SIZE))
            self.display_score()

            # Refresh the screen
            pygame.display.flip()

            # Control the game speed
            self.clock.tick(15)

        pygame.quit()