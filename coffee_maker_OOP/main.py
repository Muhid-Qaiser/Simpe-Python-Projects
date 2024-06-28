from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def report():
    print("\nResources: "
          "\n-----------------------")
    coffee_maker.report()
    money_machine.report()
    print("-----------------------\n")


menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


is_on = True
options = menu.get_items()

while is_on:

    choice = input(f"\nWhat would you like? ({options}): ").lower()

    if choice == 'report':
        report()
    elif choice == 'off':
        is_on = False
        print("\nShutting off...")
    else:
        drink_chosen = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink_chosen) and money_machine.make_payment(drink_chosen.cost):
            coffee_maker.make_coffee(drink_chosen)
