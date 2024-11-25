import pygame
from pygame.locals import * 

pygame.init()

screen_width = 864
screen_height= 936

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Meteors Incoming!")



bg = pygame.image.load('img/hold.jpg') 
bg = pygame.transform.scale(bg, (screen_width, screen_height))  # Scale it to fit the screen size


run = True
while run: 
    
    screen.blit(bg, (0,0))
    
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            run = False
            
    pygame.display.update()
    



pygame.quit()

