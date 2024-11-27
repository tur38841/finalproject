import pygame
from pygame.locals import * 

pygame.init() #initialize pygame

screen_width = 800
screen_height= 800

#frames per second
fps = pygame.time.Clock()

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Stars Incoming!")



bg = pygame.image.load('img/hold.jpg') 
bg = pygame.transform.scale(bg, (screen_width, screen_height))  # Scale it to fit the screen size


#example
class ship(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load('img/ship.png') #this is the specific image
        self.image = pygame.transform.scale(self.image, (100,100))
        self.rect = self.image.get_rect()#this will create the boundaries of the image for youh
        self.rect.center = (x,y)

    def move(self):
        key_pressed = pygame.key.get_pressed()


        #this allows us to stay on the screen
        if key_pressed[K_UP] and self.rect.top>0:
            self.rect.move_ip(0, -10)

        if key_pressed[K_DOWN] and self.rect.bottom < screen_height:
            self.rect.move_ip(0,10)

        #7 is the speed


        

ship = ship(screen_width // 4, screen_height // 2)

all_sprites = pygame.sprite.Group()
all_sprites.add(ship)


run = True
while run: 
    
    screen.blit(bg, (0,0))
    ship.move()
    all_sprites.draw(screen)
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            run = False
            
    pygame.display.update()
    fps.tick(60)




pygame.quit()

