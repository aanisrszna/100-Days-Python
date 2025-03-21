from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Create objects for Menu, CoffeeMaker, and MoneyMachine
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

while is_on:
    # Display the available menu items and prompt user for input
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ").lower()

    if choice == "off":
        is_on = False  # Turn off the machine
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if drink:
            # Check if resources are sufficient
            if coffee_maker.is_resource_sufficient(drink):
                # Process payment
                if money_machine.make_payment(drink.cost):
                    # Make the coffee
                    coffee_maker.make_coffee(drink)