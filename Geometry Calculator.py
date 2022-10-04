# Name: Hello World.py
# Author: Estalin Peña
# Date Created: october 03, 2022
# Date Last Modified: october 03, 2022
# Purpose: To Calculate specified geometric figures


from math import pi 

print("Geometry Calculator")

print("")
print("1. Calculate the area of a Circle")
print("2. Calculate the area of a Rectangle")
print("3. Calculare the area of a Triangle")
print("4. Quit")
print("")
answer = input("Enter your choice: ")

if answer.strip() == "1":
    radius = float(input("Please type the radius of your circle in centimeters: "))
    area_Circle = pi* radius*radius
    perimeter_Circle = 2*pi*radius
    print("The area of your circle is " , area_Circle , " cm2")
    print("The Perimeter of your circle is " , perimeter_Circle , " cm2")

elif answer.strip() == "2":
    lenght_Rentangle = float(input("Please type the lenght of your rectangle in centimeters: "))
    height_Rectangle = float(input("Please type the height of your rectangle in centimeters: "))
    area_Rectangle = lenght_Rentangle * height_Rectangle
    perimeter_Rectangle = 2*(lenght_Rentangle + height_Rectangle)
    print("The area of your rectangle is" , lenght_Rentangle , height_Rectangle, " cm2" )
    print("The perimeter of your rectangle is" , perimeter_Rectangle, " cm2")

elif answer.strip() == "3":
    height_Triangle= float(input("Please type the height of your triangle in centimeters: "))
    side_a= float(input("Please type the side A of your triangle in centimeters: "))
    side_b= float(input("Please type the side B of your triangle in centimeters: "))
    base_triangle= float(input("Please type the base of your triangle in centimeters: "))
    perimeter_Triangle= (side_a + side_b + base_triangle)
    area_Triangle = base_triangle * height_Triangle /2 
    print("The area of your triangle is" ,area_Triangle , " cm2")
    print("the perimeter of your triangle is", perimeter_Triangle, " cm2")

else:
    print("have a nice day") 
