text = "123"
result = text.isdecimal()            # returns False

print("First call to isdecimal():", result)

if text.count(".") == 1:
    
    # the following code does method stacking, by calling both replace() and isdecimal() in one line
    result = text.replace(".","").isdecimal()

    #text = text.replace(".","")
    #result = text.isdecimal()

print("Second call to isdecimal():", result)