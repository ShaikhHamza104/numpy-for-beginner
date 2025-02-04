import math

def sum_of_interior_angles(n):
    return (n - 2) * 180

def measure_of_interior_angle(n):
    return ((n - 2) * 180) / n

def sum_of_exterior_angles():
    return 360

def measure_of_exterior_angle(n):
    return 360 / n

def area_of_regular_polygon(n, s):
    return (n * s**2) / (4 * math.tan(math.pi / n))

def main():
    print('Welcome to Polygon Area Calculator')
    print('Please enter the number of sides you wish to calculate')
    n = int(input('''
    1.Sum of Interior angles
    2.Sum of Exterior angles
    3.Area of regular polygon
    4.measure of exterior angle
    5.area of regular polygon
    6.Exit
    '''))
    print('Please enter the number of sides you wish to calculate')
    side = int(input())
    if n == 1:
        sum_of_interior_angles(side)
    elif n == 2:
        sum_of_exterior_angles()
    elif n == 3:
        area_of_regular_polygon(side, side)
    elif n == 4:
        measure_of_exterior_angle(side)
    elif n == 5:
        area_of_regular_polygon(side, side)
    elif n == 6:
        exit()
    else:
        print('Invalid input')
main()