from graphics import *
from render_functions import renderButton, renderInput, checkClick, handleTyping, renderImage
from verifyLogin import VerifyLogin
from initialPage import InitialPage

winW = 1000
winH = 800

win = GraphWin("Gym Rats", winW, winH)
win.setBackground("#000")

# buttonLoginCliente = renderButton(win, winW/2, winH/2, "Login Cliente")
# buttonLoginPersonal = renderButton(win, winW/2, winH/2-100, "Login Personal")
# buttonSair = renderButton(win, winW/2, winH/2+100, "Sair")

exit = False
inputFocus = ""
inputEmail = False
inputSenha = False
loginPersonalEnter = False
textEmail = ""
textSenha = ""
returnImg = False

page = "initial"

while not exit:
    if win.closed:
        break
    
    print(page)
    if page == "initial":
        leavePage = False
        returnedRender = InitialPage(win, winW, winH, page, leavePage)
        while not leavePage:
            keyPressed = win.checkKey()
            mouseClick = win.checkMouse()
            returnedRender[0](keyPressed, mouseClick)


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
            