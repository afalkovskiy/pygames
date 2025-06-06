import pygame

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Working With Shapes")

run = True
while run:

  screen.fill((255, 255, 255))

  pygame.draw.polygon(screen, (100, 100, 100), ((100, 200), (200, 300), (500, 100), (200, 250)))

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  pygame.display.flip()

pygame.quit()