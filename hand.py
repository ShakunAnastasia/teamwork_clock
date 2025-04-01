from figure import Figure
from turtle import *
import math

class Hand(Figure):
    def __init__(self, length):
        super().__init__()
        self._length = length

    def calculate_position(self):
        x1, y1 = (0, 0)
        rad = math.radians(90 - self.rotation)
        x2 = x1 + self._length * math.cos(rad)
        y2 = y1 + self._length * math.sin(rad)
        return x2, y2

    def draw(self):
        up()
        setpos(0, 0)
        down()
        goto(self.calculate_position())
        up()
        setpos(0, 0)

class Second(Hand):
    def __init__(self):
        super().__init__(200)
        self.rotation = 0

class Minute(Hand):
    def __init__(self):
        super().__init__(140)

class Hour(Hand):
    def __init__(self):
        super().__init__(90)