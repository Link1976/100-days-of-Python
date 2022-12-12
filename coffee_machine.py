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

def process_coins(): 
    print(f"The cost of {selection} is {drink_cost}. Please insert coins. \n")
    total_inserted_coins = int(input("How many quarters?: ")) * 0.25
    total_inserted_coins += int(input("How many dimes?: ")) * 0.1
    total_inserted_coins += int(input("How many nickles?: ")) * 0.05
    total_inserted_coins += int(input("How many pennies?: ")) * 0.01
    if total_inserted_coins < drink_cost: 
        print("The amount of coins inserted is insufficient. ")
        return False
    elif total_inserted_coins == drink_cost:
        print(f"enjoy your {selection}!")
        return True
    else: 
        change = total_inserted_coins - drink_cost
        print(f"your change is {change}")
        print(f"enjoy your {selection}!")
        return True

def program_selection(program):
#selection of program and impact in resources
        if program == "espresso":
            resources["water"] -= MENU[program]["ingredients"]["water"]
            resources["coffee"] -= MENU[program]["ingredients"]["coffee"]
            return resources

        elif program == "latte":
            resources["water"] -= MENU[program]["ingredients"]["water"]
            resources["milk"] -= MENU[program]["ingredients"]["milk"]
            resources["coffee"] -= MENU[program]["ingredients"]["coffee"]
            return resources

        elif program == "cappuccino":
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
        drink_cost = drink["cost"]
        if enough_ingredients(drink_ingredients):
            cash_enough = False
            while not cash_enough:
                if process_coins():
                    program_selection(selection)
                    profit += drink_cost
                    cash_enough = True
                else:
                    cash_enough = False
        else:
            print("you don't have enough ingredients")
            is_on = False