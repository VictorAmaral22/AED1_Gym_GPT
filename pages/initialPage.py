from render_functions import renderButton, checkClick, renderImage

def InitialPage (win, winW, winH, page, leavePage):
    bgImage = renderImage(win, winW/2, winH/2, "./assets/background-login.png")
    logo = renderImage(win, winW/2-400, winH/2, "./assets/gym-rats-logo.png")
    buttonLoginPersonal = renderButton(win, winW-250, winH/2-150, "Login Personal", "#00B4D8", "#fff", "#fff")
    buttonLoginCliente = renderButton(win, winW-250, winH/2-50, "Login Cliente", "#00B4D8", "#fff", "#fff")
    buttonCriarConta = renderButton(win, winW-250, winH/2+50, "Criar conta", "#00B4D8", "#fff", "#fff")
    buttonSair = renderButton(win, winW-250, winH/2+150, "Sair", "#fff", "#000", "#000")

    def undraw ():
        bgImage[2]()
        logo[2]()
        buttonLoginPersonal[3]()
        buttonLoginCliente[3]()
        buttonCriarConta[3]()
        buttonSair[3]()

    def interactions(mouseclick):
        if mouseclick:
            exit = checkClick(mouseclick, buttonSair[2])
            loginPersonal = checkClick(mouseclick, buttonLoginPersonal[2])
            loginCliente = checkClick(mouseclick, buttonLoginCliente[2])
            criarConta = checkClick(mouseclick, buttonCriarConta[2])
            pageNew = page
            tmpLeavePage = leavePage

            if loginPersonal:
                undraw()
                pageNew = "login-personal"
                tmpLeavePage = True

            if loginCliente:
                undraw()
                pageNew = "login-cliente"
                tmpLeavePage = True

            if criarConta:
                undraw()
                pageNew = "criar-conta"
                tmpLeavePage = True
            
            if exit:
                undraw()
                pageNew = "exit"
                tmpLeavePage = True
            
            return [pageNew, tmpLeavePage]

    return [
        interactions,
        undraw,
    ]
        