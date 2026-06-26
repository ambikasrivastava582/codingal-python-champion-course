import pygame
import sys

# Initialize pygame
pygame.init()

# Screen size
WIDTH = 800
HEIGHT = 600

# Create game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My First Pygame")

# Colors
WHITE = (255, 255, 255)
BLUE = (30, 144, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

# Fonts
title_font = pygame.font.SysFont("Arial", 60)
text_font = pygame.font.SysFont("Arial", 30)

# Create text
title = title_font.render("Welcome to My Game!", True, YELLOW)
instruction = text_font.render("Press SPACE to Start", True, WHITE)

# Game loop
running = True

while running:

    # Background color
    screen.fill(BLUE)

    # Display title
    screen.blit(title, (120, 180))

    # Display instruction
    screen.blit(instruction, (240, 300))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Game Started!")

    # Update screen
    pygame.display.update()

# Quit pygame
pygame.quit()
sys.exit()