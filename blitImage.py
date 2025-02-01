import pygame
from pygame.locals import*
img = pygame.image.load('minyon.bmp')

white = (255, 255, 255)
w = 640
h = 480
screen = pygame.display.set_mode((w, h))
screen.fill((white))
running = 1

while running:
    screen.fill((white))
    screen.blit(img,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = 0

    pygame.display.flip()