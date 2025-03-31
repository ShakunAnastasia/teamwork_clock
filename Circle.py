from figure import Figure
from turtle import *

class Circle(Figure):
    def __init__(self, radius, extent):
        super().__init__()
        self.__extent = extent
        self.__radius = radius

    def draw(self):
        up()
        setpos(0, -275)
        down()
        circle(self.__radius, self.__extent)
        up()
