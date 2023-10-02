from graphics import *
from pages.initialPage import InitialPage
from pages.loginPersonal import LoginPersonal

winW = 1000
winH = 800

win = GraphWin("Gym Rats", winW, winH)
win.setBackground("#000")

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

    if page == "exit":
        exit = True

    if page == "initial":
        leavePage = False
        returnedRender = InitialPage(win, winW, winH, page, leavePage)
        while not leavePage:
            mouseClick = win.checkMouse()
            tmp = returnedRender[0](mouseClick)
            if tmp:
                leavePage = tmp[1]
                page = tmp[0]

    if page == "login-personal":
        leavePage = False
        returnedRender = LoginPersonal(win, winW, winH, page, leavePage)
        while not leavePage:
            mouseClick = win.checkMouse()
            tmp = returnedRender[0](mouseClick)
            if tmp:
                leavePage = tmp[1]
                page = tmp[0]

    if page == "login-cliente":
        leavePage = False
        returnedRender = LoginPersonal(win, winW, winH, page, leavePage)
        while not leavePage:
            mouseClick = win.checkMouse()
            tmp = returnedRender[0](mouseClick)
            if tmp:
                leavePage = tmp[1]
                page = tmp[0]           