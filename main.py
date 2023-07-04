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


