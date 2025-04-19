import pygame
pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong V.1")

run = True
while run:

  screen.fill((255, 255, 255))

  # pygame.draw.circle(screen, (0, 0, 0), (300, 200), 75)
  pygame.draw.circle(screen, (200,0,200), (200, 200), 25, width=4)

  # pygame.draw.circle(screen, (255, 255, 0), (300, 200), 75, draw_top_right = True, draw_bottom_left = True)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  pygame.display.flip()

pygame.quit()