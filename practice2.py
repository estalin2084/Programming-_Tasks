class Rectangle:

   #Default constructor.

   def __init__(self,w=1,h=2):

       self.width = w;

       self.height = h;

   #getArea method.

   def getArea(self):

       return self.width*self.height

   #getperimeter method.

   def getPerimeter(self):

       return 2*(self.width+self.height)

w = 4

print ("The width of the rectangle is "+str(w))

h = 40

print ("The width of the rectangle is "+str(h))

#Call the method by passing the width and height.

r = Rectangle(w,h);

#Print the area and perimeter.

print('The area of the rectangle is', r.getArea())

print('The perimeter of the rectangle is', r.getPerimeter())

w = 3.5

print("The width of the rectangle is "+str(w))

h = 35.7

print("The width of the rectangle is "+str(h))

#Call the method by passing the width and height.

r = Rectangle(w,h);

#Print the area and perimeter.

print("The area of the rectangle is", (r.getArea()))

print("The perimeter of the rectangle is", (r.getPerimeter()))