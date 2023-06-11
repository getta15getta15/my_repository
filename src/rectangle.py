from figure import figure

class rectangle(figure):

    def __init__(self, name, side_a, side_b):
        figure.__init__(self, name)
        try:
            self.side_a = side_a
            self.side_b = side_b
            self.area = self.get_area()
            self.perimeter = self.get_perimeter()
        except:
            raise Exception("error create rectangle")
        
    def get_area(self):
        return self.side_a * self.side_b
   
    def get_perimeter(self):
        return self.side_a * 2 + self.side_b * 2
