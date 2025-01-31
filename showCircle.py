import pygame
pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Working With Shapes")

run = True
while run:

  screen.fill((255, 255, 255))

  # pygame.draw.rect(screen, (255, 0, 0), (200, 100, 150, 150), width = 5)
  # pygame.draw.circle(screen, (0, 90, 0), (300, 200), 75, width = 5)

  pygame.draw.circle(screen, (0, 0, 0), (300, 200), 75)
  pygame.draw.circle(screen, (255, 255, 0), (300, 200), 75, draw_top_right = True, draw_bottom_left = True)

  # pygame.draw.ellipse(screen, (0, 0, 255), (200, 150, 150, 75))

  pygame.draw.arc(screen, (0, 255, 255), (200, 100, 150, 250), 0, 3.14, width = 5)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  pygame.display.flip()

pygame.quit()