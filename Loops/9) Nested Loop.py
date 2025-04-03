sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

# 1. We have provided the list sales_data that shows the number of scoops sold for different flavors of ice cream at three different locations: Scoopcademy, Gilberts Creamery, and Manny’s Scoop Shop.
# We want to sum up the total number of scoops sold across all three locations. Start by defining a variable scoops_sold and set it to zero.

# 2. Loop through the sales_data list using the following guidelines: 
# a. For our temporary variable of the for loop, call it location.
# b. print() out each location list.
scoops_sold = 0
# 3. Within our sales_data loop, nest a secondary loop to go through each location sublist element and add the element value to scoops_sold.
# By the end, you should have the sum of every number in the sales_data nested list.
# Checkpoint 4 Step instruction is unavailable until previous steps are completed
for location in sales_data:
  print(location)
# 4. Print out the value of scoops_sold outside of the nested loop.
for location in sales_data:
  print(location)
  for sale in location:
     scoops_sold = scoops_sold + sale
print(scoops_sold)





