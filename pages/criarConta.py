from render_functions import renderButton, checkClick, renderInput, renderImage
from graphics import Text, Point
from crudUsers import userInsert

def CriarConta (win, winW, winH, page, leavePage):
    bgImage = renderImage(win, winW/2, winH/2, "./assets/background-login.png")
    logo = renderImage(win, winW/2-400, winH/2, "./assets/gym-rats-logo.png")
    inputNome = renderInput (win, winW-250, winH/2-250, 20, 20, "Nome", "#fff", "#000")
    inputEmail = renderInput (win, winW-250, winH/2-180, 20, 20, "Email", "#fff", "#000")
    inputSenha = renderInput (win, winW-250, winH/2-110, 20, 20, "Senha", "#fff", "#000")
    inputAltura = renderInput (win, winW-250, winH/2-40, 20, 20, "Altura", "#fff", "#000")
    inputPeso = renderInput (win, winW-250, winH/2+30, 20, 20, "Peso", "#fff", "#000")
    inputIdade = renderInput (win, winW-250, winH/2+100, 20, 20, "Idade", "#fff", "#000")
    buttonCriar = renderButton(win, winW-250, winH/2+250, "Cadastrar")

    buttonReturn = renderImage(win, 30, 40, "./assets/arrow-left.png")
    warning = Text(Point(winW/2, winH/2+170), "Valores errados")
    warning.setFill("red")

    def undraw ():
        bgImage[2]()
        logo[2]()
        inputNome[2]()
        inputEmail[2]()
        inputSenha[2]()
        inputAltura[2]()
        inputPeso[2]()
        inputIdade[2]()
        buttonCriar[3]()
        warning.undraw()

    def interactions(mouseclick):
        if mouseclick:
            exit = checkClick(mouseclick, buttonReturn[1])
            create = checkClick(mouseclick, buttonCriar[2])

            pageNew = page
            tmpLeavePage = leavePage
            userLogged = False
            warning.undraw()

            if create:
                hasError = False
                nome = inputNome[0].getText()
                email = inputEmail[0].getText()
                senha = inputSenha[0].getText()
                altura = inputAltura[0].getText()
                peso = inputPeso[0].getText()
                idade = inputIdade[0].getText()

                if not hasError and len(nome) == 0:
                    warning.setText("Informe um nome válido!")
                    warning.draw(win)
                    hasError = True

                if not hasError and len(email) == 0:
                    warning.setText("Informe um email válido!")
                    warning.draw(win)
                    hasError = True

                if not hasError and len(senha) == 0:
                    warning.setText("Informe uma senha válida!")
                    warning.draw(win)
                    hasError = True
                
                if not hasError and len(altura) == 0:
                    warning.setText("Informe uma altura válida!")
                    warning.draw(win)
                    hasError = True

                if not hasError and len(peso) == 0:
                    warning.setText("Informe uma peso válido!")
                    warning.draw(win)
                    hasError = True

                if not hasError and len(idade) == 0:
                    warning.setText("Informe a idade válida!")
                    warning.draw(win)
                    hasError = True

                if not hasError:
                    validade = userInsert(nome, "Cliente", email, senha, altura, peso, idade)

                    if not validade:
                        warning.setText("Este email já está cadastrado!")
                        warning.draw(win)
                    else:
                        userLogged = validade
                        undraw()
                        pageNew = "login-cliente"
                        tmpLeavePage = True        

            if exit:
                undraw()
                pageNew = "initial"
                tmpLeavePage = True
            
            return [pageNew, tmpLeavePage, userLogged]

    return [
        interactions,
        undraw,
    ]
        