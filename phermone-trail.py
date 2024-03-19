# A simple simulation of ants leving phermone trails on grid.



# random ants leaving pheromones on a grid

import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 512, 512
GRID_SIZE = 2
NUM_ANTS = 200
PHEROMONE_EVAPORATION = 0.98
PHEROMONE_DEPOSIT = 0.1
ITERATIONS = 1000

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ant System Simulation")
clock = pygame.time.Clock()


class Ant:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = random.random() * 2 * math.pi

    def move(self):
        # Move the ant in a random direction
        self.direction += random.uniform(-math.pi / 4, math.pi / 4)
        self.x = (self.x + math.cos(self.direction)) % WIDTH
        self.y = (self.y + math.sin(self.direction)) % HEIGHT


class Grid:
    def __init__(self):
        self.grid = [[0] * (WIDTH // GRID_SIZE) for _ in range(HEIGHT // GRID_SIZE)]

    def update(self, ants):
        # Evaporate pheromone
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                self.grid[i][j] *= PHEROMONE_EVAPORATION

        # Deposit pheromone
        for ant in ants:
            grid_x = int(ant.x // GRID_SIZE)
            grid_y = int(ant.y // GRID_SIZE)
            self.grid[grid_y][grid_x] += PHEROMONE_DEPOSIT

    def draw(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                intensity = min(int(self.grid[i][j] * 255), 255)
                color = (0, intensity, 0)
                pygame.draw.rect(screen, color, (j * GRID_SIZE, i * GRID_SIZE, GRID_SIZE, GRID_SIZE))


# Create ants
ants = [Ant(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(NUM_ANTS)]

# Create grid
grid = Grid()

# Main loop
running = True
for _ in range(ITERATIONS):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move ants
    for ant in ants:
        ant.move()

    # Update grid
    grid.update(ants)

    # Clear screen
    screen.fill(BLACK)

    # Draw grid
    grid.draw()

    # Draw ants
    for ant in ants:
        pygame.draw.circle(screen, RED, (int(ant.x), int(ant.y)), 2)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
