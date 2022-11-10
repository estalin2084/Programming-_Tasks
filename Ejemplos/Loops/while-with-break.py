# break statement stops the loop even if the condition evaluateed to True
i = 1
while i < 6:
    	
    if i == 3:
        break       # Exits the loop once value in hits 3; Only numbers 1 and 2 will be printed out.

    print(i)        
    i += 1	        # increments the value in i by 1 every time the loop runs

print("Goodbye!")   # Executes after loop stops, right after break statement runs