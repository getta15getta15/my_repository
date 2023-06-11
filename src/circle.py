import math
from figure import figure

class circle(figure):

    def __init__(self, name, radius):
        figure.__init__(self, name)
        try:
            self.radius = radius
            self.area = self.get_area()
            self.perimeter = self.get_perimeter()
        except:
            raise Exception("error create circle")
        
    def get_area(self):
        return 3.14 * self.radius ** 2
    
    def get_perimeter(self):
        return 2 * 3.14 * self.radius
