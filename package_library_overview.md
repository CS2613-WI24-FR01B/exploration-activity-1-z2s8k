# Package/Library Overview

## Which Package/Library did you select?
The package/library that I chose is collection of modules called Pygame and is a part of the SDL library.

## What Pygame?
Pygame is a set of modules in Python programming language that add functionality to the media components of the SDL library.

### What purpose does Pygame serve?

Pygame modules are used for the purpose of designing video games. These modules are built to complement the 
SDL Library and provide users with a paradigm from which they can build fully functional games and multimedia program [REF](https://www.pygame.org/wiki/about).

### How do you use Pygame?

#### How do you install Pygame?

Pygame can be installed to almost any device/operating system that has Python and pip already installed. After installing
python and pip, the Pygame modules can be installed using the following line in the command prompt:

```
	py -m pip install -U pygame
```	

#### How do you design using Pygame?

once Pygame is installed, you must import the modules at the beginning of your program.

```
	import pygame
```	

In order to return an output
when executing a pygame file, you must intialize the program and remember to quit the program once your window-loop is terminated. The following two lines of code should encompass your pygame program [REF](https://pygame.readthedocs.io/en/latest/1_intro/intro.html#import-the-module).   

```
	pygame.init()

    #Insert the body of your program here. 

    pygame.quit()
```	
The detail of customization using Pygame requires an understanding of object oriented programming. The sprites and relationships between each sprite implemented in a Pygame video game can be defined and customized using a variety of different function calls. Pygame is called specifically as a prefice followed by a command and parameters as input. 

Each sprite object that's built in Pygame must contain its own internal initialization. An example of a sprite class titled **entity** using several different design components can be seen below [REF](https://pygame.readthedocs.io/en/latest/10_games/games.html). 

```
class entity(pygame.sprite.Sprite):
     def __init__(self):
     super().__init__()

```
This will create an **entity** object that can be used as a sprite in a Pygame video game. We use *self* as our parameter variable and can influence this entity using a series of dimensional instructions on the *self* parameter. funcitons can also be defined in our classes are they are what can be used to allow for our entity to interact with other components of the program. 

Alternatively, you can define these measurements outside of a entity class and use the following import after importing pygame as follows [REF](https://pygame.readthedocs.io/en/latest/1_intro/intro.html). The below statement imports 280 constants for use in game design.  

```
import pygame
from pygame.locals import *
```
This alternative allows access to pygame built in sprites where you can input parameters into pre-built objects given by the pygame library. 

An example of objects in Pygame that are prebuilt are called *rect* objects, and the nature of their interactions can be dictated by the functions of that object. As an example, when you're providing instructions for the dimensions of the entity class object, you would provide the self parameter with *rect* instructions [REF](https://pygame.readthedocs.io/en/latest/1_intro/intro.html#explore-a-simple-ball-game). 

```
#This tells the class our self parameter is to be 25X25 pixels (Very small)
self.image = pygame.Surface((25,25))

#This determines the colour of our object, in this case, it will be Gray
self.image.fill((127, 127, 127))

#This defines the self parameter as a rect object and retrieves it for use in Pygame. This allows for functions for this object to be #utilized.

self.rect = self.image.get_rect()
```
It's important to note that details of an object either imported or called from Pygame don't necessarily need to be  included in their own class. This was just done above to show how to create an independant class object, define class specific functions for the objects interactions and initialize that entity based on the intended use. This level of customization is an impressive utility of Pygame which allows users to create more simple sprites without rigorous design, as well as advanced customization option.

After creating your entity objects in the form of sprites, they need to be added to what is called an "Event loop". This event loop is used to generate a constantly updating interaction between the display for your Pygame video game and the GUI that's used to display the interactions between sprite objects. An example of implementing a simple Event loop is as follows [REF](https://pygame.readthedocs.io/en/latest/1_intro/intro.html#show-the-event-loop): 

```
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
```

This can be placed below the class and function definitons and the sprite update and implementation would go after the for loop. That for loop is designed to ensure that the game quits properly when terminated. All other events can occur subsequently and these events can be defined by the functions given to your sprite objects or can be determined within the loop itself as it will continue to update as long as the program hasn't been terminated or given the conditions specified by design. 

A good example of this comparison is initializing the setting that controls the frame rate of a program compared to detecting input to control a Player- controlled sprite. The Player- controlled sprite will more likely have their objects interactions defined by a in-class funciton. Frame rate however would be independently defined in the event loop. 

## What are the functionalities of Pygame?

The Pygame modules utility allow for simple and easy to understand game design, its entirely modular allowing for imported interactions with other elements outside of Pygame, it harnesses a surprisingly small amount of code given the detail put into the utility, and serves as a free alternative to many other game design options [REF](https://www.pygame.org/wiki/about). 

## When was Pygame created?

Pygame was created on October 28th, 2000 [REF](https://www.pygame.org/docs/tut/PygameIntro.html). 

## Why did you select Pygame?

I selected Pygame because I'd already had some familiarity with Python as a programming language from CS1003 during WI2023 term at UNB. I decided early on that I'd prefer a Python based library because of this past experience with the language. One of my goals for after graduation from UNB is to work with video games in some way. This is because I really enjoy video games and was always very interested in learning how to build them, but never really had an excuse to research on this process. While browsing for a topic for my Exploration Activity 1 in CS2613 I found the Pygame library for Python and found that it's easy to install, easy to understand with my experience of object oriented programming from CS1073 and CS1083, and I could see the results programming using this utility very quickly. I decided that this would be a good excuse to research an example of a video game design tool based on these consideration factors. 

## How did learning the Pygame influence your learning of the language?

Bridging the process of learning a language and relating it to something I enjoy outside of school that requires software development and programming language proficiency has helped develop my interesting in learning Python considerably. I was also really surprised that the Pygame program was created in 2000 considering it seems to still be optimized for the current version of Python 24 years later. 

### How was your overall experience with the package/library?

Overall, the overall experience with Pygame was very positive. Originally I was researching another Python Library called PyBrain and the lack of optimization and exceptions returned from even trying to view the PyBrain module emphasized my appreciation for how quickly Pygame was installed and ready to use. 

### Would you continue using this package/library?

Yes, I've book marked the references provided in this document and plan on continuing to use this program to help better my understanding of Python. I've actually already done some reading on the way that Pygame utilizes hardware processors for information I/O and also done some research on how SDL and C programming is used to help reduce cost of Pygame utilities. 