# Name: Hello World.py
# Author: Estalin Peña
# Date Created: october 03, 2022
# Date Last Modified: october 03, 2022
# Purpose: To Calculate specified geometric figures


from math import pi 

print("Geometry Calculator")

print("")
print("1 - Square")
print("2 - Rectangle")
print("3 - Circle")
print("4. Quit")
print("")
answer = input("Enter your choice: ")

def calc_circle(radius):
    area_Circle = pi* radius*radius
    perimeter_Circle = 2*pi*radius
    print("The area of your circle is " , area_Circle , " cm2")
    print("The Perimeter of your circle is " , perimeter_Circle , " cm2")

def calc_square(side_a, side_b, side_c, side_d):
    perimeter_square= (side_a + side_b + side_c + side_d)
    square_area=(side_a * side_b)
    print("The perimeter of your square is" ,perimeter_square , " cm2")

def calc_rectangle(length, height):
    area_Rectangle = lenght_Rentangle * height_Rectangle
    perimeter_Rectangle = 2*(lenght_Rentangle + height_Rectangle)
    print("The area of your rectangle is" , lenght_Rentangle , height_Rectangle, " cm2" )
    print("The perimeter of your rectangle is" , perimeter_Rectangle, " cm2")


if answer.strip() == "3":
    radius = float(input("Please type the radius of your circle in centimeters: "))
    calc_circle(radius)

elif answer.strip() == "2":
    lenght_Rentangle = float(input("Please type the lenght of your rectangle in centimeters: "))
    height_Rectangle = float(input("Please type the height of your rectangle in centimeters: "))
    calc_rectangle(lenght_Rentangle, height_Rectangle)
    

elif answer.strip() == "1":
    side_a= float(input("Please type the side A of your square in centimeters: "))
    side_b= float(input("Please type the side B of your square in centimeters: "))
    side_c= float(input("Please type the side C of your square in centimeters: "))
    side_d= float(input("Please type the side D of your square in centimeters: "))
    calc_square(side_a, side_b, side_c, side_d)
    
    

else:
    print("have a nice day") 