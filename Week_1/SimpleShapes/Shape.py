# 1inport packages

from abc import ABC, abstractmethod
import pygame
import random

#2 Define the colours Red, Green
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (255,0,255)
YELLOW = (255,255,0)
CYAN = (0,255,255)
MAGENTA = (255,0,255)
BLACK = (0,0,0)

colorlist = [RED, GREEN, BLUE, PURPLE, YELLOW, BLACK, MAGENTA, CYAN]

#,maxWidth, maxHeight)  

#3 Define the class object
class S_Circle():
    def __init__(self, window, shapeType):
        self.shapeType = shapeType
        self.window = window
        self.color = random.choice(colorlist)
        self.maxWidth = random.randint(20,200)
        self.maxHeight = random.randint(20,200)
        self.x = random.randint(100,500)
        self.y = random.randint(100,400)
        
    
#4 Define the methods to check if the location clicked is inside that circle
    @abstractmethod
    def clickedInside(self, mousePoint):
        clicked = self.rect.collidepoint(mousePoint)
        raise NotImplementedError('clickedInside must be defined in subclasses')
        return clicked
    
#5 Define the method that returns the indormation clicked is a circle
    def getType(self):
        return self.shapeType
    
#6 Define the method that returns the area of the circle
    def getArea(self):
        theArea = self.maxWidth * self.maxHeight
        return theArea
#7 Define the method that draws the circle with a random colour
    def draw(self):
        pygame.draw.rect(self.window, self.color, (self.x, self.y, self.maxWidth, self.maxHeight))