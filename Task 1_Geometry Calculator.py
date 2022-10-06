# Name: Hello World.py
# Author: Estalin Peña
# Date Created: october 03, 2022
# Date Last Modified: october 03, 2022
# Purpose: To Calculate specified geometric figures


from math import pi #This will allow to use pi into the calculation

print("Geometry Calculator") #This will print the Title of the program.

print("") #This will prompt the options to the user.
print("1. Calculate the area of a Circle")
print("2. Calculate the area of a Rectangle")
print("3. Calculare the area of a Triangle")
print("4. Quit")
print("")
answer = input("Enter your choice: ")

if answer.strip() == "1": #This code calculates and print the area and perimeter of a Circle, and trim the spaces.
    radius = float(input("Please type the radius of your circle in centimeters: "))
    area_Circle = pi* radius*radius
    perimeter_Circle = 2*pi*radius
    print("The area of your circle is " , area_Circle , " cm2")
    print("The Perimeter of your circle is " , perimeter_Circle , " cm")

elif answer.strip() == "2": #This code calculates and print the area and perimeter of a Rectangle, and trim the spaces.
    lenght_Rectangle = float(input("Please type the lenght of your rectangle in centimeters: "))
    height_Rectangle = float(input("Please type the height of your rectangle in centimeters: "))
    area_Rectangle = lenght_Rectangle * height_Rectangle
    perimeter_Rectangle = 2*(lenght_Rectangle + height_Rectangle)
    print("The area of your rectangle is" , lenght_Rectangle , height_Rectangle, " cm2" )
    print("The perimeter of your rectangle is" , perimeter_Rectangle, " cm")

elif answer.strip() == "3": #This code calculates and print the area and perimeter of a Triangle, and trim the spaces.
    height_Triangle= float(input("Please type the height of your triangle in centimeters: "))
    side_a= float(input("Please type the side A of your triangle in centimeters: "))
    side_b= float(input("Please type the side B of your triangle in centimeters: "))
    base_triangle= float(input("Please type the base of your triangle in centimeters: "))
    perimeter_Triangle= (side_a + side_b + base_triangle)
    area_Triangle = base_triangle * height_Triangle /2 
    print("The area of your triangle is" ,area_Triangle , " cm2")
    print("the perimeter of your triangle is", perimeter_Triangle, " cm")

elif answer.strip()== "4": #This option makes the user quit all the options above.
    print("Quit")

else: #In case the user types any other thing, we wish they a nice day.
    print("Have a nice day! ") 
