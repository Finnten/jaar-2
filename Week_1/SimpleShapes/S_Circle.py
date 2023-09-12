#circle class

#1inport packages

#2 Define the colours Red, Green
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Circle():
#3 Define the class object
    def __init__(self, window, maxWidth, maxHeight):
        self.window = window
        self.color = color
        self.radius = radius
        self.x = x
        self.y = y
        

        self.rect = pygame.Rect(self.x, self.y, self.radius * 2, self.radius * 2)
        self.shapeRype = 'Circle'
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
        pygame.draw.Circle(self.window, self.color, (self.x, self.y), self.radius)