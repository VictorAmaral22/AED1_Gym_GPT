from render_functions import checkClick, renderImage, renderInput, renderTxt
from graphics import Text, Point
from crudTreinos import getUserExercises

folderTabA = False
folderTabB = False
folderTabC = False
arrowLeft = False
arrowRight = False
paginationExercises = 1

def tabClicked (win, tab):
        global folderTabA
        global folderTabB
        global folderTabC
        global page
        
        if folderTabA:
            folderTabA[2]()
            folderTabA = False
        if folderTabB:
            folderTabB[2]()
            folderTabB = False
        if folderTabC:
            folderTabC[2]()
            folderTabC = False
        
        if tab == "A":
            folderTabA = renderImage(win, 215, 192, "./assets/treino-a-active.png")
            page = 1
        if tab == "B":            
            folderTabB = renderImage(win, 460, 192, "./assets/treino-b-active.png")
            page = 1
        if tab == "C":
            folderTabC = renderImage(win, 705, 192, "./assets/treino-c-active.png")
            page = 1

def CreateWorkout (win, winW, winH, idUser, page, leavePage, userViewing):
    global folderTabA
    global folderTabB
    global folderTabC
    exercisesList = getUserExercises(userViewing)
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
    filteredExercices = []

    def filterExercises (workout, list):
        filtered = []
        for exercise in list:
            if exercise[1] == workout:
                filtered.append(exercise)

        return filtered
    
    exercisesA = filterExercises("A", exercisesList)
    exercisesB = filterExercises("B", exercisesList)
    exercisesC = filterExercises("C", exercisesList)

    def pagination (pageExerc, exercices):
        global arrowLeft
        global arrowRight
        limit = pageExerc * 12
        nextLimit = (pageExerc+1) * 12
        start = limit - 12
        
        if arrowLeft:
            arrowLeft[2]()
            arrowLeft = False
        if arrowRight:
            arrowRight[2]()
            arrowRight = False

        if pageExerc != 1:
            arrowLeft = renderImage(win, winW/2-100, winH-60, "./assets/pagination-left.png")

        if len(exercices[(nextLimit-12):nextLimit]) > 0:
            arrowRight = renderImage(win, winW/2+100, winH-60, "./assets/pagination-right.png")

        return exercices[start:limit]

    filteredExercices = pagination(1, exercisesA)

    inputsRendered = []

    def renderExercices (filteredList):
        for input in inputsRendered:
            input[2]()

        y = 310

        for exercise in filteredList:
            titleNome = renderTxt(win, 215, 270, "#fff", "Exercício", 20)
            exerciseName = renderInput(win, 390, y, 30, 20, "", "#fff", "#000", True, exercise[2])
            inputsRendered.append(exerciseName)
            
            titleEmail = renderTxt(win, 660, 270, "#fff", "Séries", 20)
            exerciseSerie = renderInput(win, 700, y, 10, 20, "", "#fff", "#000", True, exercise[3])
            inputsRendered.append(exerciseSerie)
            
            titleHeight = renderTxt(win, 850, 270, "#fff", "Repetições", 20)
            exerciseRep = renderInput(win, 860, y, 10, 20, "", "#fff", "#000", True, exercise[4])
            inputsRendered.append(exerciseRep)
                                    
            # nameImage = renderImage(win, 350, y, "./assets/input-big.png")
            # nameTxt = renderTxt(win, 350, y, "#000", exercise[2], 20)
            
            # serieImage = renderImage(win, 800, y, "./assets/input-big.png")
            # serieTxt = renderTxt(win, 800, y, "#000", exercise[3], 20)
            
            # repsImage = renderImage(win, 1250, y, "./assets/input-big.png")
            # repsTxt = renderTxt(win, 1250, y, "#000", exercise[4], 20)

            # enterImage = renderImage(win, 1600, y, "./assets/open.png")

            

            y += 50

    renderExercices(filteredExercices)

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
        if arrowLeft:
            arrowLeft[2]()
        if arrowRight:
            arrowRight[2]()

        for input in inputsRendered:
            input[2]()
    
    def interactions(mouseclick):
        global arrowLeft
        global arrowRight
        global paginationExercises

        if mouseclick:
            exit = checkClick(mouseclick, buttonReturn[1])
            pageNew = page
            tmpLeavePage = leavePage
            userToRedirect = False

            clickedTabA = checkClick(mouseclick, [
                Point(96.0, 162.0),
                Point(334.0, 220.0)
            ])
            clickedTabB = checkClick(mouseclick, [
                Point(341.0, 162.0),
                Point(581.0, 220.0)
            ])
            clickedTabC = checkClick(mouseclick, [
                Point(588.0, 162.0),
                Point(826.0, 220.0)
            ])

            paginationLeft = False
            if arrowLeft:
                paginationLeft = checkClick(mouseclick, arrowLeft[1])

            paginationRight = False
            if arrowRight:
                paginationRight = checkClick(mouseclick, arrowRight[1])

            if exit:
                undraw()
                pageNew = "home-personal"
                tmpLeavePage = True

            if clickedTabA:
                tabClicked(win, "A")
                filteredExercices = pagination(1, exercisesA)
                renderExercices(filteredExercices)
                cont = 0
                for i in range(0, len(inputsRendered)//3):
                    exer = inputsRendered[cont][0].getText()
                    cont+=1
                    serie = inputsRendered[cont][0].getText()
                    cont+=1
                    rep = inputsRendered[cont][0].getText()
                    cont+=1
                    print(str(userViewing)+";"+exer+";"+serie+";"+rep)
            
            if clickedTabB:
                tabClicked(win, "B")
                filteredExercices = pagination(1, exercisesB)
                renderExercices(filteredExercices)

            if clickedTabC:
                tabClicked(win, "C")
                filteredExercices = pagination(1, exercisesC)
                renderExercices(filteredExercices)

            if paginationLeft or paginationRight:
                if paginationLeft:
                    paginationExercises -= 1
                if paginationRight:
                    paginationExercises += 1

                exercices = []
                if folderTabA:
                    exercices = exercisesA
                if folderTabB:
                    exercices = exercisesB
                if folderTabC:
                    exercices = exercisesC

                filteredExercices = pagination(paginationExercises, exercices)
                renderExercices(filteredExercices)                
                
            return [pageNew, tmpLeavePage, userToRedirect]

    return [
        interactions,
        undraw,
    ]
        