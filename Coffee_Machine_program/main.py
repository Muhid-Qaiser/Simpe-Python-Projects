from data import MENU, resources
from art import logo, coffee_art


def print_report(money):
    print(f'''\nResources:
Water : {resources['water']}
Milk : {resources['milk']}
Coffee : {resources['coffee']}
Money : {money} ''')


def check_coffee_type(coffee_chosen):
    if coffee_chosen == 'latte' or coffee_chosen == 'espresso' or \
            coffee_chosen == 'cappuccino':
        return True
    return False


def check_resources(coffee_chosen):
    checker = True

    for item in coffee_chosen['ingredients']:
        if resources[item] < coffee_chosen['ingredients'][item]:
            checker = False

    return checker


def get_insufficient_resource(coffee_chosen):
    for item in coffee_chosen['ingredients']:
        if resources[item] < coffee_chosen['ingredients'][item]:
            return item


def deduct_resources(coffee_chosen):
    for item in coffee_chosen['ingredients']:
        resources[item] -= coffee_chosen['ingredients'][item]


def coffee_machine():

    money = 0

    while True:

        print(f"\n{logo} \n   Welcome to the Coffee Machine.")

        user_choice = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()

        if user_choice == 'report':
            print_report(money)

        elif user_choice == 'off':
            print("\nShutting down...")
            return

        elif check_coffee_type(user_choice):
            coffee = MENU[user_choice]

            if not check_resources(coffee):
                print(f"\nSorry, there is not enough {get_insufficient_resource(coffee)}.")
                # return

            else:
                print("\nPlease insert coins.")
                quarters = int(input("How many quarters? : ")) * 0.25
                dimes = int(input("How many dimes? : ")) * 0.10
                nickles = int(input("How many nickles? : ")) * 0.05
                pennies = int(input("How many pennies? : ")) * 0.01
                temp_money = round(quarters + dimes + nickles + pennies, 2)

                if temp_money < coffee['cost']:
                    print("\nSorry, that's not enough money. Money refunded.")
                    # return

                else:
                    change = round(temp_money - coffee['cost'], 2)
                    print(f"\nHere is ${change} in change.\nEnjoy your {user_choice}.\n{coffee_art}"
                          f"\n--------------------------------------\n")

                    money = round(temp_money - change, 2)
                    deduct_resources(coffee)

        else:
            print("\nInvalid input.\nTry Again.\n")


coffee_machine()
