import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen Size
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Adventure Game")

# Colors
SKY_BLUE = (135, 206, 235)
GREEN = (34, 177, 76)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 215, 0)
BROWN = (139, 69, 19)
BLUE = (0, 0, 255)

# Fonts
title_font = pygame.font.SysFont("Arial", 60, True)
button_font = pygame.font.SysFont("Arial", 35)
small_font = pygame.font.SysFont("Arial", 25)

running = True

while running:

    # Background
    screen.fill(SKY_BLUE)

    # Ground
    pygame.draw.rect(screen, GREEN, (0, 500, 800, 100))

    # Sun
    pygame.draw.circle(screen, YELLOW, (700, 80), 40)

    # Clouds
    pygame.draw.circle(screen, WHITE, (120, 90), 30)
    pygame.draw.circle(screen, WHITE, (150, 70), 35)
    pygame.draw.circle(screen, WHITE, (180, 90), 30)

    # Title
    title = title_font.render("Adventure Game", True, BLACK)
    screen.blit(title, (180, 40))

    # Player
    pygame.draw.rect(screen, BLUE, (120, 430, 50, 70))
    player = small_font.render("Player", True, BLACK)
    screen.blit(player, (110, 510))

    # Enemy
    pygame.draw.rect(screen, RED, (600, 430, 50, 70))
    enemy = small_font.render("Enemy", True, BLACK)
    screen.blit(enemy, (595, 510))

    # Coin
    pygame.draw.circle(screen, YELLOW, (380, 430), 18)
    coin = small_font.render("Coin", True, BLACK)
    screen.blit(coin, (360, 455))

    # Score
    score = small_font.render("Score: 0", True, BLACK)
    screen.blit(score, (20, 20))

    # Start Button
    pygame.draw.rect(screen, BROWN, (300, 260, 200, 60), border_radius=10)
    start = button_font.render("START", True, WHITE)
    screen.blit(start, (355, 275))

    # Instructions
    instruction = small_font.render("Press SPACE to Start", True, BLACK)
    screen.blit(instruction, (290, 340))

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Game Started!")

    pygame.display.update()

pygame.quit()
sys.exit()