from resources import resources, MENU

is_coffee_machine_on = True
profit = 0


def print_report(remain_resources, current_profit):
    """Prints the current resource values."""
    print(f"Water: {remain_resources['water']}ml")
    print(f"Milk: {remain_resources['milk']}ml")
    print(f"Coffee: {remain_resources['coffee']}g")
    print(f"Money: ${current_profit}")


def is_resource_sufficient(remain_resources, ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for key in remain_resources:
        if remain_resources[key] < ingredients[key]:
            print(f"Sorry there is not enough {key}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Returns True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = money_received - drink_cost
        formatted_change = "{:.2f}".format(change)
        if change > 0:
            print(f"Here is ${formatted_change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, ingredients):
    """Deduct the required ingredients from the resources."""
    for key in ingredients:
        resources[key] -= ingredients[key]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


while is_coffee_machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino):\n")
    if choice == "off":
        is_coffee_machine_on = False
    elif choice == "report":
        print_report(resources, profit)
    else:
        drink = MENU[choice]
        is_enough_money = is_resource_sufficient(resources, drink["ingredients"])
        if is_enough_money:
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
