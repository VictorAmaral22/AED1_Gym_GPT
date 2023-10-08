from render_functions import renderButton, checkClick, renderImage
from crudTreinos import treinoSearch, createHTML, getRoutineExercises
from graphics import GraphWin, Text, Point
from crudUsers import getUser
from exercisesList import getExercises

def CreateWorkout (win, winW, winH, idUser, page, leavePage, userViewing):
    winW2 = 500
    winH2 = 700
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
    
    titleB = Text(Point(120, 300), "Treino B")
    titleB.setFill("#fff")
    titleB.setSize(25)
    titleB.draw(win)
    add2 = renderImage(win, 220, 300, "./assets/plus.png")
    
    titleC = Text(Point(120, 380), "Treino C")
    titleC.setFill("#fff")
    titleC.setSize(25)
    titleC.draw(win)
    add3 = renderImage(win, 220, 380, "./assets/plus.png")
    
    # exercisesList = getExercises()
    # usersButtons = []
    
    # startY = 280
    # for exercise in exercisesList:
    #     buttonGenWorkout = renderButton(win, 200, startY, exercise[1], "#00B4D8", "#fff", "#000")
    #     usersButtons.append(buttonGenWorkout)
    #     startY += 100


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
            clickAdd2 = checkClick(mouseclick, add2[1])
            clickAdd3 = checkClick(mouseclick, add3[1])
            pageNew = page
            tmpLeavePage = leavePage
            userToRedirect = False
            
            startY = 50
            startX = 170
            exercisesList = getExercises()
            usersButtons = []
            pageChange = 0
            

            if exit:
                undraw()
                pageNew = "home-personal"
                tmpLeavePage = True

            if clickAdd1:
                win2 = GraphWin("Gym Rats - Treino A", winW2+500, winH2)
                
                for exercise in exercisesList:
                    if exercise[2] == "A":
                        buttonGenWorkout = renderButton(win2, startX, startY, exercise[1], "#00B4D8", "#fff", "#000")
                        usersButtons.append(buttonGenWorkout)
                        pageChange += 1
                        startY += 100
                        if pageChange%7 == 0:
                            startY = 50
                            startX += 330
                    
                win2.setBackground("#000")
                
            if clickAdd2:
                win2 = GraphWin("Gym Rats - Treino B", winW2+500, winH2)
                
                for exercise in exercisesList:
                    if exercise[2] == "B":
                        buttonGenWorkout = renderButton(win2, startX, startY, exercise[1], "#00B4D8", "#fff", "#000")
                        usersButtons.append(buttonGenWorkout)
                        pageChange += 1
                        startY += 100
                        if pageChange%7 == 0:
                            startY = 50
                            startX += 330
                    
                win2.setBackground("#000")
                
            if clickAdd3:
                win2 = GraphWin("Gym Rats - Treino C", winW2+250, winH2)
                
                for exercise in exercisesList:
                    if exercise[2] == "C":
                        buttonGenWorkout = renderButton(win2, startX, startY, exercise[1], "#00B4D8", "#fff", "#000")
                        usersButtons.append(buttonGenWorkout)
                        pageChange += 1
                        startY += 100
                        if pageChange%7 == 0:
                            startY = 50
                            startX += 330
                    
                win2.setBackground("#000")
                
            print(usersButtons)
            return [pageNew, tmpLeavePage, userToRedirect]

    return [
        interactions,
        undraw,
    ]
        