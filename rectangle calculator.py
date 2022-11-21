class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def calculatePerimeter(self):
        return 2*(self.width + self.height)

    def calculateArea(self):
        return self.width * self.height
    
    def displayInfo(self):
        print("The lenght of the Rectangle is: ", self.calculatePerimeter()/2 - self.width, "centimeters")
        print("The width of the Rectangle is: ", self.width, "centimeters")
        print("The perimeter of the Rectangle is: ", self.calculatePerimeter(), "centimeters")
        print("The area of the Rectangle is: ", self.calculateArea(), "centimeters")

width = int(input("Please enter the width of the Rectangle in centimeters: "))
print("")
height = int(input("Please enter the height of the Rectangle in centimeters: "))
print("")

r = Rectangle(width, height)

r.displayInfo()





    

    
