import pygame
import random

y = 0
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Rain circles 3')
running = 1
x1 = random.randint(100, 500)
y1 = random.randint(100, 500)
x2 = random.randint(100, 500)
y2 = random.randint(100, 500)
r1 = 10
r2 = 10
frameNumber = 0
while running:
    frameNumber = frameNumber + 1

    if frameNumber==20:
        x1 = random.randint(100, 500)
        y1 = random.randint(100, 500)
        r1 = 10

    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = 0

    # pygame.draw.line(screen, (255, 255, 255), (x, y), (x, y + 10))
    pygame.draw.circle(screen, (120, 120, 150), (x1, y1), r1, width=5)
    pygame.draw.circle(screen, (120, 120, 150), (x2, y2), r2, width=5)
    r1 += 2
    r2 += 2
    # pygame.display.update()
    pygame.display.flip()
    pygame.time.wait(100)
    screen.fill(pygame.Color("black"))