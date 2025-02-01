import pygame
import random
from pygame.locals import*
# img = pygame.image.load('minyon.bmp')
img = pygame.image.load('clouds2.bmp')
img.set_alpha(128)
# img=pygame.transform.rotate(img, -45)
# img=pygame.transform.rotozoom(img, -45, 1.5)

white = (255, 255, 255)
w = 640
h = 480
screen = pygame.display.set_mode((w, h))
screen.fill((white))
running = 1
x = random.randint(-100, 0)
y = random.randint(100, 200)

while running:
    screen.fill((white))
    
    screen.blit(img,(x,y))
    screen.blit(img,(x*2,y+100))
    x = x + 2

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = 0

    if x>600:
        x = random.randint(100, 500)
        y = random.randint(-100, 0)

    pygame.display.flip()
    pygame.time.wait(100)