import math

class Shapes:
  def inputSides(self):
    self.side1 = float(input("Enter side one: "))
    self.side2 = float(input("Enter side two: "))

class circle(Shapes):
  def area(self):
    return math.pi * self.side1 ** 2

class rectangle(Shapes):
  def area(self):
    return self.side1 * self.side2

class triangle(Shapes):
  def area(self):
    return self.side1 * self.side2 / 2

shape = Shapes()
shape.inputSides()

circle = circle()
circle.side1 = shape.side1
print(f"Circle area: {circle.area():.2f}")

rectangle = rectangle()
rectangle.side1 = shape.side1
rectangle.side2 = shape.side2
print(f"Rectangle area: {rectangle.area():.2f}")

triangle = triangle()
triangle.side1 = shape.side1
triangle.side2 = shape.side2
print(f"Triangle area: {triangle.area():.2f}")
