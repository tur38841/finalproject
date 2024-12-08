import pygame
from pygame.locals import *
import random
pygame.init() #initialize pygame

#this was later used to regulate the speed of my game
fps = pygame.time.Clock()

#screen
screen_width = 800
screen_height= 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Stars Incoming!")

#the galaxy background
bg = pygame.image.load('img/galaxy.jpg')
#how I was able to fit the background to my screen size
bg = pygame.transform.scale(bg, (screen_width, screen_height))  # Scale it to fit the screen size

#this was later used to show how often the stars are to appear
star_frequency = 1500 # 1.5 seconds

#we need this variable to properly time the gaps
last_star = pygame.time.get_ticks()
flying = False
game_over = False


class ship(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load('img/ship.png') #this is the specific image
        self.image = pygame.transform.scale(self.image, (100,100)) #size of the image 
        self.rect = self.image.get_rect()#this will create the boundaries of the image 
        self.rect.center = (x,y)
        self.hitbox =pygame.Rect(self.rect.x + 10, self.rect.y + 10, 80, 80)
    def move(self):
        key_pressed = pygame.key.get_pressed()

        #checks if the up arrow is presserd and the ship is not falling of the screen 
        if key_pressed[K_UP] and self.rect.top>0:
            self.rect.move_ip(0, -10)
        #same idea, but checks that it is not falling off the screen at the bottom
        if key_pressed[K_DOWN] and self.rect.bottom < screen_height:
            self.rect.move_ip(0,10) #10 is the speed

        self.hitbox.topleft = self.rect.topleft
    
            

class Star(pygame.sprite.Sprite):
    def __init__(self,x,y, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/star.png')
        
        # position 1 is from the top, -1 is from the bottom
        if position == 1:
            #slightly angles the star 
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect = self.image.get_rect()
            self.rect.topleft = (x,y)
        if position == -1:
            self.rect = self.image.get_rect()
            self.rect.topleft = (x,y)
        self.image = pygame.transform.scale(self.image, (200,200))
        self.rect.inflate_ip(-200,-200)

        #the hitbox is shifed  a little to the right and down
        #this allows for there to be a more specific hit on the hitbox
        self.hitbox = pygame.Rect(self.rect.x + 10, self.rect.y + 10, 80, 80)
        
    def update(self):
        self.rect.x -= 4
        self.hitbox.topleft = self.rect.topleft
        if self.rect.right < 0:
            self.kill()

#this shows where I placed my ship 
ship = ship(screen_width // 4, screen_height // 2)


all_star = pygame.sprite.Group() # I add the specific stars later in the code
all_ship = pygame.sprite.Group()
all_ship.add(ship)                

#while the game is running
run = True
while run:
    
    #centers the background
    screen.blit(bg, (0,0))
    #calls the move function from the ship class
    ship.move() 
    #brings the ship to the screen
    all_ship.draw(screen)
    #constantly updates the ship
    all_ship.update()

    
    all_star.draw(screen)
    all_star.update()
    
    if game_over == False:
        
        #generate new stars
        time_now = pygame.time.get_ticks()
        if time_now - last_star > star_frequency:
            star1 = Star(screen_width, random.randint(0,800), -1) 
            star2 = Star(screen_width, random.randint(0,800), -1)
            star3 = Star(screen_width, random.randint(0,800), 1)
            star4 = Star(screen_width, random.randint(0,800), 1)

            all_star.add(star1, star2, star3, star4)
            last_star = time_now
                
        all_star.update()


    #this constantly checks for the hit
    for star in all_star:
        if ship.hitbox.colliderect(star.hitbox):  # Check if the ship's hitbox intersects the star's hitbox
            game_over = True
    
    if game_over:
        font = pygame.font.Font(None, 74)
        #font.render(text, anti_aliasing, color)
        text = font.render("Game Over!", True, (255, 0, 0))
        screen.blit(text, (screen_width//2 - text.get_width()//2, screen_height//2))
        
    for event in pygame.event.get():
        #allows you to exit out of the code
        if event.type == pygame.QUIT: 
            run = False
            
    pygame.display.update()
    fps.tick(60)




pygame.quit()
