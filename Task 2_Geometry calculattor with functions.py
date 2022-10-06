# Name: Geometry Calculator with Functions.py
# Author: Estalin Peña
# Date Created: october 04, 2022
# Date Last Modified: october 04, 2022
# Purpose: To Calculate specified geometric figures

#First I need to print the name of the program, then create the menu of the geometric figures. After that create a variable that takes 
# the choices of the user. Then I need to create one function to evaluate the area and perimeter of every given geometric figure and ask te user for 
# the data of each figure to be calculated.
# Lastly, when the user enters the data for any given figure, the answer would trim the spaces of each response.
#If the user chooses something different from the menu, we will wish them to have a good day.


from math import pi #This will allow to use pi into the calculation

print("Geometry Calculator") #This will print the Title of the program.

print("")   
print("1 - Square")    #This will prompt the options to the user.
print("2 - Rectangle")
print("3 - Circle")
print("4 - Quit")
print("")
answer = input("Enter your choice: ") #This input will allow the user to choose between the options


def calc_square(side_a): #This function calculates the perimeter and the area of the square.
    perimeter_square= (side_a * 4)
    square_area=(side_a * side_a)
    print("The perimeter of your square is" ,perimeter_square , " cm2")
    print ("The area of your square is", square_area, " cm2")

def calc_rectangle(length_Rectangle, height_Rectangle): #This functionn calculates the area and perimeter of a Rectangle.
    area_Rectangle = length_Rectangle * height_Rectangle
    perimeter_Rectangle = 2*(length_Rectangle + height_Rectangle)
    print("The area of your rectangle is" , area_Rectangle, " cm2" )
    print("The perimeter of your rectangle is" , perimeter_Rectangle, " cm")

def calc_circle(radius): #This function calculates the radius of a circle.
    area_Circle = pi* radius*radius
    perimeter_Circle = 2*pi*radius
    print("The area of your circle is " , area_Circle , " cm2")
    print("The Perimeter of your circle is " , perimeter_Circle , " cm")

if answer.strip() == "1": #This if takes the input of the user when selecting number 1, and trim the spaces.
    lenght_Rectangle = float(input("Please type the lenght of your rectangle in centimeters: "))
    height_Rectangle = float(input("Please type the height of your rectangle in centimeters: "))
    calc_rectangle(lenght_Rectangle, height_Rectangle)
    

elif answer.strip() == "2": #This elif takes the input of the user when selecting number 2, and trim the spaces.
    side_a= float(input("Please type the side A of your square in centimeters: "))
    side_b= float(input("Please type the side B of your square in centimeters: "))
    calc_square(side_a, side_b)

elif answer.strip() == "3": #This elif takes the input of the user when selectecting number 3, and trim the spaces.
    radius = float(input("Please type the radius of your circle in centimeters: "))
    calc_circle(radius)    

elif answer.strip() == "4":#This option makes the user quit all the options above.
    print("Quit")
    
else: #In case the user types any other thing, we wish they a nice day.
    print("Have a nice day! ") 