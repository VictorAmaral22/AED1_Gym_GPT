import graphics as gf
import random

winW = 1000
winH = 800

win = gf.GraphWin("Colisão", winW, winH)

button = gf.Rectangle(gf.Point(0, 0), gf.Point(100, 100))
button.draw(win)

win.getMouse()