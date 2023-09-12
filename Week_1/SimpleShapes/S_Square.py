# S_Rectangle class

import pygame

# Set up the colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class S_Square():

    def __init__(self, window, Width, Height, Color, X, Y):
        self.window = window
        self.width = Width
        self.height = Width
        self.color = Color
        self.x = X
        self.y = Y
        self.rect = pygame.Rect(self.x, self.y, self.width,self.height)
        self.shapeType = 'Square'
        
    def clickedInside(self, mousePoint):
        clicked = self.rect.collidepoint(mousePoint)
        return clicked

    def getType(self):
        return self.shapeType
    
    def getArea(self):
        theArea = self.width * self.height
        return theArea

    def draw(self):
        pygame.draw.rect(self.window, self.color, (self.x, self.y, self.width, self.height))
