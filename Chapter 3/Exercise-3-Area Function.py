print("Menu: ")
print("1. Calculate the area of a square")
print("2. Calculate the area of a circle")
print("3. Calculate the area of a triangle")
x=int(input("Choose your option: "))

if x==1:
    a = int(input("Enter the side:"))
    print("Area of square=",a*a)
elif x==2:
    r=int(input("Enter the radius of the circle: "))
    print("Area of circle =", 3.14*r*r)
elif x==3:
    b = int(input("Enter the base : "))
    h = int(input("Enter the height : "))
    area = b*h/2
    print("Area of triangle =",area)
else:
    print("Choose your option correctly!")     