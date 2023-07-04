# TASk 1
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
# drink.taste = "Strawberry"
print(drink)
