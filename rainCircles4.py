import pygame
import random

y = 0
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Rain circles 3')
running = 1
x1 = random.randint(100, 500)
y1 = random.randint(100, 500)
x2 = random.randint(100, 500)
y2 = random.randint(100, 500)
r1 = 10
r2 = 10
frameNumber = 0

nCircles = 20
circleArr = []

class rainCircle:
    def __init__(self, x, y, r, t):
        self.x = x
        self.y = y
        self.r = r
        self.t = t

c3 = rainCircle(random.randint(100, 500), random.randint(100, 500), 10, random.randint(10, 50) )
print(c3.x, c3.y, c3.r, c3.t)

for i in range(nCircles):
    ci = rainCircle(random.randint(100, 500), random.randint(100, 500), random.randint(5,20), random.randint(2, 100))
    circleArr.append(ci)

for ci in circleArr:
    print(ci.x, ci.y, ci.r, ci.t)


while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = 0

    frameNumber = frameNumber + 1

    if frameNumber>200:
        frameNumber=200

    # if frameNumber==20:
    #     x1 = random.randint(100, 500)
    #     y1 = random.randint(100, 500)
    #     r1 = 10

    # pygame.draw.circle(screen, (120, 120, 150), (x1, y1), r1, width=5)
    # r1 += 2

    for ci in circleArr:
        xi = ci.x
        yi = ci.y
        ri = ci.r
        ri +=2
        ci.r += 2
        ti = ci.t
        ci.t +=1

        if frameNumber > ti:
            pygame.draw.circle(screen, (120, 120, 150), (xi, yi), ri, width=5)

        if ri>100:
            ci.x = random.randint(100, 500)
            ci.y = random.randint(100, 500)
            ci.r = 10
            ci.t = random.randint(2, 100)


    pygame.display.flip()
    pygame.time.wait(100)
