def triangle_validity(x,y,z):
    if x+y>=z and y+z>=x and z+x>=y:
        return True
    else:
        return False

side_x = float(input('Please enter length for side x: '))
side_y = float(input('Please enter length for side y: '))
side_z = float(input('Please enter length for side z: '))


if triangle_validity(side_x, side_y, side_z):
    print('Triangle is Valid.')
    if side_x == side_y == side_z:
     print("Equilateral triangle")
    elif side_x==side_y or side_y==side_z or side_z==side_x:
     print("isosceles triangle")
    else:
     print("Scalene triangle")

else:
    print('Triangle is Invalid.')

