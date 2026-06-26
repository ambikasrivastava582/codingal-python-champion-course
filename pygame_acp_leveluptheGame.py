import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Level Up Game")

# Colors
WHITE = (255, 255, 255)
BLUE = (50, 100, 255)
GREEN = (0, 200, 0)
BLACK = (0, 0, 0)

# Font
font = pygame.font.SysFont("Arial", 35)

# Player
player_x = 100
player_y = 250
player_speed = 5

# Game Variables
score = 0
level = 1

clock = pygame.time.Clock()

running = True

while running:

    screen.fill(WHITE)

    # Draw Player
    pygame.draw.rect(screen, BLUE, (player_x, player_y, 60, 60))

    # Display Score
    score_text = font.render(f"Score : {score}", True, BLACK)
    screen.blit(score_text, (20, 20))

    # Display Level
    level_text = font.render(f"Level : {level}", True, GREEN)
    screen.blit(level_text, (20, 60))

    # Instructions
    instruction = font.render("Press SPACE to Earn 10 Points", True, BLACK)
    screen.blit(instruction, (180, 520))

    # Events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            # Increase score
            if event.key == pygame.K_SPACE:
                score += 10

                # Level Up
                if score % 50 == 0:
                    level += 1
                    player_speed += 2
                    print("Level Up!")

    # Move Player Automatically
    player_x += player_speed

    # Reset position when reaching the edge
    if player_x > WIDTH:
        player_x = -60

    pygame.display.update()

    # Increase game speed with each level
    clock.tick(30 + level * 5)

pygame.quit()
sys.exit()