from turtle import *
from Circle import Circle
from numbers import Numbers
from hand import Second, Minute, Hour
from datetime import datetime

def update_clock():
    now = datetime.now()
    second_hand.rotation = now.second * 6
    minute_hand.rotation = now.minute * 6 + now.second * 0.1
    hour_hand.rotation = (now.hour % 12) * 30 + now.minute * 0.5

    clear()
    circle.draw()
    second_hand.draw()
    minute_hand.draw()
    hour_hand.draw()

    update()
    ontimer(update_clock, 1000)

def main():
    global circle, second_hand, minute_hand, hour_hand

    reset()
    speed(0)
    tracer(0, 0)
    hideturtle()

    circle = Circle(275, 360)
    second_hand = Second()
    minute_hand = Minute()
    hour_hand = Hour()

    update_clock()
    mainloop()

if __name__ == '__main__':
    main()