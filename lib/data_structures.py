import pprint

spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

# 1. ====================================================================================
# Define a function get_names() that takes a list of spicy_foods and
# returns a list of strings with the names of each spicy food.
# @params: list(spicy_foods)
# @output: list of names
def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]

print(f"1. get_names => {get_names(spicy_foods)}", end='\n\n')




# 2. ====================================================================================
# Define a function get_spiciest_foods() that takes a list of spicy_foods and 
# returns a list of dictionaries where the heat level of the food is greater than 5.
# @params: list(spicy_foods)
# @output: list of spicy foods with a heat level greater than 5
def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food['heat_level']>5]

print(f"2. get_spiciest_foods => ")
pprint.pp(get_spiciest_foods(spicy_foods))
print('')




# 3. ====================================================================================
# Define a function print_spicy_foods() that takes a list of spicy_foods and output 
# to the terminal each spicy food in the following format using print():
# Buffalo Wings (American) | Heat Level: 🌶🌶🌶.
# @params: list(spicy_foods)
# @output: prints strings of spicy foods
def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶'*food['heat_level']}")
    # [print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶'*food['heat_level']}") for food in spicy_foods]

print(f"3. print_spicy_foods => ")
print_spicy_foods(spicy_foods)
print('')




# 4. ====================================================================================
# Define a function get_spicy_food_by_cuisine() that takes a list of spicy_foods and 
# a string representing a cuisine, and returns a SINGLE dictionary for the spicy food whose
# cuisine matches the cuisine being passed to the method.
# @params: list(spicy_foods), string(cuisine)
# @output: spicy food whose cuisine matches the `cuisine` argument
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    return next((food for food in spicy_foods if cuisine == food.get('cuisine')), 'Not Found')

print(f"4. get_spicy_food_by_cuisine => {get_spicy_food_by_cuisine(spicy_foods, 'Thai')}", end='\n\n')




# 5. ====================================================================================
# Define a function print_spiciest_foods() that takes a list of spicy_foods and outputs 
# to the terminal ONLY the spicy foods that have a heat level greater than 5, in the following format:
# Buffalo Wings (American) | Heat Level: 🌶🌶🌶
# @params: list(spicy foods)
# @output: prints spicy foods with a heat level greater than 5
def print_spiciest_foods(spicy_foods):
    print_spicy_foods(get_spiciest_foods(spicy_foods))

print(f"5. print_spiciest_foods =>")
print_spiciest_foods(spicy_foods)
print('')




# 6. ====================================================================================
# Define a function average_heat_level() that takes a list of spicy_foods and returns an integer
# representing the average heat level of all the spicy foods in the array. Recall that to derive
# the average of a collection, you need to calculate the total and divide number of elements in 
# the collection.
# @params: list(spicy foods)
# @output: number(average of heat levels)
def get_average_heat_level(spicy_foods):
    return sum([food['heat_level'] for food in spicy_foods]) / len(spicy_foods)

print(f"6. get_average_heat_level => {get_average_heat_level(spicy_foods)}", end='\n\n')




# 7. ====================================================================================
# Define a function create_spicy_food() that takes a list of spicy_foods and a new spicy_food and
# returns the original list with the new spicy_food added.
# @params: list(spicy_foods), dictionary(new spicy food)
# @output: list with new spicy food added
def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

print(f"7. create_spicy_food => ")
pprint.pp(create_spicy_food(
    spicy_foods, 
    {
        'name': 'Griot',
        'cuisine': 'Haitian',
        'heat_level': 10,
    }
    ))

pprint.pp(spicy_foods)