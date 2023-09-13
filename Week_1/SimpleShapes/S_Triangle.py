# S_Triangle class

import pygame

# Set up the colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (255,0,255)
YELLOW = (255,255,0)
CYAN = (0,255,255)
MAGENTA = (255,0,255)
BLACK = (0,0,0)

class S_Triangle():  
    # Named calling is using the exact name like Color=Green

    def __init__(self, window, Width, Height, Color, X, Y):
        self.window = window
        self.width = Width
        self.height = Height
        self.triangleSlope = -1 * (self.height / self.width)
        self.color = Color
        self.x = X
        self.y = Y
        self.rect = pygame.Rect(self.x, self.y,
                                            self.width, self.height)
        self.shapeType = 'Triangle'
        
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

    def getType(self):
        return self.shapeType

    def getArea(self):
        theArea = .5 * self.width * self.height
        return theArea

    def draw(self):
        pygame.draw.polygon(self.window, self.color,
            ((self.x, self.y + self.height),
             (self.x, self.y),
             (self.x + self.width, self.y)))
