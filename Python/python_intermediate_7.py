##Write a program that draws a recursive image.
##For example, a Sierpinski triangle, a Barnsley fern, or a Mandelbrot set fractal would be good drawings.
##Any recursive image will do, but try to make them look fun or interesting.
##Bonus points for adding a color scheme!
##Please post a link to a sample image produced by your program, and above all, be creative.

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
