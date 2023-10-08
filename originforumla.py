import math 
class Point:
    def __init__(self, x=0,y=0):
        self.x=x
        self.y=y
    def distance_to_origin(self):
        return math.sqrt(self.x**2+self.y**2)
    def reflect(self, axis):
        if axis=='x':
            self.x=-self.x
        elif axis=='y':
            self.y=-self.y
        else:
           print("Error: Invalid axis. Use 'x' or 'y'.")    
objpoint=Point(3,4) 
print("distance to origin", objpoint.distance_to_origin())   
objpoint.reflect('x')
print("reflect (x-axis):" ,objpoint.x,objpoint.y)     
objpoint.reflect('y')
print("reflect (y-axis):" ,objpoint.x,objpoint.y)