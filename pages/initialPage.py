from render_functions import renderButton, checkClick

def InitialPage (win, winW, winH, page, leavePage):
    buttonLoginPersonal = renderButton(win, winW/2, winH/2-150, "Login Personal")
    buttonLoginCliente = renderButton(win, winW/2, winH/2-50, "Login Cliente")
    buttonCriarConta = renderButton(win, winW/2, winH/2+50, "Criar conta")
    buttonSair = renderButton(win, winW/2, winH/2+150, "Sair")

    def undraw ():
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
        