
#1 inport packages

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

color=random.choice(colorlist)
maxWidth=random.randint(10,100)
maxHeight=random.randint(10,100)  

#3 Define the class object
class Shape(ABC):
    def __init__(self, window, shapeType, maxWidth, maxHeight,color):
        self.shapeType = shapeType
        self.window = window
        self.maxWidth = maxWidth
        self.maxHeight = maxHeight
        self.color = color
        
        
    
#4 Define the methods to check if the location clicked is inside that circle
    @abstractmethod
    def clickedInside(self, mousePoint):
        raise NotImplementedError('clickedInside must be defined in subclasses')
    
#5 Define the method that returns the indormation clicked is a circle

    
#6 Define the method that returns the area of the circle
    @abstractmethod
    def getArea(self):
        raise NotImplementedError('getArea must be defined in subclasses')
    
#7 Define the method that draws the circle with a random colour
    @abstractmethod
    def draw(self):
        raise NotImplementedError('draw must be defined in subclasses')