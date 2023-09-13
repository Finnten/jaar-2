# S_Rectangle class

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

class S_Rectangle():

    def __init__(self, window, Width, Height, Color, X, Y):
        self.window = window
        self.width = Width
        self.height = Height
        self.color = Color
        self.x = X
        self.y = Y
        self.rect = pygame.Rect(self.x, self.y, self.width,self.height)
        self.shapeType = 'Rectangle'
        
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
