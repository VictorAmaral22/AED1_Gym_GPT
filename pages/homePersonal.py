from render_functions import renderButton, checkClick, renderImage
from crudTreinos import treinoSearch, createHTML
from graphics import Text, Point
from crudUsers import getUsersWithNoWorkouts

def HomePersonal (win, winW, winH, idUser, page, leavePage):
    # buttonGenWorkout = renderButton(win, winW/2, winH/2, "Mostrar ficha de treino")
    buttonReturn = renderImage(win, 30, 30, "./assets/arrow-left.png")
    warning = Text(Point(winW/2, winH/2+200), "Você ainda não tem uma ficha de treino")
    warning.setFill("red")
    usersWithNoWorkouts = getUsersWithNoWorkouts()
    print(usersWithNoWorkouts)

    # if len(usersWithNoWorkouts) > 0:


    def undraw ():
        buttonReturn[2]()
        warning.undraw()

    def interactions(mouseclick):
        if mouseclick:
            exit = checkClick(mouseclick, buttonReturn[1])
            pageNew = page
            tmpLeavePage = leavePage

            if exit:
                undraw()
                pageNew = "initial"
                tmpLeavePage = True
            
            return [pageNew, tmpLeavePage]

    return [
        interactions,
        undraw,
    ]
        