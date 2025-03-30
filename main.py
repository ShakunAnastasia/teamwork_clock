from turtle import *
from Circle import Circle
from hand import Hand
from hand import Second
from hand import Minute
from hand import Hour

def main():
    reset()
    speed(0)
    circle = Circle(250)
    hand = Hand(Second())
    hand.draw()
    circle.draw()
    mainloop()

if __name__ == '__main__':
    main()