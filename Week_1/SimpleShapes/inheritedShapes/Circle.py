
#1 inport packages

import pygame
from Shape import*
import math

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

#3 Define the class object

class Circle(Shape):
  
    def __init__(self, window, shapeType, maxWidth, maxHeight):
        super().__init__(window, 'Circle', maxWidth, maxHeight)
        self.shapeType = shapeType

        # randomize the radius, x and y local
        self.color = random.choice(colorlist)
        self.radius = random.randint(10,50)
        self.x = random.randint(100,500)
        self.y = random.randint(100,400)
    
#4 Define the methods to check if the location clicked is inside that circle
    def clickedInside(self, mousePoint):
        distance = math.sqrt((mousePoint[0] - self.x) ** 2 + (mousePoint[1] - self.y) ** 2)
        return distance <= self.radius
    
#5 Define the method that returns the indormation clicked is a circle
    def getType(self):
        return f"{self.shapeType} ({self.radius})" # this is a string, not a number, so no need to convert to string (str()
    
#6 Define the method that returns the area of the circle
    def getArea(self):
        theArea = math.pi* self.radius * self.radius
        return theArea
#7 Define the method that draws the circle with a random colour
    def draw(self):
        pygame.draw.circle(self.window, self.color, (self.x, self.y), self.radius)