from graphics import *

winW = 1000
winH = 800

win = GraphWin("Gym Rats", winW, winH)
win.setBackground("#000")

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

    # print(p1)
    # print(p2)

    corners = [p1, p2]

    def undraw ():
        button.undraw()
        buttonTitle.undraw()

    return [
        button,
        buttonTitle,
        corners,
        undraw
    ]

def renderInput (win, posW, posH, label):
    inputW = 150
    inputH = 30
    input = Rectangle(Point(posW-inputW, posH-inputH), Point(posW+inputW, posH+inputH))
    input.draw(win)
    input.setFill("#fff")
    inputContent = Text(input.getCenter(), "")
    inputContent.setFill("#000")
    inputContent.draw(win)

    inputLabel = Text(Point(input.getP1().x+20, input.getP1().y-20), label)
    inputLabel.setFill("#fff")
    inputLabel.draw(win)

    p1 = input.getP1()
    p2 = input.getP2()

    # print(p1)
    # print(p2)

    corners = [p1, p2]

    def undraw ():
        input.undraw()
        inputContent.undraw()

    def draw ():
        input.draw(win)
        inputContent.draw(win)

    def changeTxt (txt):
        inputContent.setText(txt)

    return [
        input,
        inputContent,
        corners,
        undraw,
        draw,
        changeTxt
    ]

def checkClick(posClick, bbox):
    if posClick.x >= bbox[0].x and posClick.x <= bbox[1].x and posClick.y >= bbox[0].y and posClick.y <= bbox[1].y:
        return True
    else:
        return False

def handleTyping (keyPressed, text):
    if keyPressed == "space":
        text += " "
    if keyPressed == "BackSpace":
        text = text[:-1]
    if keyPressed == "at":
        text += "@"
    if keyPressed == "period":
        text += "."
    if keyPressed == "comma":
        text += ","
    if keyPressed == "ccedilla":
        text += "ç"
    if keyPressed in "abcdefghijklmnopqrstuvwxyz1234567890":
        text += keyPressed

    return text

buttonLoginPersonal = renderButton(win, winW/2, winH/2-100, "Login Personal")
buttonLoginCliente = renderButton(win, winW/2, winH/2, "Login Cliente")
buttonSair = renderButton(win, winW/2, winH/2+100, "Sair")

exit = False
inputFocus = ""
inputEmail = False
inputSenha = False
textEmail = ""
textSenha = ""

page = "initial"

while not exit:
    mousePos = win.checkMouse()

    if mousePos:
        exit = checkClick(mousePos, buttonSair[2])

        if page == "initial":
            loginPersonal = checkClick(mousePos, buttonLoginPersonal[2])
            loginCliente = checkClick(mousePos, buttonLoginCliente[2])

            if loginPersonal:
                buttonLoginPersonal[3]()
                buttonLoginCliente[3]()
                buttonSair[3]()

                inputEmail = renderInput(win, winW/2, winH/2-100, "Email")
                inputSenha = renderInput(win, winW/2, winH/2, "Senha")
                page = "login-personal"
    
        if page == "login-personal":
            inputEmailFocus = False
            inputSenhaFocus = False
            inputEmail[0].setFill("#fff")
            inputSenha[0].setFill("#fff")

            if inputEmail:
                inputEmailFocus = checkClick(mousePos, inputEmail[2])
            if inputSenha:
                inputSenhaFocus = checkClick(mousePos, inputSenha[2])

            if inputEmailFocus:
                inputEmail[0].setFill("#00B4D8")
                inputFocus = "email"
            if inputSenhaFocus:
                inputSenha[0].setFill("#00B4D8")
                inputFocus = "senha"
    else:
        if inputEmail and inputFocus == "email":
            keyPressed = win.checkKey()

            if keyPressed and keyPressed == "Return":
                inputFocus = ""
            elif keyPressed:             
                textEmail = handleTyping(keyPressed, textEmail)
                inputEmail[5](textEmail)
        
        if inputSenha and inputFocus == "senha":
            keyPressed = win.checkKey()

            if keyPressed and keyPressed == "Return":
                inputFocus = ""
            elif keyPressed:        
                textSenha = handleTyping(keyPressed, textSenha)
                inputSenha[5](textSenha)
            