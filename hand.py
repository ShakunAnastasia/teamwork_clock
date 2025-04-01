from figure import Figure
from turtle import *
import math

class Hand(Figure):
    def __init__(self, length, width=2):
        super().__init__()
        self._length = length
        self._width = width

    def calculate_position(self):
        x1, y1 = (0, 0)
        rad = math.radians(90 - self.rotation)
        x2 = x1 + self._length * math.cos(rad)
        y2 = y1 + self._length * math.sin(rad)
        return x2, y2

    def draw(self):
        original_width = pensize()
        pensize(self._width)

        color("dark slate gray")

        x2, y2 = self.calculate_position()

        up()
        setpos(0, 0)
        down()
        goto(x2, y2)

        rad = math.radians(90 - self.rotation)
        tip_length = self._length * 0.15
        base_width = self._width * 3

        base_left_rad = rad + math.pi / 4
        base_right_rad = rad - math.pi / 4
        base_left_x = x2 - tip_length * 0.5 * math.cos(rad) + base_width * math.cos(base_left_rad)
        base_left_y = y2 - tip_length * 0.5 * math.sin(rad) + base_width * math.sin(base_left_rad)
        base_right_x = x2 - tip_length * 0.5 * math.cos(rad) + base_width * math.cos(base_right_rad)
        base_right_y = y2 - tip_length * 0.5 * math.sin(rad) + base_width * math.sin(base_right_rad)

        tip_x = x2 + tip_length * 0.5 * math.cos(rad)
        tip_y = y2 + tip_length * 0.5 * math.sin(rad)


        up()
        goto(x2, y2)
        down()
        begin_fill()
        goto(base_left_x, base_left_y)
        goto(tip_x, tip_y)
        goto(base_right_x, base_right_y)
        goto(x2, y2)
        end_fill()

        up()
        setpos(0, 0)
        pensize(original_width)

class Second(Hand):
    def __init__(self):
        super().__init__(length=200, width=1)
        self.rotation = 0

class Minute(Hand):
    def __init__(self):
        super().__init__(length=140, width=3)

class Hour(Hand):
    def __init__(self):
        super().__init__(length=90, width=4)