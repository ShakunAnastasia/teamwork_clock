from figure import Figure
from turtle import *

class Circle(Figure):
    def __init__(self, radius):
        super().__init__()
        self.__radius = radius

    def draw(self):
        up()
        pencolor(self.color)
        setpos(self._calc_position((0, -self.__radius)))
        down()
        circle(self.__radius)
        up()
