# Task 1
class Soda:
    taste = None

    def __init(self, taste):
        self.taste = taste

    def __str__(self):
        if self.taste:
            return f"You've got soda with {self.taste} taste"
        else:
            return "You've got common soda"


drink = Soda()
drink.taste = "Strawberry"
print(drink)


# Task 2
class Math:

    def addition(self, x, y):
        return x + y

    def substraction(self, x, y):
        return x - y

    def multiplication(self, x, y):
        return x * y

    def division(self, x, y):
        if y != 0:
            return x / y
        else:
            return "You can do it"


add = Math()
sub = Math()
mult = Math()
div = Math()
print(add.addition(14, 6))
print(sub.substraction(10, 3))
print(mult.multiplication(10, 3))
print(div.division(10, 3))


# Task 3
class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def start(self):
        print("Car started")

    def off(self):
        print("Car is turned off")

    def set_color(self, color):
        self.color = color

    def set_type(self, type):
        self.type = type

    def set_year(self, year):
        self.year = year


car = Car(color="red", type="electric", year="2011")
car.start()
car.off()

# Task 4
from math import pi


class Sphere:
    def __init__(self, r=1, x=0, y=0, z=0):
        self.r = r
        self.x = x
        self.y = y
        self.z = z

    def get_volume(self):
        return (self.r ** 3) * pi * 4 / 3

    def get_square(self):
        return (self.r ** 2) * pi * 4

    def get_radius(self):
        return self.r

    def get_center(self):
        return self.x, self.y, self.z

    def set_radius(self, r):
        self.r = r

    def set_center(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def is_point_inside(self, x, y, z):
        return (self.x - x) ** 2 + (self.y - y) ** 2 + (self.z - z) ** 2 < self.r ** 2


# Task 5
class SuperStr(str):
    def __init__(self, value):
        super()
        self.value = value

    def is_repeatance(self, s):
        if self.value == s * (len(self.value) // len(s)):
            print(True)
        else:
            print(False)

    def is_palindrom(self):
        if self.value == self.value[::-1]:
            print(True)
        else:
            print(False)
