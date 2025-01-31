import pygame

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
x = 0

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Working With Shapes")

run = True
while run:

  screen.fill((255, 255, 255))

  if pygame.mouse.get_pressed()[0] == True:
    x += 0.001
  elif pygame.mouse.get_pressed()[2] == True:
    x -= 0.001

  pygame.draw.arc(screen, (0, 255, 255), (200, 100, 150, 150), 0, x, width = 5)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  pygame.display.flip()

pygame.quit()