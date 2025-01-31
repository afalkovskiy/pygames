
import pygame
pygame.init()
screen = pygame.display.set_mode([800,600])
run = True
GREEN = (0,255,0) # RGB
radius = 50
while run:
    screen.fill((255,255,255))
    for event in pygame.event.get():        
        if event.type == pygame.QUIT:
            run = False
            # if event.key == pygame.K_LEFT:              
            #     keep_going = False        
    pygame.draw.circle(screen, GREEN, (100,100), radius)
    pygame.draw.circle(screen, GREEN, (150,100), radius)
    pygame.display.update()
pygame.quit()