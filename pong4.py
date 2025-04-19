import pygame
pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong V.4")

run = True
x1=50
y1=100
dx=5
dy=5

while run:

  screen.fill((255, 255, 255))

  if x1>SCREEN_WIDTH:
    dx = -5
  if x1<0:
    dx = 5    

  if y1>SCREEN_HEIGHT or y1<0:
     dy = -dy
      


  x1=x1+dx
  y1=y1+dy


  # pygame.draw.circle(screen, (0, 0, 0), (300, 200), 75)
  pygame.draw.circle(screen, (200,0,200), (x1, y1), 25, width=4)

  # pygame.draw.circle(screen, (255, 255, 0), (300, 200), 75, draw_top_right = True, draw_bottom_left = True)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  pygame.display.flip()
  pygame.time.wait(10)

pygame.quit()