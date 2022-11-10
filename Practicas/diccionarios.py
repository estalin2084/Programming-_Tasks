

guess_me = 7

for number in range(20):
    if number > guess_me:
        print("{} Oops".format(number))
    elif number == guess_me:
        print("{} Too low".format(number))
    else:
        print("{} is middle aged".format(number))

#Assign the value 7 to the variable guess_me. Use a for loop to iterate a variable called number over range(20). 
# If number is less than guess_me, print 'too low'.
#  If it equals guess_me, print found it! and then break out of the for loop. 
# If number is greater than guess_me, print 'oops' and then exit the loop.
