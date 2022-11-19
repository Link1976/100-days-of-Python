MENU = {

    "espresso": {

        "ingredients": {

            "water": 50,

            "coffee": 18,

        },

        "cost": 1.5,

    },

    "latte": {

        "ingredients": {

            "water": 200,

            "milk": 150,

            "coffee": 24,

        },

        "cost": 2.5,

    },

    "cappuccino": {

        "ingredients": {

            "water": 250,

            "milk": 100,

            "coffee": 24,

        },

        "cost": 3.0,

    }

}

profit = 0

resources = {

    "water": 300,

    "milk": 200,

    "coffee": 100,

}

       

def enough_ingredients(order_ingredients):
    for ingredient in order_ingredients:
        if order_ingredients[ingredient] >= resources[ingredient]:
            return False
        else:
            return True       

def program_selection(program):
#selection of program and impact in resources
        if program == "espresso":
            print(f"Enjoy your {program}!")
            resources["water"] -= MENU[program]["ingredients"]["water"]
            resources["coffee"] -= MENU[program]["ingredients"]["coffee"]
            return resources

        elif program == "latte":
            print(f"Enjoy your {program}!")
            resources["water"] -= MENU[program]["ingredients"]["water"]
            resources["milk"] -= MENU[program]["ingredients"]["milk"]
            resources["coffee"] -= MENU[program]["ingredients"]["coffee"]
            return resources

        elif program == "cappuccino":
            print(f"Enjoy your {program}!")
            resources["water"] -= MENU[program]["ingredients"]["water"]
            resources["milk"] -= MENU[program]["ingredients"]["milk"]
            resources["coffee"] -= MENU[program]["ingredients"]["coffee"]
            return resources    

       

is_on = True

while is_on:

    selection = input("What would you like (espresso / latte / cappuccino)?: \n")
    
    if selection == "off":
        print("Goodbye! ")
        is_on = False

    elif selection == "report":
        print("The level of of water is " +  str(resources["water"]) + ".")
        print("The level of of milk is "+ str(resources["milk"]) + ".")
        print("The level of of coffee is "+ str(resources["coffee"]) + ".")
        print("Total cash is "+ str(profit) + ".")

    else:

        drink = MENU[selection]
        drink_ingredients = drink["ingredients"]
        if enough_ingredients(drink_ingredients):
            program_selection(selection)
        else:
            print("you don't have enough ingredients")
            is_on = False