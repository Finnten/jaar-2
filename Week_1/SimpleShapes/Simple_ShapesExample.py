# because all the randomness does not help to concentrate on the shapes I modified Main_shapesExample to this one
# and accept that I need simple shapes that do not choose colors and size themselves,
# and also accept that I have to init those shapes with parameters when creating them.

import pygame
import sys
from pygame.locals import *
from S_Rectangle import *
from S_Circle import *  # already ailable but the implementation left to you
from S_Triangle import *
from S_Square import *  # tip: make this a child of rectangle
import pygwidgets

# Set up the constants
WHITE = (255, 255, 255)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

# Set up the window
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
clock = pygame.time.Clock()

shapesList = [] # I keep a shapesList but the init of the objects changes, in fact only 3 shapes to start with

# Named calling is using the exact name like Color=Green
# the parameter list for simpleshapes is (window, Width, Height, Color, X, Y) to be filled in here    

RShape = S_Rectangle(window, Width=50, Height=150, Color=BLUE, X=100, Y=100)
shapesList.append(RShape)

TShape = S_Triangle(window, Width=100, Height=100, Color=GREEN, X=200, Y=200)
shapesList.append(TShape)

oStatusLine = pygwidgets.DisplayText(window, (4,4),'Click on shapes', fontSize=28)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            # Reverse order to check last drawn shape first
            for oShape in shapesList:
                if oShape.clickedInside(event.pos):
                    area = oShape.getArea()
                    area = str(area)
                    theType = oShape.getType()
                    newText = 'Clicked on a ' + theType + ' whose area is ' + area
                    oStatusLine.setValue(newText)
                    break # only deal with topmost shape

    # Tell each shape to draw itself
    window.fill(WHITE)
    for oShape in shapesList:
        oShape.draw()
    oStatusLine.draw()

    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)
