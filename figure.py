import math

class Figure:
    def __init__(self):
        self.__position = (0, 0)
        self.__rotation = 0

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, pos):
        assert isinstance(pos, (tuple, list)) and len(pos) == 2
        self.__position = pos

    @property
    def rotation(self):
        return self.__rotation

    @rotation.setter
    def rotation(self, rotation):
        assert isinstance(rotation, (float, int))
        self.__rotation = rotation

    def draw(self):
        pass

    def erase(self, bg_color="white"):
        old_color = self.color
        self.color = bg_color
        self.draw()
        self.color = old_color