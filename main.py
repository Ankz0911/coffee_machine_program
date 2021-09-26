from data import MENU
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
commands = ["espresso", "latte", "cappuccino", "report", "off"]

def coffee_maker():

    def pour_water(value_element, name_element):
        if value_element <= resources[name_element]:
            return resources[name_element] - value_element
        else:
            return False


    def accept_money():
        quarters = float(input('Kindly insert quarters\n'))
        dimes = float(input('Kindly insert dimes\n'))
        mickel = float(input('Kindly insert nickel\n'))
        pennies = float(input('Kindly insert pennies\n'))
        return (quarters * 0.25 + dimes * 0.10 + mickel * 0.05 + pennies * 0.01) - user_demand_cost

    def program_restart() :
        variable_e = input('Type y to restart\n')
        if variable_e == 'y' :
            coffee_maker()
        else:
            print('invalid input')


    user_demand = input('What would you like to have today ? espresso , latte or cappuccino ?')
    if user_demand not in commands:
        print('invalid input')
        program_restart()
    elif user_demand == "report" :
        print(f"current resources are {resources}\n")
        program_restart()
    elif user_demand == "off":
        quit()


    variable_a = MENU[user_demand]
    user_demand_ingredients = variable_a['ingredients']
    user_demand_cost = variable_a['cost']

    water_value = user_demand_ingredients["water"]
    milk_value = user_demand_ingredients["milk"]
    coffee_value = user_demand_ingredients["coffee"]

    variable_b = pour_water(water_value, "water")
    variable_c = pour_water(milk_value, "milk")
    variable_d = pour_water(coffee_value, "coffee")

    if variable_a != False and variable_b != False and variable_c != False:
        resources['water'] = variable_b
        resources['milk'] = variable_c
        resources['coffee'] = variable_d
        print(f"kindly insert : ${user_demand_cost}")
        change = accept_money()
        print(f"here's your remaining ${change}")
        print('enjoy your coffee')
        program_restart()
    else:
        print("sorry we are unable to process your drink")

        program_restart()


coffee_maker()