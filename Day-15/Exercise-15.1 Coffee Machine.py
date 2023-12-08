from coffeemachinelogo import logo
from coffemachineresource import MENU, resources

print(logo)
iteration = False
def report():
    for key in resources:
        print(f"{key}: {resources[key]}")

while not iteration:
    ask= input("What would you like? (espresso/latte/cappuccino): ").lower()
    if ask =="report":
        report()
    elif ask == "latte" or ask == "espresso" or ask == "cappuccino":
        if ask == "espresso":
            if resources['water']>=50 and resources['coffee']>=18:
                coffee_price = MENU[ask]['cost']
                resources['money'] +=coffee_price
                print("Price is: ",coffee_price)
                print("Please Insert coins.")
                quarters = int(input("How many quarters?: "))
                dimes = int(input("How many dimes?: "))
                nickles = int(input("How many nickles?: "))
                pennies = int(input("How many pennies?: "))
                gave_money = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
                return_money = gave_money - coffee_price
                if coffee_price> gave_money:
                    print("Sorry that's not enough money. Money refunded.")
                    iteration = True
                elif gave_money>=coffee_price:
                    print(f"Here is ${return_money:.2f} dollars in change.")

                resources['water'] -= 50
                resources['coffee'] -= 18
            else:
                print("Sorry there is not enough ingredients")
                iteration = True
                
        elif ask == "latte":
            if resources['water']>=200 and resources['milk']>=150 and resources['coffee']>=24:
                coffee_price = MENU[ask]['cost']
                resources['money'] +=coffee_price
                print("Price is: ",coffee_price)
                print("Please Insert coins.")
                quarters = int(input("How many quarters?: "))
                dimes = int(input("How many dimes?: "))
                nickles = int(input("How many nickles?: "))
                pennies = int(input("How many pennies?: "))
                gave_money = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
                return_money = gave_money - coffee_price
                if coffee_price> gave_money:
                    print("Sorry that's not enough money. Money refunded.")
                    iteration = True
                elif gave_money>=coffee_price:
                    print(f"Here is ${return_money:.2f} dollars in change.")

                resources['water'] -= 200
                resources['milk'] -= 150
                resources['coffee'] -= 24
            else:
                print("Sorry there is not enough ingredients")
                iteration = True

        elif ask == "cappuccino":
            if resources['water']>=250 and resources['milk']>=100 and resources['coffee']>=24:
                coffee_price = MENU[ask]['cost']
                resources['money'] +=coffee_price
                print("Price is: ",coffee_price)
                print("Please Insert coins.")
                quarters = int(input("How many quarters?: "))
                dimes = int(input("How many dimes?: "))
                nickles = int(input("How many nickles?: "))
                pennies = int(input("How many pennies?: "))
                gave_money = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
                return_money = gave_money - coffee_price
                if coffee_price> gave_money:
                    print("Sorry that's not enough money. Money refunded.")
                    iteration = True
                elif gave_money>=coffee_price:
                    print(f"Here is ${return_money:.2f} dollars in change.")

                resources['water'] -= 250
                resources['milk'] -= 100
                resources['coffee'] -= 24
            else:
                print("Sorry there is not enough ingredients")
                iteration = True
    elif ask == "off":
        iteration = True