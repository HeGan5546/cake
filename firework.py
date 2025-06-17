import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fireworks")

#Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
COLORS = [(255, 255, 0), (255, 0, 255), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]


#Define Firework class
class Fireworks:
    def __init__(self, x, y):
        self.x =  x
        self.y = y
        self.color = random.choice(COLORS)
        self.exploded = False
        self.particles = []

    def explode(self):
        self.exploded = True
        for _ in range(100):
            speed = random.uniform(0.5, 3)
            angle = random.uniform(0, 2 * math.pi)
            dx = speed * math.cos(angle)
            dy = speed * math.sin(angle)
            particle = Particle(self.x, self.y, dx, dy, self.color)
            self.particles.append(particle)

    def update(self):
        if not self.exploded:
            self.y -= 3
            if self.y <= 0:
                self.explode()
        else:
            self.particles = [particle for particle in self.particles if particle.update()]


    def draw(self, screen):
        if not self.exploded:
            pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), 3)

        else:
            for particle in self.particles:
                particle.draw(screen)

#Define Particle class
class Particle:
    def __init__(self, x, y, dx, dy, color):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.color = color
        self.alpha = 255

    def update(self):
        self.x += self.dx
        self.alpha -= 3
        return self.alpha > 0

    def draw(self, screen):
        pygame.draw.circle(screen, (self.color[0], self.color[1], self.color[2], self.alpha), (int(self.x), int(self.y)), 2)

#Main loop
clock = pygame.time.Clock()
fireworks = []

running = True
while running:
    SCREEN.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if random.randint(1, 100) == 1:
        fireworks.append(Fireworks(random.randint(0, WIDTH), HEIGHT))

    for firework in fireworks:
        firework.update()
        firework.draw(SCREEN)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
        











            
