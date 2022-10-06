# Name: Hello World.py
# Author: Estalin Peña
# Date Created: october 03, 2022
# Date Last Modified: october 03, 2022
# Purpose: To check the lenght and format of the Username variable.




run = True #While this it's true the program will keep asking the user to enter its username, and will trim the spaces.
while run == True: 
    username = input("Please enter your name: ")
    username= username.strip()

    upper = False #When this variables are false they will keep looping until there's a capital letter and a number in the username.
    number =  False
    for aLetter in username:
        if aLetter.isupper():
            upper= True
        elif aLetter.isnumeric():
            number= True

    if len(username) <2: #when the username is less than one, or does not have any character at all, the message will prompt.
        print("Sorry, username must be longer than one letter.")
        

    elif len(username) >20: #When the username is longer than 20 characters, the message bellow will prompt.
        print("Sorry, username cannot be more than 20 letters in length.")

    
    elif upper == False or number == False: #This evaluates either if the username has a number or a capitar letter in it.
        print("Sorry, your username must have at least one uppercase letter and at least one number")

   
    else: #When all the conditions are met the username is created.
        print ("Congratulations your username", username,"has been created")
        run = False 
        
     

    

