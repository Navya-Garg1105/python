import math
class Shape:
    def area(self):
        raise NotImplementedError

class Circle(Shape):
    def __init__(self, radius):
        # Initialize radius
        self.radius = radius
    
    # Implement this
    def area(self):
        return math.pi *self.radius **2

class Rectangle(Shape):
    def __init__(self, length, width):
        # Initialize dimensions
        self.length = length
        self.width = width
    
    # Implement this
    def area(self):
        return (self.length * self.width)

# Test Input
circle = Circle(7)
rectangle = Rectangle(10,8)
print(circle.area()) 
print(rectangle.area()) 