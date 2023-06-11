import pytest
import sys
sys.path.append('C:\\eclipse\\repository\\my_repository\\src')

import circle
import rectangle
import square
import triangle

def test_circle():
    my_circle = circle.circle("my_circle", 10)
    if my_circle.radius != 10:
        assert False
    elif my_circle.area != my_circle.get_area():
        assert False
    elif my_circle.perimeter != my_circle.get_perimeter():
        assert False
    else:
        assert True
        
def test_rectangle():
    my_rectangle = rectangle.rectangle("my_rectangle", 10, 20)
    
def test_square():
    my_square = square.square("my_square", 10)

def test_triangle():
    my_triangle = triangle.triangle("my_triangle", 10, 20, 30)            
    

