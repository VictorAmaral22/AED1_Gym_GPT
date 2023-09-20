import graphics as gf

winW = 1000
winH = 800

win = gf.GraphWin("Gym Rats", winW, winH)
win.setBackground("#111D13")

def renderButton (win, posW, posH, title):
    buttonW = 150
    buttonH = 40
    button = gf.Rectangle(gf.Point(posW-buttonW, posH-buttonH), gf.Point(posW+buttonW, posH+buttonH))
    button.draw(win)
    button.setFill("#A1CCA5")
    buttonTitle = gf.Text(button.getCenter(), title)
    buttonTitle.draw(win)

    p1 = button.getP1()
    p2 = button.getP2()

    print(p1)
    print(p2)

    corners = [p1, p2]
    return corners

def checkClick(posClick, bbox):
    if posClick.x >= bbox[0].x and posClick.x <= bbox[1].x and posClick.y >= bbox[0].y and posClick.y <= bbox[1].y:
        return True
    else:
        return False

bbxLoginPersonal = renderButton(win, winW/2, winH/2-100, "Login Personal")
bbxLoginCliente = renderButton(win, winW/2, winH/2, "Login Cliente")
bbxSair = renderButton(win, winW/2, winH/2+100, "Sair")

exit = False

while not exit:
    mousePos = win.getMouse()
    exit = checkClick(mousePos, bbxSair)
    
    loginPersonal = checkClick(mousePos, bbxLoginPersonal)
    loginCliente = checkClick(mousePos, bbxLoginCliente)
    