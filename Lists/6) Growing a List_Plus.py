# 1. Jiho is updating a list of orders. He just received orders for "lilac" and "iris". 
# Create a list called new_orders that contains our new orders.
orders = ["daisy", "buttercup", "snapdragon", "gardenia", "lily"]

# Create new orders here:

new_orders = orders + ["lilac", "iris"]

#2. Use + to create a new list called orders_combined that combines orders with new_orders.
orders_combined = orders + new_orders

#3. Remove the # and whitespace in front of the list broken_prices. If you run this code, you’ll get an error: 
#       TypeError: can only concatenate list (not "int") to list
#Fix the command by inserting brackets ([ and ]) so that it will run without errors.
#broken_prices = [5, 3, 4, 5, 4] + 4
broken_prices = [5, 3, 4, 5, 4] + [4]
