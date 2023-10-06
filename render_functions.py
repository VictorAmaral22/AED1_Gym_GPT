from graphics import *

def renderButton (win, posW, posH, title, bgColor="#001d3d", txtColor="#fff", outline=False):
    buttonW = 150
    buttonH = 40
    button = Rectangle(Point(posW-buttonW, posH-buttonH), Point(posW+buttonW, posH+buttonH))
    button.setFill(bgColor)
    
    if outline:
        button.setOutline(outline)

    button.draw(win)
    buttonTitle = Text(button.getCenter(), title)
    buttonTitle.setStyle("bold")
    buttonTitle.setFill(txtColor)
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

def renderInput (win, posW, posH, inputW=20, fontSize=20, label="Insira um texto", inputFill="#fff", txtColor="#fff"):
    input = Entry(Point(posW, posH), inputW)
    input.draw(win)
    input.setFill(inputFill)
    input.setSize(fontSize)
    txt = Text(Point(posW, posH-30), label)
    txt.setFill(txtColor)
    txt.draw(win)

    corners = []

    def undraw ():
        input.undraw()
        txt.undraw()

    def draw ():
        input.draw(win)
        txt.draw(win)

    return [
        input,
        corners,
        undraw,
        draw,
    ]

def checkClick(posClick, bbox):
    if posClick.x >= bbox[0].x and posClick.x <= bbox[1].x and posClick.y >= bbox[0].y and posClick.y <= bbox[1].y:
        return True
    else:
        return False

def renderImage (win, posW, posH, imagePath):
    image = Image(Point(posW, posH), imagePath)

    imgWidth = image.getWidth()
    imgHeight = image.getWidth()
    imgAnchor = image.getAnchor()
    
    image.draw(win)

    corners = [
        Point(imgAnchor.x - imgWidth/2, imgAnchor.y - imgHeight/2),
        Point(imgAnchor.x + imgWidth/2, imgAnchor.y + imgHeight/2)
    ]

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