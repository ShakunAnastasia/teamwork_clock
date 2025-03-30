from turtle import *
from figure import Figure
import math

class Hand(Figure):
    def __init__(self, length, Second, Minute, Hour):
        super().__init__()
        self._length = length
        self._Second = Second
        self._Minute = Minute
        self._Hour = Hour

    def calculate_position_2(self, __position, _length):
        x1, y1 = self.__position
        x2, y2 = (x1 + self._length * math.cos(90-self.rotation), y1 + self._length * math.sin(90-self.rotation))
        position_2 = x2, y2
        return position_2

    def draw(self):
        setpos(self.__position)
        down()
        goto(self.calculate_position_2(self.__position, self._length))
        up()
        setpos(self.__position)


class Second(Hand):
    def __init__(self):
        super().__init__()
        self.__rotation = 0.1
        self._length = 200

class Minute(Hand):
    def __init__(self):
        super().__init__()
        self.__rotation = 6
        self._length = 200

class Hour(Hand):
    def __init__(self):
        super().__init__()
        self.__rotation = 30
        self._length = 200













