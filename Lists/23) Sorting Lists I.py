# 1. Use .sort() to sort addresses.
addresses = ["221 B Baker St.", "42 Wallaby Way", "12 Grimmauld Place", "742 Evergreen Terrace", "1600 Pennsylvania Ave", "10 Downing St."]
addresses.sort()
# 2. Use print() to see how addresses changed.
print(addresses)

# 3. Remove the # and whitespace in front of the line sort(names). Edit this line so that it runs without producing a NameError.
names = ["Ron", "Hermione", "Harry", "Albus", "Sirius"]
#sort(names)
names.sort()

# 4. Use print to examine sorted_cities. Why is it not the sorted version of cities?
cities = ["London", "Paris", "Rome", "Los Angeles", "New York"]
sorted_cities = cities.sort()
print(sorted_cities)

# 5. Edit the .sort() call on cities such that it sorts the cities in reverse order (descending). Print cities to see the result.
cities.sort(reverse=True)
print(cities)



