# S_Rectangle class

import pygame
import math
from Shape import*

#2 Define the colours Red, Green

#3 Define the class object

class Square(Shape):


    def __init__(self, window, shapeType, maxWidth, maxHeight, color):
        super().__init__(window, 'Square', maxWidth, maxHeight, color)
        self.shapeType = shapeType
        self.width = maxWidth
        self.height = maxHeight = maxWidth

        # randomize the radius, x and y local
        self.color = color
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
