from math import pi
from abc import abstractmethod, ABC



class shapes(ABC):
    def __init__(self, side_lenght = float, high_lenght = float, radius = float):
        """

        :param side_lenght: the lenght of random side
        :param high_lenght: the lenght of high drawn to this side
        """
        self.side_lenght = side_lenght
        self.high_lenght = high_lenght
        self.radius = radius
    @abstractmethod

    def calculate_square_rectangle(self):
        """
        calculate the square
        :return: float
        """
        pass
    def calculate_square_circle(self):
        """
        calculate the square
        :return: float
        """
        pass
    def calculate_perimeter_rectangle(self):
        """
        calculate the perimeter
        :return: float
        """
        pass
    def calculate_perimeter_circle(self):
        """
        calculate the perimeter
        :return: float
        """
        pass

class Circle(shapes):
    number_of_sides = 0
    def calculate_square_circle(self):
        return pi*self.radius*self.radius

    def calculate_perimeter_circle(self):
        return 2*pi*self.radius


class Rectangle(shapes,ABC):
    def __init__(self, side_lenght = float, high_lenght = float):
        """

        :param side_lenght: The side lenght
        :param high_lenght: The high lenght
        """
        super().__init__(side_lenght, high_lenght)
class Parallelogram(Rectangle):
    angle_value = 30
    def calculate_square_rectangle(self):
        return self.side_lenght * self.high_lenght

    def calculate_perimeter_rectangle(self):
        return (self.side_lenght+2*self.high_lenght)*2

shape_list = []
circle = Circle(0,0,30)
shape_list.append(circle)
parallelogram = Parallelogram(20,15)
shape_list.append(parallelogram)