# game.py
import pygame
from constants import *
from snake import Snake
from food import Food
from screens import show_title_screen, show_game_over_screen
from version import __version__

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption(f"Snake Game (Version: {__version__})")
        self.clock = pygame.time.Clock()
        self.snake = Snake()
        self.food = Food()
        self.score = 0

    def display_score(self):
        """Display the score on the screen."""
        font = pygame.font.Font(None, 35)
        score_surface = font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_surface, (400, 20))

    def reset_game(self):
        """Reset the game state."""
        self.snake = Snake()
        self.food = Food()
        self.score = 0

    # game.py
    def check_collision(self):
        """Check for wall or self-collision."""
        # Wall collision
        if (self.snake.position[0] < 0 or self.snake.position[0] >= WIDTH or
            self.snake.position[1] < 0 or self.snake.position[1] >= HEIGHT):
            print("Wall collision detected!")  # Debug message
            return True

        # Self-collision
        for block in self.snake.body[1:]:
            if self.snake.position == block:
                print(f"Self-collision detected! Head: {self.snake.position}, Body: {self.snake.body}")  # Debug message
                return True

        return False

    def run(self):
        """Run the game loop."""
        show_title_screen(self.screen)
        self.reset_game()

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
                action = show_game_over_screen(self.screen)
                if action == 'RESTART':
                    self.reset_game()
                else:
                    running = False

            # Draw everything
            self.screen.fill(BLACK)
            for block in self.snake.body:
                pygame.draw.rect(self.screen, GREEN, pygame.Rect(block[0], block[1], CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(self.screen, RED, pygame.Rect(self.food.position[0], self.food.position[1], CELL_SIZE, CELL_SIZE))
            self.display_score()
            self.display_debug_info()

            # Refresh the screen
            pygame.display.flip()

            # Control the game speed
            self.clock.tick(15)

        pygame.quit()


    def display_debug_info(self):
        """Display debug information on the screen."""
        font = pygame.font.Font(None, 20)
        debug_lines = [
            f"FPS: {int(self.clock.get_fps())}",  # Frames Per Second
            f"Score: {self.score}",  # Current score
            f"Snake Length: {len(self.snake.body)}",  # Snake body length
            f"Food Position: {self.food.position}",  # Food position on the grid
            f"Snake Head: {self.snake.position}",  # Snake head position
            f"Version: {__version__}"
        ]
        
        # Render each debug line
        y_offset = 40  # Starting vertical position
        for line in debug_lines:
            debug_surface = font.render(line, True, (255, 255, 255))
            self.screen.blit(debug_surface, (10, y_offset))
            y_offset += 20