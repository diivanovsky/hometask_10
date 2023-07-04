# Task 1
class Soda:
    taste = None

    def __init(self, taste):
        self.taste = taste

    def __str__(self):
        if self.taste:
            return f"You 've got soda with {self.taste} taste"
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
