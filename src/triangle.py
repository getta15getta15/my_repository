from figure import figure

class triangle(figure):

    def __init__(self, name, side_a, side_b, side_c):
        figure.__init__(self, name)
        try:
            self.side_a = side_a
            self.side_b = side_b
            self.side_c = side_c
            self.area = self.get_area()
            self.perimeter = self.get_perimeter()
        except:
            raise Exception("error create triangle")

    def get_area(self):
        pperimeter = (self.side_a + self.side_b + self.side_c) / 2
        return (pperimeter * (pperimeter - self.side_a) * (pperimeter - self.side_b) * (pperimeter - self.side_c))
        
    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c 
        