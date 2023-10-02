from render_functions import renderButton, checkClick, renderInput, renderImage
from verifyLogin import VerifyLogin
from graphics import Text, Point

def LoginPersonal (win, winW, winH, page, leavePage):
    inputEmail = renderInput (win, winW/2, winH/2-50, 20, 20)
    inputSenha = renderInput (win, winW/2, winH/2, 20, 20)
    buttonLoginPersonal = renderButton(win, winW/2, winH/2+80, "Entrar como Personal")
    buttonReturn = renderImage(win, 30, 30, "arrow-left.png")
    warning = Text(Point(winW/2, winH/2+200), "Credenciais inválidas")
    warning.setFill("red")

    def undraw ():
        inputEmail[2]()
        inputSenha[2]()
        buttonLoginPersonal[3]()
        buttonReturn[2]()
        warning.undraw()

    def interactions(mouseclick):
        if mouseclick:
            exit = checkClick(mouseclick, buttonReturn[1])
            loginPersonal = checkClick(mouseclick, buttonLoginPersonal[2])
            pageNew = page
            tmpLeavePage = leavePage

            if loginPersonal:

                login = VerifyLogin(inputEmail[0].getText(), inputSenha[0].getText(), "Personal")
                if login:
                    undraw()
                    pageNew = "home-personal"
                    tmpLeavePage = True
                else:
                    warning.draw(win)                
            
            if exit:
                undraw()
                pageNew = "initial"
                tmpLeavePage = True
            
            return [pageNew, tmpLeavePage]

    return [
        interactions,
        undraw,
    ]
        