fruit = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]

fruit[1] = "blackcurrant"                       # Changes "banana" to "blackcurrant"
fruit[1:3] = ["blackcurrant", "watermelon"]     # Using a range in the index – 1 included, 3 is not; 
                                                # Changes "banana" (at index 1) to "blackcurrant", 
                                                # and "cherry" (at index 2) to "watermelon"

print(fruit)