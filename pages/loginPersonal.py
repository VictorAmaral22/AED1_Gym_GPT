from render_functions import renderButton, checkClick, renderInput

def LoginPersonal (win, winW, winH, page, leavePage):
    inputEmail = renderInput (win, winW/2, winH/2-50, 17, 23)
    inputSenha = renderInput (win, winW/2, winH/2, 17, 23)
    buttonLoginPersonal = renderButton(win, winW/2, winH/2+80, "Entrar como Personal")
    # buttonLoginCliente = renderButton(win, winW/2, winH/2, "Login Cliente")
    # buttonSair = renderButton(win, winW/2, winH/2+100, "Sair")

    def undraw ():
        print("undraw")
        # buttonLoginPersonal[3]()
        # buttonLoginCliente[3]()
        # buttonSair[3]()

    def draw ():
        print("draw")
        # buttonLoginPersonal[3]()
        # buttonLoginCliente[3]()
        # buttonSair[3]()

    def interactions(mouseclick):
         i = 1 + 1
        # print("interactions")
        # if mouseclick:
            # exit = checkClick(mouseclick, buttonSair[2])
            # loginPersonal = checkClick(mouseclick, buttonLoginPersonal[2])
            # loginCliente = checkClick(mouseclick, buttonLoginCliente[2])
            # pageNew = page
            # tmpLeavePage = leavePage

            # if loginPersonal:
            #     undraw()
            #     pageNew = "login-personal"
            #     tmpLeavePage = True

            # if loginCliente:
            #     undraw()
            #     pageNew = "login-cliente"
            #     tmpLeavePage = True
            
            # if exit:
            #     undraw()
            #     pageNew = "exit"
            #     tmpLeavePage = True
            
            # return [pageNew, tmpLeavePage]

    return [
        interactions,
        undraw,
        draw,
    ]
        