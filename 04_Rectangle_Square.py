class Rectangle:
    def __init__(self):
        self.width=0
        self.height=0

    def set_width(self,width):
        self.width=width

    def set_height(self,height):
        self.height=height

    def area(self):
        return self.width*self.height


class Square(Rectangle):
    def set_width(self,width):
        self.width=width
        self.height=width

    def set_height(self,height):
        self.width=height
        self.height=height


rectangle=Rectangle()
rectangle.set_width(10)
rectangle.set_height(20)

print("Rectangle area:",rectangle.area())

square=Square()
square.set_width(10)
square.set_height(20)

print("Square area:",square.area())

print()
print("Expected Rectangle area: 10 x 20 = 200")
print("Actual Square area:",square.area())