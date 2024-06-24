class Shape:
    def __init__(self):
        pass
    
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length
    
    def area(self):
        return self.length * self.length
if __name__ == "__main__":
    shape = Shape()
    print(shape.area())

    square = Square(8)
    print(square.area())