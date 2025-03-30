from figure import Figure
from turtle import *

class Circle(Figure):
    def __init__(self, radius):
        super().__init__()
        self.__radius = radius

    def draw(self):
        up()
        setpos(0, -250)
        down()
        circle(self.__radius)
        up()
