from turtle import *
from figure import Figure
import math

class Hand(Figure):
    def __init__(self, length):
        super().__init__()
        self._length = length

    def calculate_position_2(self):
        x1, y1 = self.position
        rad = math.radians(self.rotation)
        x2 = x1 + self._length * math.cos(rad)
        y2 = y1 + self._length * math.sin(rad)
        return x2, y2

    def draw(self):
        setpos(self.position)
        down()
        goto(self.calculate_position_2())
        up()
        setpos(self.position)


class Second(Hand):
    def __init__(self):
        super().__init__(225)
        self.rotation = 0

class Minute(Hand):
    def __init__(self):
        super().__init__(175)
        self.rotation = 0

class Hour(Hand):
    def __init__(self):
        super().__init__(125)
        self.rotation = 0