# title_screen.py
import pygame
from constants import *

def show_title_screen(screen):
    """Display the title screen."""
    screen.fill(BLACK)
    font = pygame.font.Font(None, 80)
    title_surface = font.render("SNAKE GAME", True, GREEN)
    title_rect = title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    screen.blit(title_surface, title_rect)

    font = pygame.font.Font(None, 40)
    start_surface = font.render("Press any key to start", True, WHITE)
    start_rect = start_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    screen.blit(start_surface, start_rect)

    pygame.display.flip()

    # Wait for the player to press a key
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                waiting = False


def show_game_over_screen(screen):
    """Display the game over screen."""
    screen.fill(BLACK)
    font = pygame.font.Font(None, 80)
    game_over_surface = font.render("GAME OVER", True, RED)
    game_over_rect = game_over_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    screen.blit(game_over_surface, game_over_rect)

    font = pygame.font.Font(None, 40)
    restart_surface = font.render("Press R to Restart or Q to Quit", True, WHITE)
    restart_rect = restart_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    screen.blit(restart_surface, restart_rect)

    pygame.display.flip()

    # Wait for the player to choose
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return "RESTART"  # Restart the game
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()