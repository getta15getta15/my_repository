class Figure:
 
    def __init__(self, name):
        try:
            self.name = name
        except:
            raise Exception("error create main figure")

    def add_area(self, other):
        try:
            return self.area() + other.area()
        except:
            raise ValueError("error add area")
