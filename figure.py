import math

class Figure:
    def __init__(self):
        self.__rotation = 0

    @property
    def rotation(self):
        return self.__rotation

    @rotation.setter
    def rotation(self, rotation):
        assert isinstance(rotation, (float, int))
        self.__rotation = rotation

    def draw(self):
        pass

from figure import Figure
from turtle import *
import math
