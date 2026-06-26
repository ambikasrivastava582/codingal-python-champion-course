import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen Size
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprite Example")

# Load Images
background = pygame.image.load("background.png")
player = pygame.image.load("player.png")
enemy = pygame.image.load("enemy.png")
coin = pygame.image.load("coin.png")

# Resize Images
background = pygame.transform.scale(background, (800, 600))
player = pygame.transform.scale(player, (80, 80))
enemy = pygame.transform.scale(enemy, (80, 80))
coin = pygame.transform.scale(coin, (40, 40))

# Font
font = pygame.font.SysFont("Arial", 35)

running = True

while running:

    # Display Background
    screen.blit(background, (0, 0))

    # Display Player
    screen.blit(player, (100, 420))

    # Display Enemy
    screen.blit(enemy, (600, 420))

    # Display Coin
    screen.blit(coin, (380, 350))

    # Display Text
    title = font.render("Adventure Game", True, (255, 255, 255))
    screen.blit(title, (260, 30))

    score = font.render("Score : 0", True, (255, 255, 0))
    screen.blit(score, (20, 20))

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()
sys.exit()