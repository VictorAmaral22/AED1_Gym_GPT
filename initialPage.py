from render_functions import renderButton, checkClick

def InitialPage (win, winW, winH, page, leavePage):
    buttonLoginPersonal = renderButton(win, winW/2, winH/2-100, "Login Personal")
    buttonLoginCliente = renderButton(win, winW/2, winH/2, "Login Cliente")
    buttonSair = renderButton(win, winW/2, winH/2+100, "Sair")

    def undraw ():
        buttonLoginPersonal[3]()
        buttonLoginCliente[3]()
        buttonSair[3]()

    def draw ():
        buttonLoginPersonal[3]()
        buttonLoginCliente[3]()
        buttonSair[3]()

    def interactions(keypressed, mouseclick):
        if mouseclick:
            exit = checkClick(mouseclick, buttonSair[2])
            loginPersonal = checkClick(mouseclick, buttonLoginPersonal[2])
            loginCliente = checkClick(mouseclick, buttonLoginCliente[2])

            if loginPersonal:
                undraw()
                page = "login-personal"
                leavePage = True


            # print(exit)
            # print(loginPersonal)
            # print(loginCliente)

    return [
        interactions,
        undraw,
        draw,
    ]
        