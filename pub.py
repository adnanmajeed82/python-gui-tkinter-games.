import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Zombie Game")

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Load game assets
player_img = pygame.image.load('player.png')
zombie_img = pygame.image.load('zombie.png')

# Define Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.centerx = WINDOW_WIDTH // 2
        self.rect.bottom = WINDOW_HEIGHT - 20

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5

        # Keep the player inside the window
        self.rect.x = max(0, min(self.rect.x, WINDOW_WIDTH - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, WINDOW_HEIGHT - self.rect.height))

# Define Zombie class
class Zombie(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = zombie_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WINDOW_WIDTH - self.rect.width)
        self.rect.y = random.randint(0, WINDOW_HEIGHT - self.rect.height)
        self.speed = random.randint(1, 3)

    def update(self, player):
        if self.rect.x < player.rect.x:
            self.rect.x += self.speed
        elif self.rect.x > player.rect.x:
            self.rect.x -= self.speed
        if self.rect.y < player.rect.y:
            self.rect.y += self.speed
        elif self.rect.y > player.rect.y:
            self.rect.y -= self.speed

# Create sprite groups
all_sprites = pygame.sprite.Group()
zombies = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Main game loop
running = True
clock = pygame.time.Clock()
while running:
    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get player input
    keys = pygame.key.get_pressed()

    # Update player and zombies
    player.update(keys)
    for zombie in zombies:
        zombie.update(player)

    # Spawn zombies
    if len(zombies) < 10:
        zombie = Zombie()
        zombies.add(zombie)
        all_sprites.add(zombie)

    # Check for collisions
    hits = pygame.sprite.spritecollide(player, zombies, False)
    if hits:
        running = False

    # Draw
    window.fill(WHITE)
    all_sprites.draw(window)
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()
