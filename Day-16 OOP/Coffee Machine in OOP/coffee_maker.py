class CoffeeMaker:
    def __init__(self):
        self.resuorces = {
            "water": 300,
            "milk" : 200,
            "coffee" : 100,
        }
    
    def report(self):
        print(f"Water: {self.resuorces['water']}ml")
        print(f"Milk: {self.resuorces['milk']}ml")
        print(f"Coffee: {self.resuorces['coffee']}g")
    
    def is_resources_sufficient(self, drink):
        can_make = True
        for item in drink.ingrediants:
            if drink.ingrediants[item] > self.resuorces[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make

    def make_coffee(self, order):
        for item in order.ingrediants:
            self.resuorces[item] -= order.ingrediants[item]
        print(f"Here is your {order.name}. Enjoy!")
            
