fruit = ["orange", "mango", "kiwi", "pineapple", "banana"]

for aFruit in fruit:
    print("- {}".format(aFruit.capitalize()))

favouriteFruit = input("\nWhat is your favourite fruit (see the list above)? ").strip().lower()

# a simple way to check if user's value is one of the valid values (the values in the List)
while favouriteFruit not in fruit:
    favouriteFruit = input("\nPlease choose from the list of fruit above... What is your favourite fruit? ").strip().lower()
    
print("Thank you!")