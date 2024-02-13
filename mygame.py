#Firstly we need to include the library so we can use the utility
#On windows, you can get this library easily using pip.
import pygame
import sys

#this init() is to initialize the program. The program is terminated by the quit() command
pygame.init()

#We need to create the screen on which our output will be displayed. This will consist of a gray background
#Our width and height are set here
width,height = 800,600
#Then the screen is created using pygame, and the specifics given of the variables width and height.
screen = pygame.display.set_mode((width,height))
#This is the text that will appear at the top of the graphics window. 
pygame.display.set_caption("One simple platormer game: Exploration Activity 1")


#this is just a little colour library I created so I don't have to always use the number representations
#There are other colours that can be used, these are just simple and common arbitrary choices.
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

#The player is the component of the platformer that the user will have the most control.
#This is initialized using the sprite module of the pygame library and values can be set as they are below. 
class Player(pygame.sprite.Sprite):
    #firstly the player needs to be initialized
    def __init__(self):
        #this is done as follows by using super() to consult the parent
        super().__init__()
        #The following are measured specifics of our player object. 
        self.image = pygame.Surface((50,50))
        self.image.fill((GREEN))
        self.rect = self.image.get_rect()
        self.rect.x=100
        self.rect.y=531
        self.vel_y=0
        
        #The results should be a small green filled squre that's 50X50 relative to the 600X800 screen.
        #Once this is initialized, there needs to be functions that dictate control and environmental info.
    def update(self):
        #The update function takes inputs that are predetermined by pygame to control our sprite. 
        #Firstly, our player sprite must be influenced by a downward force simulating gravity. 
        #This is a seperate function we design below. 
        self.gravity()
        #the keys variable is mapped to the pygame function for pressing keyboard keys as input. 
        keys = pygame.key.get_pressed()
        #The following if statements will 'rect' our 'self' or player in the direction shown based on 
        #The  mapped key. Each key on the keyboard can be mapped and return a response.
        #The following key presses will result in movement right, movement left or moving against gravity
        #by a set amount. This amount was picked at random but seemed reasonable at -23 (upward motion)
        if keys[pygame.K_LEFT]:
            self.rect.x -=5
        if keys[pygame.K_RIGHT]:
            self.rect.x+=5
        if keys[pygame.K_SPACE]:
            self.rect.y -=23
        #This is the gravity function. 
        #It was added to work against the jump action above based on the location of our sprite
        #This doesn't really work as intended but allows for a simple jump action. 
    def gravity(self):
    
        #self is the parameter given to gravity and if the player is above the floor-platform, they're designed
        #to move downward simulating gravity. 
        if self.rect.y < height - 50:
            self.vel_y += 1
        else:
        #This was added to give the appearance of collision, since when the player is on the floor, 
        #the sprite will not move upward or downward. This is reinforced by the -hits- statement implemented 
        #During the update loop for the platformer 
            self.vel_y = 0
            self.rect.y = height - 50
            
        self.rect.y += self.vel_y
        
#This will save the player variable as a Player object. Then add the player object to the group of sprites
#intended for the platformer.         
player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
#The following is a class for the platforms the player will be able to interact with on the screen. 
class Platform(pygame.sprite.Sprite):
    #Like the player object, they're initialized given the following parameters. 
    def __init__(self,x,y,width,height):
        #Also initialized using the parent object. 
        super().__init__()
        #These are the undetermined dimensions of the platforms. These are input as parameters
        #and are implemented by the initialization of the platform 
        self.image = pygame.Surface((width,height))
        #I chose blue cus why not. 
        self.image.fill((BLUE))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y 
#Unlike the player character, I don't create a character then add them to the sprite group
#I instead create a group called platforms, add a bunch of Platform() objects of different dimensions 
#And rect positions upon initialization and then add them to the all_sprites group as one big group.         
platforms = pygame.sprite.Group()
platforms.add(Platform(0,height - 20, width, 20))
platforms.add(Platform(100,400,200,20))
platforms.add(Platform(600,400,200,20))
platforms.add(Platform(300,300,200,20))
#Here is where I add the platforms created above to the sprite group. 
all_sprites.add(platforms)
    

running = True
while running:
    #This is a loop created to keep the game running. The game will continue to run until 
    #The exit button is interacted with. The result is closing the program. 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #all_sprites.update() forces the sprites grouped in all_sprites to the screen.        
    all_sprites.update()
    
    #hits is a variable chosen to provide the game with collision. The collision component
    #Didn't work as intended with just gravity() predetermining the -resting- state of our player object. 
    hits = pygame.sprite.spritecollide(player,platforms,False)
    
    #I later found out however that this also didn't work as inteded as it resulted in my ability to collide with 
    #The tops of platforms, callibrating the resting position, but the button of the platform results in the same
    #Re-positioning of the player to the top. If you jump through the bottom of a platform, it will launch you above 
    #The platform. 
    if hits:
        player.rect.y = hits[0].rect.y - 50
        player.vel_y = 0
        
    
    #I found all other colours were too vibrant and hard on the eyes so Gray worked best as a background colour. 
    screen.fill(GRAY)
    #The following addsd all the sprites to the screen
    all_sprites.draw(screen)
    
    pygame.display.flip()
    #This provides the game with a refresh-reate based time from Clock()
    #60 frames is just a good standard to aim for I imagine. 
    pygame.time.Clock().tick(60)
    #This next bit of code closes the pygame library and the system library. 
pygame.quit()
sys.exit()