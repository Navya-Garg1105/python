from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
class circle(shape):
    def __init__(self, radius):
        self.r = radius
    def area(self):
        print(3.14*self.r**2)
    def perimeter(self):
        print(2*3.14*self.r)

obj = circle(20)
obj.area()
obj.perimeter()
