# Author: Estallin Pena
# Date Created: 11-14-2022
# Last Modified: 11-14-2022
# Purpose: The program takes the input of 5 restaurants and their rate.





#fuction restaurans_ratings():
    #take 2 inputs, the name of the restarutans and the rating given by the user
    # and evaluates if the rating is greater than 0 and less or equal to 5
    # returns the value of the data stord in the dictionary user_ratings


def restaurants_ratings():

    user_ratings = {}

    i = 1
    while i <= 5:
        print("\nRestaurant #", i)

        name = input("Please enter the name of the restaurant: ")
        rating = int(input("Please enter the rating: "))

        while True:
            if not (rating > 0 and rating <= 5 ):
                rating = int(input("Please enter a valid number from 1 to 5: "))
            else:
                user_ratings[name] = rating
                break
        i +=1

    return user_ratings


#fuction allplaces_Ratings():
    #sorts the through the ratings of the restaurants and does the math to know wich is the minimum and the maximum value
    #stores 3 parameters:
        #allRatings:  the rating for the 5 restaurants
        #minRating:   stores the minimum rated restaurants
        #maxRaringL   stores the minimum rated restaurants
    
        # returns a dictionary with the info of the restaurants and the ratings

def allplacesRating(allRatings,minRating, maxRating):
    
    placesbyRating = {}

    for aRrestaurant, aRating in allRatings.items():
        if aRating >= minRating and aRating <= maxRating:
            placesbyRating[aRrestaurant] = aRating

    return placesbyRating

#fuction showRatings():
    #Shows the information of the excellent and bad places to eat
    #stores 2 parameters:
        #title:  Title to be shown
        #ratings:  The ratings to be shown
       
    
        # returns no value

def showRatings(title, ratings):

    print("\n{}".format(title))
    print("{:->40s}".format(''))

    for aplace, aRating in ratings.items():
        print("{0:35s}{1}".format(aplace, aRating * "*"))


user_ratings =  restaurants_ratings()                    # gets restaurant names and rating for each from user
excellentPlaces = allplacesRating(user_ratings, 3,5)     # calculates the excellent places to eat, with a min and max rating
notgoodPLaces = allplacesRating(user_ratings, 1,2)       # calculates  not good places to eat, based on a min and max rating


showRatings("Excellent places to go", excellentPlaces)    # shows to the user all the excellent places to go
print("-" * 40)
showRatings("Not good places to go", notgoodPLaces)       # shows to the user all the not good places to go



