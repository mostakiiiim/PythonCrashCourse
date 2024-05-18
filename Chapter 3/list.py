cities = ['munich', 'ingolstadt', 'hamm', 'nuremburg']

print(cities)

print(cities[1])

print(cities[1].title())

# Modifying elements in the list by accessing using [] and changing it

cities[3] = 'dortmund'

print(cities)

# Adding new items to existing list

# Appending elements to end of the list

cities.append('berlin')

print(cities)

# Inserting elements in the list

cities.insert(3, 'Bonn')

print(cities)

# Insert() operation shifts every element on the list one position to the right

# Removing Elements from the list del method

del cities[2]

print(cities)

# Removing elements from the list:- pop() method

# Benefit of using pop method is we can still access the removed elements

popped_cities = cities.pop()
first_city = cities.pop(0)
print(popped_cities)
print(first_city)
print(cities)

print(f"The first city that I visited Germany was {first_city.title()}")


# Removing an item by value (case sensitive) .remove method

cities.remove('Bonn')

print(cities)

too_far = 'dortmund'
cities.remove(too_far)

print(f"{too_far} is too far from where I live")

# Note remove() method only deletes the first occurrence from the list.
# In case of duplicate elements looping is required
