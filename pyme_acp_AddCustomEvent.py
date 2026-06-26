import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Custom Event Example")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

player_color = BLUE

# Font
font = pygame.font.SysFont("Arial", 30)

# Create a Custom Event
CHANGE_COLOR = pygame.USEREVENT + 1

# Trigger the event every 3000 milliseconds (3 seconds)
pygame.time.set_timer(CHANGE_COLOR, 3000)

running = True

while running:
    screen.fill(WHITE)

    # Draw Player
    pygame.draw.rect(screen, player_color, (250, 150, 100, 100))

    # Display Text
    text = font.render("Color changes every 3 seconds", True, (0, 0, 0))
    screen.blit(text, (80, 40))

    # Event Handling
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # Handle Custom Event
        elif event.type == CHANGE_COLOR:
            player_color = (
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255)
            )
            print("Custom Event Triggered!")

    pygame.display.update()

pygame.quit()
sys.exit()