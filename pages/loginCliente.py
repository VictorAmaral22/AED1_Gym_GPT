from render_functions import renderButton, checkClick, renderInput, renderImage

def LoginCliente (win, winW, winH, page, leavePage):
    inputEmail = renderInput (win, winW/2, winH/2-50, 17, 23)
    inputSenha = renderInput (win, winW/2, winH/2, 17, 23)
    buttonLoginPersonal = renderButton(win, winW/2, winH/2+80, "Entrar como Cliente")
    returnButton = renderImage (win, 30, 30, "arrow-left.png")

    def undraw ():
        print("undraw")
        inputEmail[3]()
        inputSenha[3]()
        buttonLoginPersonal[3]()

    def interactions(mouseclick):
        i = 1
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
    ]
        