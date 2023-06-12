class Figure:
 
    def __init__(self, name):
        self.name = name

    def add_area(self, other):
        try:
            return self.area() + other.area()
        except:
            raise ValueError("error add area")
