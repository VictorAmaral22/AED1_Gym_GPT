from render_functions import renderButton, checkClick, renderImage
from crudTreinos import treinoSearch, createHTML
from graphics import Text, Point
from crudUsers import getUsersWithNoWorkouts

def HomePersonal (win, winW, winH, idUser, page, leavePage):
    bgImage = renderImage(win, winW/2, winH/2, "./assets/background.png")
    logo = renderImage(win, 110, 40, "./assets/logo-small.png")
    buttonReturn = renderImage(win, 30, 40, "./assets/arrow-left.png")
    title = Text(Point(290, 150), "Bem vindo ao GYM RATS!")
    title.setFill("#fff")
    title.setSize(30)
    title.draw(win)

    subTitle = Text(Point(315, 200), "Selecione um dos seus clientes para editar")
    subTitle.setFill("#fff")
    subTitle.setSize(20)
    subTitle.draw(win)

    usersWithNoWorkouts = getUsersWithNoWorkouts()
    usersButtons = []

    startY = 280
    for user in usersWithNoWorkouts:
        buttonGenWorkout = renderButton(win, 200, startY, user[1], "#00B4D8", "#fff", "#000")
        usersButtons.append(buttonGenWorkout)
        startY += 100

    def undraw ():
        bgImage[2]()
        logo[2]()
        buttonReturn[2]()
        title.undraw()
        subTitle.undraw()
        for user in usersButtons:
            user[3]()

    def interactions(mouseclick):
        if mouseclick:
            exit = checkClick(mouseclick, buttonReturn[1])
            pageNew = page
            tmpLeavePage = leavePage
            userToRedirect = False

            if exit:
                undraw()
                pageNew = "initial"
                tmpLeavePage = True

            c = 0
            for user in usersButtons:
                clicked = checkClick(mouseclick, user[2])

                if clicked:
                    undraw()
                    pageNew = "create-workout"
                    tmpLeavePage = True
                    userToRedirect = usersWithNoWorkouts[c][0]

                c += 1
            
            return [pageNew, tmpLeavePage, userToRedirect]

    return [
        interactions,
        undraw,
    ]
        