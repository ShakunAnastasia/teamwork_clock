import math

class Figure:
    def __init__(self):
        self.__position = (0, 0)
        self.__rotation = 0
        self.__scale = (1, 1)
        self.__pivot = (0, 0)
        self.__color = "black"
        self.__visible = False

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

    @property
    def scale(self):
        return self.__scale

    @scale.setter
    def scale(self, scale):
        assert isinstance(scale, (tuple, list)) and len(scale) == 2
        self.__scale = scale

    @property
    def pivot(self):
        return self.__pivot

    @pivot.setter
    def pivot(self, pivot):
        assert isinstance(pivot, (tuple, list)) and len(pivot) == 2
        self.__pivot = pivot

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    def _calc_position(self, vertex):
        x, y = vertex
        x -= self.__pivot[0]
        y -= self.__pivot[1]
        x *= self.__scale[0]
        y *= self.__scale[1]
        cos_phi = math.cos(self.__rotation)
        sin_phi = math.sin(self.__rotation)
        x, y = cos_phi * x - sin_phi * y, sin_phi * x + cos_phi * y
        x += self.__position[0] + self.__pivot[0]
        y += self.__position[1] + self.__pivot[1]
        return x, y

    def draw(self):
        pass

    def erase(self, bg_color="white"):
        old_color = self.color
        self.color = bg_color
        self.draw()
        self.color = old_color