import data


def is_resources_sufficient(order_ingredients):
    """Check if there are enough resources to fulfill the order."""
    for item in order_ingredients:
        if order_ingredients[item] >= data.resources[item]:
            print(f"Sorry, there is not enough {item}")
            return False
    return True


def process_coins():
    """Process the coins inserted by the user and return the total."""
    print("Please insert coins")
    total = float(input("How many quarters? ")) * 0.25
    total += float(input("How many dimes? ")) * 0.10
    total += float(input("How many nickels? ")) * 0.05
    total += float(input("How many pennies? ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Check if the payment is sufficient for the selected drink."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change")
        data.money += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources to make the coffee."""
    for item in order_ingredients:
        data.resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}!")


# Machine state
coffee_machine_on = True

# Main loop
while coffee_machine_on:
    # User input for the coffee order
    order = input("What would you like? (espresso/latte/cappuccino): ")

    # Machine options
    # Turn off the machine
    if order == "off":
        coffee_machine_on = False
    # Print report of available resources and money
    elif order == "report":
        print(f"Water: {data.resources['water']}")
        print(f"Milk: {data.resources['milk']}")
        print(f"Coffee: {data.resources['coffee']}")
        print(f"Money: ${data.money}")
    else:
        # Get details of the selected drink from the menu
        drink = data.MENU[order]
        # Check if there are enough resources
        if is_resources_sufficient(drink["ingredients"]):
            # Process user payment
            payment = process_coins()
            # Check if the transaction was successful
            if is_transaction_successful(payment, drink["cost"]):
                # Make the coffee and update resources
                make_coffee(order, drink["ingredients"])
