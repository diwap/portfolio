class Car:
    def __init__(self, color, brand, owner):
        self.color = color
        self.brand = brand
        self.owner = owner

    def get_detail(self):
        return "There is %s %s car owned by %s." % (
            self.color,
            self.brand,
            self.owner
        )

    def say_hi_to_owner(self):
        return "Hey, what's up %s?" % self.owner

car1 = Car("red", "bugatti", "Aayush")

print(car1.get_detail())

print(car1.say_hi_to_owner())

print(car1.color)