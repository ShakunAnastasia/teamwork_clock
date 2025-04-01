from figure import Figure
from turtle import *
import math

class Circle(Figure):
    def __init__(self, radius, extent):
        super().__init__()
        self.__extent = extent
        self.__radius = radius

    def draw(self):
        fillcolor("tan")
        begin_fill()
        up()
        setpos(0, -self.__radius)
        down()
        circle(self.__radius, self.__extent)
        end_fill()
        up()

        color("dark slate gray")
        up()
        setpos(0, -self.__radius)
        down()
        circle(self.__radius, self.__extent)
        up()

        self.draw_numbers()
        self.draw_ticks()

    def draw_numbers(self):
        font_size = int(self.__radius * 0.07)
        for i in range(1, 13):
            angle = math.radians(90 - i * 30)
            x = self.__radius * 0.85 * math.cos(angle)
            y = self.__radius * 0.85 * math.sin(angle)
            up()
            setpos(x, y - font_size / 2)
            down()
            color("dark slate gray")
            write(str(i), align="center", font=("Arial Narrow", font_size, "normal"))

    def draw_ticks(self):
        for i in range(60):
            angle = math.radians(90 - i * 6)
            outer_x = self.__radius * math.cos(angle)
            outer_y = self.__radius * math.sin(angle)
            inner_x = outer_x * (0.9 if i % 5 == 0 else 0.95)
            inner_y = outer_y * (0.9 if i % 5 == 0 else 0.95)
            up()
            setpos(outer_x, outer_y)
            down()
            color("dark slate gray")
            goto(inner_x, inner_y)
            up()