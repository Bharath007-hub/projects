class Polygon:
    def area(self):
        pass

class Rectangle(Polygon):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

class Square(Polygon):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

def main():
    shapes = [
        Rectangle(10, 5),
        Square(4)
    ]

    for shape in shapes:
        print(f"{shape.__class__.__name__} area: {shape.area()}")

main()
