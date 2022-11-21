fruit = ["orange", "mango", "kiwi", "pineapple", "banana"]

for aFruit in fruit:
    print("- {}".format(aFruit.capitalize()))

favouriteFruit = input("\nWhat is your favourite fruit (see the list above)? ").strip().lower()

# without a List, we need to include all valid values in the condition, to check if user's value 
# is one of them (ie. valid). In a different scenario, there could be many more valid values...
while favouriteFruit != "orange" and favouriteFruit != "mango" and favouriteFruit != "kiwi" \
    and favouriteFruit != "pineapple" and favouriteFruit != "banana":

    favouriteFruit = input("\nPlease choose from the list of fruit above... What is your favourite fruit? ").strip().lower()
    
print("Thank you!")