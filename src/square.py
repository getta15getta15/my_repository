from figure import Figure

class Square(Figure):

    def __init__(self, name, side):
        Figure.__init__(self, name)
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
