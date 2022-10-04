
run = True 
while run != False:
    username = input("Please enter: your name ")
    s = ''.join(ch for ch in username if ch.isupper())
    n= " ".join(ch for ch in username if ch.isnumeric()) 







    if len(username) ==1:
        print("Sorry, username must be longer than one letter.")
        

    elif len(username) >20:
        print("Sorry, username cannot be more than 20 letters in length.")

    elif len(s)==0:
        print("Hola")

    elif len(n)==0:
        print("Sorry, username should have at leas")

    else:
        print ("finish")
        run = False 
        
     

    

