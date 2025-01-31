import pygame
import random

y = 0
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Trial')
running = 1
x = random.randint(100, 500)
y = random.randint(100, 500)
r = 10
while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = 0

    # pygame.draw.line(screen, (255, 255, 255), (x, y), (x, y + 10))
    pygame.draw.circle(screen, (120, 120, 150), (x, y), r, width=5)
    r += 2
    pygame.display.update()
    pygame.display.flip()
    pygame.time.wait(100)
    screen.fill(pygame.Color("black"))