from turtle import *

setup(800, 600)
reset()
pencolor('black')
speed(100)
pu()
pd()
setx(-50)
sety(-50)
getscreen()._root.attributes('-topmost', True)
getscreen()._root.attributes('-topmost', False)
colormode(255)

def superDiagonal(number, size):
    def square(length):
        for i in range(4):
            fd(length)
            lt(90)
    if number == 0:
        return
    else:
        fillcolor(int(size * 25 % 255), int(size * 25 % 255), int(size * 25 % 255))
        begin_fill()
        square(size)
        end_fill()
        for i in range(4):
            fd(size)
            rt(90)
            superDiagonal(number - 1, size / 2)
            rt(180)
        
superDiagonal(6, 100)
