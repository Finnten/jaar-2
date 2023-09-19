# S_Rectangle class

import pygame
import math
from Shape import*

#2 Define the colours Red, Green


#3 Define the class object

class Square(Shape):

    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    PURPLE = (255,0,255)
    YELLOW = (255,255,0)
    CYAN = (0,255,255)
    MAGENTA = (255,0,255)
    BLACK = (0,0,0)

    colorlist = [RED, GREEN, BLUE, PURPLE, YELLOW, BLACK, MAGENTA, CYAN]

    def __init__(self, window, shapeType, maxWidth, maxHeight):
        super().__init__(window, 'Square', maxWidth, maxHeight)
        self.shapeType = shapeType
        self.width = maxWidth
        self.height = maxHeight

        # randomize the radius, x and y local
        self.color = random.choice(colorlist)
        self.x = random.randint(30,400)
        self.y = random.randint(30,400)

#4 Define the methods to check if the location clicked is inside that Square
    def clickedInside(self, mousePoint):
        return (
            self.x <= mousePoint[0] <= self.x + self.width and
            self.y <= mousePoint[1] <= self.y + self.height
        )

#5 Define the method that returns the indormation clicked is a square
    def getType(self):
        return self.shapeType

#6 Define the method that returns the area of the square
    def getArea(self):
        theArea = self.width * self.height
        return theArea
    
#7 Define the method that draws the square with a random colour
    def draw(self):
        pygame.draw.rect(self.window, self.color, (self.x, self.y, self.width, self.height))
