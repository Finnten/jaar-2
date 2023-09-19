# S_Rectangle class

import pygame
import math
from Shape import*

#2 Define the colours Red, Green


#3 Define the class object

class Triangle(Shape):

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
        super().__init__(window, 'Triangle', maxWidth, maxHeight)
        self.shapeType = shapeType
        self.window = window
        self.width = maxWidth
        self.height = maxHeight
        self.triangleSlope = -1 * (self.height / self.width)
        

        # randomize the radius, x and y local
        self.color = random.choice(colorlist)
        self.x = random.randint(30,400)
        self.y = random.randint(30,400)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

#4 Define the methods to check if the location clicked is inside that Square
    def clickedInside(self, mousePoint):
        inRect = self.rect.collidepoint(mousePoint)
        if not inRect:
            return False
        
        # Do some math to see if the point is inside the triangle
        xOffset = mousePoint[0] - self.x
        yOffset = mousePoint[1] - self.y
        if xOffset == 0:
            return True
        
        # Calculate the slope (rise over run)
        pointSlopeFromYIntercept = (yOffset - self.height) / xOffset
        if pointSlopeFromYIntercept < self.triangleSlope:
            return True
        else:
            return False

#5 Define the method that returns the indormation clicked is a square
    def getType(self):
        return self.shapeType

#6 Define the method that returns the area of the square
    def getArea(self):
        theArea = .5 * self.width * self.height
        return theArea
    
#7 Define the method that draws the square with a random colour
    def draw(self):
        pygame.draw.polygon(self.window, self.color,
            ((self.x, self.y + self.height),
             (self.x, self.y),
             (self.x + self.width, self.y)))