import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake Game")

# Define colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Define constants
CELL_SIZE = 20
SNAKE_SPEED = 10

# Define the Snake class
class Snake:
    def __init__(self):
        self.body = [(100, 100)]
        self.direction = 'RIGHT'

    def move(self):
        x, y = self.body[0]
        if self.direction == 'UP':
            y -= CELL_SIZE
        elif self.direction == 'DOWN':
            y += CELL_SIZE
        elif self.direction == 'LEFT':
            x -= CELL_SIZE
        elif self.direction == 'RIGHT':
            x += CELL_SIZE
        self.body.insert(0, (x, y))
        self.body.pop()

    def grow(self):
        x, y = self.body[0]
        if self.direction == 'UP':
            y -= CELL_SIZE
        elif self.direction == 'DOWN':
            y += CELL_SIZE
        elif self.direction == 'LEFT':
            x -= CELL_SIZE
        elif self.direction == 'RIGHT':
            x += CELL_SIZE
        self.body.insert(0, (x, y))

    def draw(self):
        for x, y in self.body:
            pygame.draw.rect(window, GREEN, (x, y, CELL_SIZE, CELL_SIZE))

    def check_collision(self):
        x, y = self.body[0]
        if x < 0 or x >= WINDOW_WIDTH or y < 0 or y >= WINDOW_HEIGHT:
            return True
        for i in range(1, len(self.body)):
            if self.body[i] == (x, y):
                return True
        return False

# Define the Food class
class Food:
    def __init__(self):
        self.position = (random.randint(0, (WINDOW_WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE,
                         random.randint(0, (WINDOW_HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE)

    def draw(self):
        pygame.draw.rect(window, RED, (self.position[0], self.position[1], CELL_SIZE, CELL_SIZE))

# Create the Snake and Food objects
snake = Snake()
food = Food()

# Main game loop
clock = pygame.time.Clock()
running = True
while running:
    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.direction != 'DOWN':
                snake.direction = 'UP'
            elif event.key == pygame.K_DOWN and snake.direction != 'UP':
                snake.direction = 'DOWN'
            elif event.key == pygame.K_LEFT and snake.direction != 'RIGHT':
                snake.direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and snake.direction != 'LEFT':
                snake.direction = 'RIGHT'

    # Move the snake
    snake.move()

    # Check for collisions with food
    if snake.body[0] == food.position:
        snake.grow()
        food = Food()

    # Check for collisions with walls or itself
    if snake.check_collision():
        running = False

    # Draw everything
    window.fill(WHITE)
    snake.draw()
    food.draw()
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(SNAKE_SPEED)

pygame.quit()
