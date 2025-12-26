

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, w, h):
        self.w, self.h = w, h

    def area(self):
        return self.w * self.h

    def perimeter(self):
        return 2 * (self.w + self.h)


class Circle(Shape):
    def __init__(self, r):
        self.r = r
        self.pi = 3.24159

    def area(self):
        return self.pi * self.r ** 2

    def perimeter(self):
        return 2 * self.pi * self.r


shapes = [Rectangle(5, 10), Circle(7)]

for s in shapes:
    print("Area:", s.area())
    print("Perimeter:", s.perimeter())
    print()
