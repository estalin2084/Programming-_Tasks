fruit = ["apple", "banana", "cherry", "apple", "kiwi", "watermelon", "grape", "strawberry", "grape"]

fruit.remove("grape")   # note: only the first occurrence of the value "grape" is removed
fruit.pop(4)		    # Removes 5th item ("kiwi")
fruit.pop()		        # Without an index specified, pop() removes the last element ("grape")
del fruit[3]		    # Removes 4th item, 'apple' positioned at index 3
del fruit[0:2]	        # Removes a range of elements: 1st and 2nd element ("apple" and "banana")

print(fruit)            # Output:   ['cherry', 'watermelon', 'strawberry']

fruit.clear()           # Removes all the remaining items from the list. 
print(fruit)            # Output:   []

del fruit               # Removes the list object itself
print(fruit)            # Output:   NameError: name 'fruit' is not defined