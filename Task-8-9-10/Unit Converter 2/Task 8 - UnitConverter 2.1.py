#Name: Unit Converter.py
# Author: Estalin Peña
# Date Created: october 24, 2022
# Date Last Modified: october 24, 2022
# Purpose: Convert Temperature (Celsius and Fahrenheit) and speed (KMH/MPH)

#Fuction name: temp_convert
#Description: Will Output the conversion of the temperature selected by the user
#Parameters: 
#            Val: Numeric value of the temperature
#            Unit: The kind of temperature the user wants to convert
#Return value:The conversion of the temperature selected by the user


def unit_measurement(val, unit):
    pnd_to_kg = (val * 0.451)
    kg_to_pnd = (val /0.451)/
    if unit.upper() =="P":
        print('{:.2f} {}'.format(pnd_to_kg, "Pounds".strip()))
    if unit.upper() =="KG":
        print('{:.2f} {}'.format(kg_to_pnd, "Kilograms".strip()))

#Fuction name: speed_convert
#Description: Will Output the conversion of the speed selected by the user
#Parameters: 
#            Val: Numeric value of the speed
#            Unit: The kind of speed the user wants to convert
#Return value:The conversion of the speed selected by the user
def distance_measurement(val, unit):
    meters_to_feet= (val *  3.281)
    feet_to_meters = (val /3.281)
    if unit.upper() == "M":
        print('{:.2f} {}'.format(meters_to_feet, "Meters".strip()))
    if unit.upper() == "F":
        print('{:.2f} {}'.format(feet_to_meters, "Feet".strip()))



print(" ")#spaces between the information
print("\t","\t", "\t",  "Welcome to the Unit Converter")#Displays the welcome message
print(" ")#spaces between the information

unit_selector = input("Please select the unit you wish to convert: 1) Measurement 2) Distance: ")#Takes the type of unit the user wishes to convert
while unit_selector != "1" and unit_selector != "2":
    print("Your input is incorrect")
    unit_selector = input("Please select the unit you wish to convert: 1) Measurement 2) Distance: ")
    



print(" - " *40)#separates the data printed with dashes

if unit_selector == "1": #This evaluates the user selection  for Temperature
    val = float(input("Please enter the temperature: "))#This takes the numeric value of the temperature
    unit = input("'C' Celcius or 'F' Farenheit: ")#The user selects Celsius of Fahrenheit
    temp_convert(val, unit)#This returns the values from the fuction tempt converter and  applies the formula
elif unit_selector == "2": #This evaluates the user selection for speed.
    val = float(input("Please enter the speed: ")) #This input takes the numeric value of the speed
    unit = input("KMH or MPH: ") #this takes the kind of distance 
    speed_convert(val, unit)#This returns the values from the fuction speed converter and  applies the formula


print(" - " *40)#separates the data printed with dashes

goodBye = input("Do you wish to continue? [Yes/No]: ".strip())#This variable asks the user if wants to continue in the process 
print(" - " *40)#separates the data printed with dashes
while goodBye == True: #This while evaluates either if the user wants to continue or not converting speed or temperatures.
    if goodBye.upper() == "Yes" or goodBye.upper() == "Y":
        goodBye = True
    elif goodBye.upper() == "No" or goodBye.upper() == "N":
        goodBye == False
        break
else: #If no is selected then we wish the user a great day!
    print("Have a great day!".strip())