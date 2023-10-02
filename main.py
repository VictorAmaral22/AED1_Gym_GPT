from graphics import *
from pages.initialPage import InitialPage
from pages.loginPersonal import LoginPersonal
from pages.loginCliente import LoginCliente
from pages.homeCliente import HomeCliente
from pages.criarConta import CriarConta

winW = 1000
winH = 800

win = GraphWin("Gym Rats", winW, winH)
win.setBackground("#000")

exit = False
loggedUser = False

page = "initial"

while not exit:
    if win.closed:
        break
    
    # print(page)
    # print(loggedUser)

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
                if tmp[2]:
                    loggedUser = tmp[2]

    if page == "login-cliente":
        leavePage = False
        returnedRender = LoginCliente(win, winW, winH, page, leavePage)
        while not leavePage:
            mouseClick = win.checkMouse()
            tmp = returnedRender[0](mouseClick)
            if tmp:
                leavePage = tmp[1]
                page = tmp[0]
                if tmp[2]:
                    loggedUser = tmp[2]
    
    if page == "criar-conta":
        leavePage = False
        returnedRender = CriarConta(win, winW, winH, page, leavePage)
        while not leavePage:
            mouseClick = win.checkMouse()
            tmp = returnedRender[0](mouseClick)
            if tmp:
                leavePage = tmp[1]
                page = tmp[0]

    if page == "home-cliente":
        leavePage = False
        returnedRender = HomeCliente(win, winW, winH, loggedUser, page, leavePage)
        while not leavePage:
            mouseClick = win.checkMouse()
            tmp = returnedRender[0](mouseClick)
            if tmp:
                leavePage = tmp[1]
                page = tmp[0]
    
    if page == "home-personal":
        leavePage = False
        returnedRender = HomeCliente(win, winW, winH, loggedUser, page, leavePage)
        while not leavePage:
            mouseClick = win.checkMouse()
            tmp = returnedRender[0](mouseClick)
            if tmp:
                leavePage = tmp[1]
                page = tmp[0]