from turtle import *
from Circle import Circle
from hand import Hand

def main():
    reset()
    speed(0)
    circle = Circle(250)
    hand = Hand()
    circle.draw()
    mainloop()

if __name__ == '__main__':
    main()