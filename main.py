from graphics import *
from pages.initialPage import InitialPage
from pages.loginPersonal import LoginPersonal
from pages.loginCliente import LoginCliente
from pages.criarConta import CriarConta
from pages.homeCliente import HomeCliente
from pages.homePersonal import HomePersonal
from pages.createWorkout import CreateWorkout

winW = 1280
winH = 720

win = GraphWin("Gym Rats", winW, winH)
win.setBackground("#000")

exit = False
loggedUser = False
userViewing = False

page = "initial"

if loggedUser:
    page = "home-personal"

while not exit:
    if win.closed:
        break

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
        returnedRender = HomePersonal(win, winW, winH, loggedUser, page, leavePage)
        while not leavePage:
            mouseClick = win.checkMouse()
            tmp = returnedRender[0](mouseClick)
            if tmp:
                leavePage = tmp[1]
                page = tmp[0]
                userViewing = tmp[2]
    
    if page == "create-workout":
        leavePage = False
        returnedRender = CreateWorkout(win, winW, winH, loggedUser, page, leavePage, userViewing)
        while not leavePage:
            mouseClick = win.checkMouse()
            tmp = returnedRender[0](mouseClick)
            if tmp:
                leavePage = tmp[1]
                page = tmp[0]