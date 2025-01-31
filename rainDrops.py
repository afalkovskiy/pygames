import pygame
import random

y = 0
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Trial')
running = 1
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = 0
    x = random.randint(0, 600)
    pygame.draw.line(screen, (255, 255, 255), (x, y), (x, y + 10))
    y += 1
    pygame.display.update()
    pygame.display.flip()
    pygame.time.wait(1)
    screen.fill(pygame.Color("black"))