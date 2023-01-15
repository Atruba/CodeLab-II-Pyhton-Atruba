class shape():
   
    def calculateArea(self,*args):
        a = 1
        [a:= a*i for i in args]
        return a
    def __init__(self, r = None, s1 = None, s2 = None, b = None, h = None):
        self.radius = r
        self.side1 = s1
        self.side2 = s2
        self.base = b
        self.height = h
    def inputSidesC(self):
        self.radius = int(input("Enter radius: "))
        circle()
    def inputSidesR(self):
        self.side1 = int(input("Enter side 1: "))
        self.side2 = int(input("Enter side 2: "))
        rectangle()
    def inputSidesT(self):
        self.base = int(input("Enter base: "))
        self.height = int(input("Enter height: "))
        triangle()
class circle(shape):
    def __init__(self, r = None):
        self.radius = r
    def area(self):
        pi = 3.14159265359
        return self.calculateArea(float(self.radius),pi,2)

class rectangle(shape):
    def __init__(self):
        self.side1 = float(input("edge 1"))
        self.side2 = float(input("edge 2"))
    def calculateArea(self):
        return self.side1 * self.side2
class triangle(shape):
    def __init__(self, b = None, h = None):
        self.base = b
        self.height = h
    def area(self):
        print("Area of triangle: ", 0.5 * self.base * self.height)

c = circle(input("Enter Circle Radius"))
print(c.area())

r = rectangle()
print(r.calculateArea())

t = triangle()
t.inputSidesT()