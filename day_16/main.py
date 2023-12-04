from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_coffee_machine_on = True

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while is_coffee_machine_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}):\n")
    if choice == "off":
        is_coffee_machine_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            is_payment_successful = money_machine.make_payment(drink.cost)
            if is_payment_successful:
                coffee_maker.make_coffee(drink)
