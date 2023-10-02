from render_functions import renderButton, checkClick, renderImage

def HomeCliente (win, winW, winH, page, leavePage):
    buttonGenWorkout = renderButton(win, winW/2, winH/2, "Mostrar ficha de treino")
    buttonReturn = renderImage(win, 30, 30, "arrow-left.png")

    def undraw ():
        buttonGenWorkout[3]()
        buttonReturn[2]()

    def interactions(mouseclick):
        if mouseclick:
            exit = checkClick(mouseclick, buttonReturn[1])
            mostrarTreino = checkClick(mouseclick, buttonGenWorkout[2])
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
        