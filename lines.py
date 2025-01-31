import pygame

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Working With Shapes")

run = True
while run:

  screen.fill((255, 255, 255))

  pos = pygame.mouse.get_pos()
  pygame.draw.line(screen, (255, 0, 255), (300, 200), pos)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  pygame.display.flip()

pygame.quit()