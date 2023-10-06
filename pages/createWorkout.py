from render_functions import renderButton, checkClick, renderImage
from crudTreinos import treinoSearch, createHTML, getRoutineExercises
from graphics import GraphWin, Text, Point
from crudUsers import getUser

def CreateWorkout (win, winW, winH, idUser, page, leavePage, userViewing):
    winW2 = 500
    winH2 = 1000
    bgImage = renderImage(win, winW/2, winH/2, "./assets/background.png")
    logo = renderImage(win, 110, 40, "./assets/logo-small.png")
    buttonReturn = renderImage(win, 30, 40, "./assets/arrow-left.png")
    title = Text(Point(290, 150), "Gerencie o treino do cliente")
    title.setFill("#fff")
    title.setSize(30)
    title.draw(win)
    buttonSave = renderButton(win, winW-200, winH-100, "Salvar", "#00B4D8", "#fff", "#fff")

    # userData = getUser(userViewing)
    # exercicesA = getRoutineExercises("A")
    # exercicesB = getRoutineExercises("B")
    # exercicesC = getRoutineExercises("C")

    titleA = Text(Point(120, 220), "Treino A")
    titleA.setFill("#fff")
    titleA.setSize(25)
    titleA.draw(win)
    add1 = renderImage(win, 220, 220, "./assets/plus.png")


    # win2 = GraphWin("Gym Rats", winW2, winH2)
    # win2.setBackground("#000")

    # print(userData)
    # print(exercicesA)
    # print(exercicesB)
    # print(exercicesC)

    def undraw ():
        bgImage[2]()
        logo[2]()
        buttonReturn[2]()
        buttonSave[3]()
        title.undraw()

    def interactions(mouseclick):
        if mouseclick:
            exit = checkClick(mouseclick, buttonReturn[1])
            clickAdd1 = checkClick(mouseclick, add1[1])
            pageNew = page
            tmpLeavePage = leavePage
            userToRedirect = False

            if exit:
                undraw()
                pageNew = "home-personal"
                tmpLeavePage = True

            if clickAdd1:
                win2 = GraphWin("Gym Rats - Treino A", winW2, winH2)
                win2.setBackground("#000")
                
            
            return [pageNew, tmpLeavePage, userToRedirect]

    return [
        interactions,
        undraw,
    ]
        