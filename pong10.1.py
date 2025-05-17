import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700
PAD_HEIGHT = 10
PAD_WIDTH = 140

BRICK_WIDTH = 80
BRICK_HEIGHT = 40
BRICK_COLOR = (255, 255, 255)

# create a list of brick objects
bricks = []
for i in range(5):
  for j in range(9):
    brick_x = j * (BRICK_WIDTH + 10)
    brick_y = i * (BRICK_HEIGHT + 10)
    bricks.append(pygame.Rect(brick_x, brick_y, BRICK_WIDTH, BRICK_HEIGHT))

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong V.10.1")

run = True
x1=random.randint(100, 500)
y1=250
dx=random.randint(1,10)
dy=random.randint(1,10)

xPad = int(SCREEN_WIDTH/2)
yPad = SCREEN_HEIGHT - 10
dxPad = 0

startflag=True

while run:

  screen.fill((0, 0, 0))

  for brick in bricks:
    pygame.draw.rect(screen, BRICK_COLOR, brick, 4)

  for brick in bricks: 
    if brick.collidepoint(x1, y1):
      bricks.remove(brick)
      dy = -dy
      break


  if x1>SCREEN_WIDTH:
    dx = -5
  if x1<0:
    dx = 5    

  if y1<0:
    dy = -dy

  if y1>SCREEN_HEIGHT and x1 >= xPad - 25 and x1 <= xPad + PAD_WIDTH:
    dy = -dy 
  else: 
   if y1>SCREEN_HEIGHT: 
    # x1=random.randint(100, 500)
    # y1=10
    # dx=random.randint(5)
    # dy=random.randint(1,10)
    x1=250
    y1=250
    dx=5
    dy=5
    x1=xPad+PAD_WIDTH/2
    y1=yPad-15
    startflag=True
    

#    xPad = int(SCREEN_WIDTH/2)
#    yPad = SCREEN_HEIGHT - 10   


  x1=x1+dx
  y1=y1+dy
  if startflag==True:
    x1=xPad+PAD_WIDTH/2
    y1=yPad-15
   


  # pygame.draw.circle(screen, (0, 0, 0), (300, 200), 75)
  pygame.draw.circle(screen, (255,255,255), (x1, y1), 15,)
  pygame.draw.rect(screen, (255,255,255), (xPad, yPad, PAD_WIDTH, PAD_HEIGHT), 4,2,2,2)

  # pygame.draw.circle(screen, (255, 255, 0), (300, 200), 75, draw_top_right = True, draw_bottom_left = True)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
          dxPad = - 6
 
        if event.key == pygame.K_RIGHT:
          dxPad = 6 

        if event.key == pygame.K_UP and startflag==True: 
          dy=-5
          startflag=False

    elif event.type == pygame.KEYUP:
      dxPad = 0 

  xPad = xPad + dxPad 
  if xPad + PAD_WIDTH > SCREEN_WIDTH:
    dxPad = 0
  if xPad < 0:
    dxPad = 0      

  pygame.display.flip()
  pygame.time.wait(10)

pygame.quit()