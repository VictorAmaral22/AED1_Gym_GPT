from render_functions import renderButton, checkClick, renderImage
from treinoSearch import treinoSearch
from treinoMostrar import createHTML
from graphics import Text, Point

def HomeCliente (win, winW, winH, idUser, page, leavePage):
    buttonGenWorkout = renderButton(win, winW/2, winH/2, "Mostrar ficha de treino")
    buttonReturn = renderImage(win, 30, 30, "arrow-left.png")
    warning = Text(Point(winW/2, winH/2+200), "Você ainda não tem uma ficha de treino")
    warning.setFill("red")

    def undraw ():
        buttonGenWorkout[3]()
        buttonReturn[2]()
        warning.undraw()

    def interactions(mouseclick):
        if mouseclick:
            exit = checkClick(mouseclick, buttonReturn[1])
            mostrarTreino = checkClick(mouseclick, buttonGenWorkout[2])
            pageNew = page
            tmpLeavePage = leavePage
            
            if mostrarTreino:
                temTreino = treinoSearch(idUser)
                if temTreino:
                    createHTML()
                else:
                    warning.draw(win)


            if exit:
                undraw()
                pageNew = "initial"
                tmpLeavePage = True
            
            return [pageNew, tmpLeavePage]

    return [
        interactions,
        undraw,
    ]
        