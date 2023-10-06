from render_functions import renderButton, checkClick, renderInput, renderImage
from crudUsers import VerifyLogin
from graphics import Text, Point

def LoginPersonal (win, winW, winH, page, leavePage):
    bgImage = renderImage(win, winW/2, winH/2, "./assets/background-login.png")
    logo = renderImage(win, winW/2-400, winH/2, "./assets/gym-rats-logo.png")
    inputEmail = renderInput (win, winW-250, winH/2-70, 20, 20, "Email", "#fff", "#000")
    inputSenha = renderInput (win, winW-250, winH/2, 20, 20, "Senha", "#fff", "#000")
    buttonLoginPersonal = renderButton(win, winW-250, winH/2+80, "Entrar como Personal", "#00B4D8", "#fff", "#fff")
    buttonReturn = renderImage(win, 30, 30, "./assets/arrow-left.png")
    warning = Text(Point(winW-250, winH/2+200), "Credenciais inválidas")
    warning.setFill("red")

    def undraw ():
        bgImage[2]()
        logo[2]()
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
            userLogged = False

            if loginPersonal:

                login = VerifyLogin(inputEmail[0].getText(), inputSenha[0].getText(), "Personal")
                if login:
                    undraw()
                    pageNew = "home-personal"
                    tmpLeavePage = True
                    userLogged = login
                else:
                    warning.undraw()
                    warning.draw(win)                
            
            if exit:
                undraw()
                pageNew = "initial"
                tmpLeavePage = True
            
            return [pageNew, tmpLeavePage, userLogged]

    return [
        interactions,
        undraw,
    ]
        