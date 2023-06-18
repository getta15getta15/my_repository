from figure import Figure

class Square(Figure):

    def __init__(self, name, side):
        super().init(self, name)
        if not isinstance(side, int) or side > 0:
            raise ValueError(f'Can not create square with side {side}')
        self.side = side
        self.area = self.get_area()
        self.perimeter = self.get_perimeter()

    def get_area(self):
        return self.side ** 2
    
    def get_perimeter(self):
        return self.side * 4      
