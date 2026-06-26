import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen Settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Multiple Sprites Example")

# Load Background
background = pygame.image.load("background.png")
background = pygame.transform.scale(background, (800, 600))


# Sprite Class
class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image_file, x, y, width, height):
        super().__init__()

        self.image = pygame.image.load(image_file)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


# Create Sprites
player = GameSprite("player.png", 100, 420, 70, 70)
enemy = GameSprite("enemy.png", 620, 420, 70, 70)
coin = GameSprite("coin.png", 350, 250, 40, 40)
star = GameSprite("star.png", 500, 180, 40, 40)

# Create Sprite Group
all_sprites = pygame.sprite.Group()

# Add Sprites to Group
all_sprites.add(player)
all_sprites.add(enemy)
all_sprites.add(coin)
all_sprites.add(star)

# Font
font = pygame.font.SysFont("Arial", 35)

# Game Loop
running = True

while running:

    # Draw Background
    screen.blit(background, (0, 0))

    # Draw All Sprites
    all_sprites.draw(screen)

    # Display Title
    title = font.render("Adventure Game", True, (255, 255, 255))
    screen.blit(title, (250, 20))

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()
sys.exit()