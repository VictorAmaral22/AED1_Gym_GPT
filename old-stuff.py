# if mousePos:
            # exit = checkClick(mousePos, buttonSair[2])
            # loginPersonal = checkClick(mousePos, buttonLoginPersonal[2])
            # loginCliente = checkClick(mousePos, buttonLoginCliente[2])

            # if loginPersonal:
            #     buttonLoginPersonal[3]()
            #     buttonLoginCliente[3]()
            #     buttonSair[3]()

            #     inputEmail = renderInput(win, winW/2, winH/2-100, "Email")
            #     inputSenha = renderInput(win, winW/2, winH/2, "Senha")
            #     loginPersonalEnter = renderButton(win, winW/2, winH/2+100, "Entrar")
            #     returnImg = renderImage(win, 40, 40, "arrow-left.png")
            #     page = "login-personal"
    
        # if page == "login-personal":
            # inputEmailFocus = False
            # inputSenhaFocus = False
            # inputEmail[0].setFill("#fff")
            # inputSenha[0].setFill("#fff")
            # hasClickedLogin = checkClick(mousePos, loginPersonalEnter[2])
            # warning = False

            # if inputEmail:
            #     inputEmailFocus = checkClick(mousePos, inputEmail[2])
            # if inputSenha:
            #     inputSenhaFocus = checkClick(mousePos, inputSenha[2])
            # if hasClickedLogin:
            #     verifiedUser = VerifyLogin(textEmail, textSenha, "Personal")

            #     if verifiedUser:
            #         inputEmail[3]()
            #         inputSenha[3]()
            #         loginPersonalEnter[3]()
            #         if warning:
            #             warning.undraw()
            #     else:
            #         warning = Text(Point(winW/2, winH/2+200), "Credenciais inválidas")
            #         warning.setTextColor("red")
            #         warning.draw(win)           
                    

            # if inputEmailFocus:
            #     inputEmail[0].setFill("#00B4D8")
            #     inputFocus = "email"
            # if inputSenhaFocus:
            #     inputSenha[0].setFill("#00B4D8")
            #     inputFocus = "senha"
    # else:
    #     if inputEmail and inputFocus == "email":
    #         keyPressed = win.checkKey()

    #         if keyPressed and keyPressed == "Return":
    #             inputFocus = ""
    #         elif keyPressed:             
    #             textEmail = handleTyping(keyPressed, textEmail)
    #             inputEmail[5](textEmail)
        
    #     if inputSenha and inputFocus == "senha":
    #         keyPressed = win.checkKey()

    #         if keyPressed and keyPressed == "Return":
    #             inputFocus = ""
    #         elif keyPressed:        
    #             textSenha = handleTyping(keyPressed, textSenha)
    #             inputSenha[5](textSenha)





# def renderInput (win, posW, posH, label):
#     inputW = 150
#     inputH = 30
#     input = Rectangle(Point(posW-inputW, posH-inputH), Point(posW+inputW, posH+inputH))
#     input.draw(win)
#     input.setFill("#fff")
#     inputContent = Text(input.getCenter(), "")
#     inputContent.setFill("#000")
#     inputContent.draw(win)

#     inputLabel = Text(Point(input.getP1().x+20, input.getP1().y-20), label)
#     inputLabel.setFill("#fff")
#     inputLabel.draw(win)

#     p1 = input.getP1()
#     p2 = input.getP2()

#     corners = [p1, p2]

#     def undraw ():
#         input.undraw()
#         inputContent.undraw()
#         inputLabel.undraw()

#     def draw ():
#         input.draw(win)
#         inputContent.draw(win)

#     def changeTxt (txt):
#         inputContent.setText(txt)

#     return [
#         input,
#         inputContent,
#         corners,
#         undraw,
#         draw,
#         changeTxt
#     ]

# def handleTyping (keyPressed, text):
#     if keyPressed == "space":
#         text += " "
#     if keyPressed == "BackSpace":
#         text = text[:-1]
#     if keyPressed == "at":
#         text += "@"
#     if keyPressed == "period":
#         text += "."
#     if keyPressed == "comma":
#         text += ","
#     if keyPressed == "ccedilla":
#         text += "ç"
#     if keyPressed in "abcdefghijklmnopqrstuvwxyz1234567890":
#         text += keyPressed

#     return text