
#1 inport packages

import pygame
from Shape import*

#2 Define the colours Red, Green


#3 Define the class object

class Circle(Shape):
    def __init__(self, window, maxWidth, maxHeight):
        super().__init__(window, 'Circle', maxWidth, maxHeight)
        self.shapeType = shapeType
        self.window = window
        self.maxWidth = maxWidth
        self.maxHeight = maxHeight
    
#4 Define the methods to check if the location clicked is inside that circle
    def clickedInside(self, mousePoint):
        clicked = self.rect.collidepoint(mousePoint)
        return clicked
#5 Define the method that returns the indormation clicked is a circle
    def getType(self):
        return self.shapeType
    
#6 Define the method that returns the area of the circle
    def getArea(self):
        theArea = 3.14 * self.radius * self.radius
        return theArea
#7 Define the method that draws the circle with a random colour
    def draw(self):
        pygame.draw.circle(self.window, self.color, (self.x, self.y), self.radius)