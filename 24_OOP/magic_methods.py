class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def isSquare(self):
        if self.width == self.height:
            return False

    def __gt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() > other.area()
        else:
            return NotImplementedError

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.area() == other.area()
        else:
            return NotImplementedError

    def __repr__(self):
        return f"Rectangle Width:{self.width} and Height:{self.height}"


rectangle1 = Rectangle(20, 30)
rectangle2 = Rectangle(10, 40)


area1 = rectangle1.area()
print(area1)

print(rectangle1 > rectangle2)
print(rectangle1 > 20)
print(rectangle1 == rectangle2)  # comparison based on area

# print(rectangle1.__gt__(rectangle2))


print(rectangle1)
