heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

# 1. We have defined a list heights of visitors to a theme park. 
# In order to ride the Topsy Turvy Tumbletron roller coaster, you need to be above 161 centimeters.
# Using a list comprehension, create a new list called can_ride_coaster that has every element from heights that is greater than 161.
can_ride_coaster = []

can_ride_coaster = [height for height in heights if height > 161]

# 2. Print can_ride_coaster.
print(can_ride_coaster)
