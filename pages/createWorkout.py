from render_functions import renderButton, checkClick, renderImage
from crudTreinos import treinoSearch, createHTML, getRoutineExercises
from graphics import GraphWin, Text, Point
from crudUsers import getUser
from exercisesList import getExercises
from crudTreinos import treinoSearch, getUserExercises

def CreateWorkout (win, winW, winH, idUser, page, leavePage, userViewing):
    exercisesList = getUserExercises(userViewing)
    exercisesWindows = []
    bgImage = renderImage(win, winW/2, winH/2, "./assets/background.png")
    logo = renderImage(win, 110, 40, "./assets/logo-small.png")
    buttonReturn = renderImage(win, 30, 40, "./assets/arrow-left.png")
    title = Text(Point(450, 40), "Gerencie o treino do cliente")
    title.setFill("#fff")
    title.setSize(30)
    title.draw(win)
    
    folderExercices = renderImage(win, winW/2, winH/2+100, "./assets/exercices_folder.png")
    folderTop = renderImage(win, 459, 192, "./assets/treinos-folder.png")

    folderTabA = renderImage(win, 215, 192, "./assets/treino-a-active.png")
    folderTabB = False
    folderTabC = False

    print(exercisesList)

    # buttonSave = renderButton(win, winW-200, winH-100, "Salvar", "#00B4D8", "#fff", "#fff")

    # titleA = Text(Point(110, 220), "Treino A")
    # titleA.setFill("#fff")
    # titleA.setSize(25)
    # titleA.draw(win)
    # add1 = renderImage(win, 220, 220, "./assets/plus.png")
    
    # titleB = Text(Point(300, 220), "Treino B")
    # titleB.setFill("#fff")
    # titleB.setSize(25)
    # titleB.draw(win)
    # add2 = renderImage(win, 220, 300, "./assets/plus.png")
    
    # titleC = Text(Point(500, 220), "Treino C")
    # titleC.setFill("#fff")
    # titleC.setSize(25)
    # titleC.draw(win)
    # add3 = renderImage(win, 220, 380, "./assets/plus.png")

    def undraw ():
        bgImage[2]()
        logo[2]()
        folderExercices[2]()
        folderTop[2]()
        buttonReturn[2]()
        title.undraw()

        if folderTabA:
            folderTabA[2]()
        if folderTabB:
            folderTabB[2]()
        if folderTabC:
            folderTabC[2]()
        # buttonSave[3]()
        # titleA.undraw()
        # titleB.undraw()
        # titleC.undraw()
        # add1[2]()
        # add2[2]()
        # add3[2]()

        for window in exercisesWindows:
            window.close()

    def interactions(mouseclick):
        if mouseclick:
            exit = checkClick(mouseclick, buttonReturn[1])
            # clickAdd1 = checkClick(mouseclick, add1[1])
            # clickAdd2 = checkClick(mouseclick, add2[1])
            # clickAdd3 = checkClick(mouseclick, add3[1])
            pageNew = page
            tmpLeavePage = leavePage
            userToRedirect = False
            
            startY = 50
            startX = 170
            usersButtons = []
            pageChange = 0
            

            if exit:
                undraw()
                pageNew = "home-personal"
                tmpLeavePage = True

            # if clickAdd1:
            #     for window in exercisesWindows:
            #         window.close()

            #     win2 = GraphWin("Gym Rats - Treino A", winW2+500, winH2)
                
            #     exercisesWindows.append(win2)

            #     for exercise in exercisesList:
            #         if exercise[2] == "A":
            #             buttonGenWorkout = renderButton(win2, startX, startY, exercise[1], "#00B4D8", "#fff", "#000")
            #             usersButtons.append(buttonGenWorkout)
            #             pageChange += 1
            #             startY += 100
            #             if pageChange%7 == 0:
            #                 startY = 50
            #                 startX += 330
                    
            #     win2.setBackground("#000")

            #     leaveSubPage = False
            #     while not leaveSubPage:
            #         if win.closed:
            #             break

            #         clickSubWin = win.checkMouse()
            #         if clickSubWin:
            #             print(clickSubWin)
                
            # if clickAdd2:
            #     for window in exercisesWindows:
            #         window.close()

            #     win2 = GraphWin("Gym Rats - Treino B", winW2+500, winH2)

            #     exercisesWindows.append(win2)
                
            #     for exercise in exercisesList:
            #         if exercise[2] == "B":
            #             buttonGenWorkout = renderButton(win2, startX, startY, exercise[1], "#00B4D8", "#fff", "#000")
            #             usersButtons.append(buttonGenWorkout)
            #             pageChange += 1
            #             startY += 100
            #             if pageChange%7 == 0:
            #                 startY = 50
            #                 startX += 330
                    
            #     win2.setBackground("#000")

            #     leaveSubPage = False
            #     while not leaveSubPage:
            #         if win.closed:
            #             break

            #         clickSubWin = win.checkMouse()                        
                
            # if clickAdd3:
            #     for window in exercisesWindows:
            #         window.close()
                    
            #     win2 = GraphWin("Gym Rats - Treino C", winW2+250, winH2)

            #     exercisesWindows.append(win2)
                
            #     for exercise in exercisesList:
            #         if exercise[2] == "C":
            #             buttonGenWorkout = renderButton(win2, startX, startY, exercise[1], "#00B4D8", "#fff", "#000")
            #             usersButtons.append(buttonGenWorkout)
            #             pageChange += 1
            #             startY += 100
            #             if pageChange%7 == 0:
            #                 startY = 50
            #                 startX += 330
                    
            #     win2.setBackground("#000")

            #     leaveSubPage = False
            #     while not leaveSubPage:
            #         if win.closed:
            #             break

            #         clickSubWin = win.checkMouse()
            #         if clickSubWin:
            #             print(clickSubWin)
                
            return [pageNew, tmpLeavePage, userToRedirect]

    return [
        interactions,
        undraw,
    ]
        