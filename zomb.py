import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Traffic vs. Zombie")

# Define colors
WHITE = (255, 255, 255)

# Define Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = WINDOW_WIDTH // 2
        self.rect.bottom = WINDOW_HEIGHT - 20

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5

# Define Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WINDOW_WIDTH - self.rect.width)
        self.rect.y = random.randint(-100, -40)
        self.speedy = random.randint(1, 5)

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > WINDOW_HEIGHT + 10:
            self.rect.x = random.randint(0, WINDOW_WIDTH - self.rect.width)
            self.rect.y = random.randint(-100, -40)
            self.speedy = random.randint(1, 5)

# Create sprite groups
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
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

    # Update
    all_sprites.update()

    # Spawn enemies
    if len(enemies) < 10:
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)

    # Collision detection
    hits = pygame.sprite.spritecollide(player, enemies, False)
    if hits:
        running = False

    # Draw
    window.fill((0, 0, 0))
    all_sprites.draw(window)
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()
