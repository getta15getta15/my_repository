from figure import Figure

class Triangle(Figure):

    def __init__(self, name, side_a, side_b, side_c):
        super().__init__(name)
        if not isinstance(side_a, int) or side_a <= 0:
            raise ValueError(f'Can not create triangle with side {side_a}')
        if not isinstance(side_b, int) or side_b <= 0:
            raise ValueError(f'Can not create triangle with side {side_b}')
        if not isinstance(side_c, int) or side_c <= 0:
            raise ValueError(f'Can not create triangle with side {side_c}')            
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.area = self.get_area()
        self.perimeter = self.get_perimeter()

    def get_area(self):
        pperimeter = (self.side_a + self.side_b + self.side_c) / 2
        return (pperimeter * (pperimeter - self.side_a) * (pperimeter - self.side_b) * (pperimeter - self.side_c))
        
    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c 
        
