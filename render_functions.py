from graphics import *

def renderButton (win, posW, posH, title):
    buttonW = 150
    buttonH = 40
    button = Rectangle(Point(posW-buttonW, posH-buttonH), Point(posW+buttonW, posH+buttonH))
    button.draw(win)
    button.setFill("#001d3d")
    buttonTitle = Text(button.getCenter(), title)
    buttonTitle.setFill("#fff")
    buttonTitle.draw(win)

    p1 = button.getP1()
    p2 = button.getP2()

    corners = [p1, p2]

    def undraw ():
        button.undraw()
        buttonTitle.undraw()

    def draw ():
        button.draw(win)
        buttonTitle.raw(win)

    return [
        button,
        buttonTitle,
        corners,
        undraw,
        draw
    ]

def renderInput (win, posW, posH, inputW=20, fontSize=20):
    input = Entry(Point(posW, posH), inputW)
    input.draw(win)
    input.setFill("#fff")
    input.setSize(fontSize)

    print(input.getAnchor())

    # inputLabel = Text(Point(input.getAnchor().x+20, input.getP1().y-20), label)
    # inputLabel.setFill("#fff")
    # inputLabel.draw(win)

    # p1 = input.getP1()
    # p2 = input.getP2()

    corners = []

    def undraw ():
        input.undraw()

    def draw ():
        input.draw(win)

    # def changeTxt (txt):
        # inputContent.setText(txt)

    return [
        input,
        corners,
        undraw,
        draw,
        # changeTxt
    ]

def checkClick(posClick, bbox):
    if posClick.x >= bbox[0].x and posClick.x <= bbox[1].x and posClick.y >= bbox[0].y and posClick.y <= bbox[1].y:
        return True
    else:
        return False

def renderImage (win, posW, posH, imagePath):
    image = Image(Point(posW, posH), imagePath)
    
    image.draw(win)

    corners = []

    def undraw ():
        image.undraw()

    def draw ():
        image.draw(win)

    return [
        image,
        corners,
        undraw,
        draw
    ]