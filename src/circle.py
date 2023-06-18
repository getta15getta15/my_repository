from figure import Figure

class Circle(Figure):

    def __init__(self, name, radius):
        super().init(self, name)
        if not isinstance(radius, int) or radius <= 0:
            raise ValueError(f'Can not create circle with radius {radius}')
            self.radius = radius
            self.area = self.get_area()
            self.perimeter = self.get_perimeter()
        
    def get_area(self):
        return 3.14 * self.radius ** 2
    
    def get_perimeter(self):
        return 2 * 3.14 * self.radius

