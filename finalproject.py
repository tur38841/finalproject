import pygame
from pygame.locals import * 

pygame.init() #initialize pygame
screen_width = 800
screen_height= 800
fps = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Stars Incoming!")


bg = pygame.image.load('img/hold.jpg') 
bg = pygame.transform.scale(bg, (screen_width, screen_height))  # Scale it to fit the screen size

star_frequency = 1500 # 1.5 seconds
last_star = pygame.time.get_ticks()
flying = False
game_over = False

class ship(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load('img/ship.png') #this is the specific image
        self.image = pygame.transform.scale(self.image, (100,100))
        self.rect = self.image.get_rect()#this will create the boundaries of the image for youh
        self.rect.center = (x,y)

    def move(self):
        key_pressed = pygame.key.get_pressed()

        self.clicked = False
        
        #this allows us to stay on the screen
        if key_pressed[K_UP] and self.rect.top>0:
            self.rect.move_ip(0, -10)

        if key_pressed[K_DOWN] and self.rect.bottom < screen_height:
            self.rect.move_ip(0,10)

        #7 is the speed
    
            



class star(pygame.sprite.Sprite):
    def __init__(self,x,y, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/star.png')
        
        # position 1 is from the top, -1 is from the bottom
        if position == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect = self.image.get_rect()
            self.rect.topleft = (x,y)
        if position == -1:
            self.rect = self.image.get_rect()
            self.rect.topleft = (x,y)
        self.image = pygame.transform.scale(self.image, (200,200))
       
    def update(self):
        self.rect.x -= 4



ship = ship(screen_width // 4, screen_height // 2)

all_star = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(ship)

                 

run = True
while run: 
    
    screen.blit(bg, (0,0))
    ship.move()
    all_sprites.draw(screen)
    all_sprites.update()
    all_star.draw(screen)
    all_star.update()
    
    if game_over == False:
        #generate new stars
        time_now = pygame.time.get_ticks()
        if time_now - last_star > star_frequency:
            top_star  = star(screen_width, int(screen_height / 4), -1) #screen_width starts from beg
            btm_star = star(screen_width, int(screen_height / 2), 1)
            all_star.add(top_star, btm_star)
            last_pipe = time_now
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and flying == False:
            flying = True
    pygame.display.update()
    fps.tick(60)




pygame.quit()


#goals for next edit
# figure out why it is repeating so frequently - chatgpt
# figure out randomization - youtube

