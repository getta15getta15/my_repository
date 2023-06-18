from figure import Figure

class Rectangle(Figure):

    def __init__(self, name, side_a, side_b):
        super().__init__(name)
        if not isinstance(side_a, int) or side_a <= 0:
            raise ValueError(f'Can not create rectangle with side {side_a}')
        if not isinstance(side_b, int) or side_b <= 0:
            raise ValueError(f'Can not create rectangle with side {side_b}')
        self.side_a = side_a
        self.side_b = side_b
        self.area = self.get_area()
        self.perimeter = self.get_perimeter()
        
    def get_area(self):
        return self.side_a * self.side_b
   
    def get_perimeter(self):
        return self.side_a * 2 + self.side_b * 2
