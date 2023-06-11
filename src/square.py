import math
from figure import figure

class square(figure):

    def __init__(self, name, side):
        figure.__init__(self, name)
        try:
            self.side = side
            self.area = self.get_area()
            self.perimeter = self.get_perimeter()
        except:
            raise Exception("error create square")

    def get_area(self):
        return self.side ** 2
    
    def get_perimeter(self):
        return self.side * 4      
