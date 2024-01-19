# Importing necessary classes from the respective modules
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Creating instances of the Menu, CoffeeMaker, and MoneyMachine classes
machine_menu = Menu()
coffee_machine = CoffeeMaker()
register = MoneyMachine()

# Variable to control the main loop
is_on = True

# Main program loop
while is_on:
    # Prompting the user to input their order
    order = input("What would you like? (espresso/latte/cappuccino): ")

    # Checking if the user wants to turn off the coffee machine
    if order == 'off':
        is_on = False
    # Checking if the user wants a report of the coffee machine's resources
    elif order == 'report':
        coffee_machine.report()
    else:
        # Finding the drink object based on the user's order
        drink = machine_menu.find_drink(order)

        # Checking if there are enough resources to make the selected drink
        if coffee_machine.is_resource_sufficient(drink):
            # Checking if the user has made a successful payment for the drink
            if register.make_payment(drink.cost):
                # Making the coffee if both resource and payment conditions are met
                coffee_machine.make_coffee(drink)
