import pytest
import sys
sys.path.append('C:\\eclipse\\repository\\my_repository\\src')

from circle import Circle
from rectangle import Rectangle
from square import Square
from triangle import Triangle

@pytest.mark.parametrize('circle_radius, circle_area, circle_perimeter', [(10, 314, 62.80)])

def test_circle(circle_radius, circle_area, circle_perimeter):
    my_circle = Circle("my_circle", circle_radius)
    assert my_circle.radius == circle_radius
    assert my_circle.area == circle_area
    assert round(my_circle.perimeter, 2) == circle_perimeter

@pytest.mark.parametrize('rectangle_side_a, rectangle_side_b, rectangle_area, rectangle_perimeter', [(10, 20, 200, 60)])
        
def test_rectangle(rectangle_side_a, rectangle_side_b, rectangle_area, rectangle_perimeter):
    my_rectangle = Rectangle("my_rectangle", rectangle_side_a, rectangle_side_b)
    assert my_rectangle.get_area() == rectangle_area
    assert my_rectangle.get_perimeter() == rectangle_perimeter
    
@pytest.mark.parametrize('square_side, square_area, square_perimeter', [(10, 100, 40)])

def test_square(square_side, square_area, square_perimeter):
    my_square = Square("my_square", 10)
    assert my_square.get_area() == square_area
    assert my_square.get_perimeter() == square_perimeter

@pytest.mark.parametrize('triangle_side_a, triangle_side_b, triangle_side_c, triangle_area, triangle_perimeter', [(1, 2, 2.23, 1, 5.23)])

def test_triangle(triangle_side_a, triangle_side_b, triangle_side_c, triangle_area, triangle_perimeter):
    my_triangle = Triangle("my_triangle", triangle_side_a, triangle_side_b, triangle_side_c)            
    assert round(my_triangle.get_area(), 2) == triangle_area
    assert round(my_triangle.get_perimeter(), 2) == triangle_perimeter

@pytest.mark.parametrize('circle_radius, circle_area', [(10, 314)])
@pytest.mark.parametrize('rectangle_side_a, rectangle_side_b, rectangle_area', [(10, 20, 200)])
@pytest.mark.parametrize('square_side, square_area', [(10, 100)])
@pytest.mark.parametrize('triangle_side_a, triangle_side_b, triangle_side_c, triangle_area', [(1, 2, 2.23, 1)])
    
def test_add_area( circle_radius, circle_area
                 , rectangle_side_a, rectangle_side_b, rectangle_area
                 , square_side, square_area
                 , triangle_side_a, triangle_side_b, triangle_side_c, triangle_area):
    my_circle = Circle("my_circle", circle_radius)
    my_rectangle = Rectangle("my_rectangle", rectangle_side_a, rectangle_side_b)
    my_square = Square("my_square", 10)
    my_triangle = Triangle("my_triangle", triangle_side_a, triangle_side_b, triangle_side_c)
    assert round(my_circle.add_area(my_rectangle)) == (circle_area + rectangle_area)  
    assert round(my_circle.add_area(my_square)) == (circle_area + square_area)  
    assert round(my_circle.add_area(my_triangle)) == (circle_area + triangle_area)  
    
