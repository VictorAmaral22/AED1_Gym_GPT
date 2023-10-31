from render_functions import checkClick, renderImage, renderInput, renderTxt
from graphics import Text, Point
from crudTreinos import getUserExercises

folderTabA = False
folderTabB = False
folderTabC = False
arrowLeft = False
arrowRight = False
paginationExercises = 1
inputsRendered = []
exercisesList = []
exercisesA = []
exercisesB = []
exercisesC = []

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

def saveWorkout (exercises, user):
    print(exercises)
    print(user)

def CreateWorkout (win, winW, winH, idUser, page, leavePage, userViewing):
    global folderTabA
    global folderTabB
    global folderTabC
    global inputsRendered
    global exercisesList
    global exercisesA
    global exercisesB
    global exercisesC

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
    titleName = renderTxt(win, 215, 270, "#fff", "Exercício", 20)
    titleSerie = renderTxt(win, 660, 270, "#fff", "Séries", 20)
    titleRep = renderTxt(win, 850, 270, "#fff", "Repetições", 20)
    buttonSave = renderImage(win, winW-350, winH-80, "./assets/save-workout.png")

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
        itemsPerPage = 8
        limit = pageExerc * itemsPerPage
        nextLimit = (pageExerc+1) * itemsPerPage
        start = limit - itemsPerPage
        
        if arrowLeft:
            arrowLeft[2]()
            arrowLeft = False
        if arrowRight:
            arrowRight[2]()
            arrowRight = False

        if pageExerc != 1:
            arrowLeft = renderImage(win, winW/2-100, winH-60, "./assets/pagination-left.png")

        if len(exercices[(nextLimit-itemsPerPage):nextLimit]) > 0:
            arrowRight = renderImage(win, winW/2+100, winH-60, "./assets/pagination-right.png")

        return exercices[start:limit]

    filteredExercices = pagination(1, exercisesA)

    def renderExercices (filteredList):
        global inputsRendered

        for input in inputsRendered:
            input[1][0][2]()
            input[1][1][1]()
            input[2][2]()
            input[3][2]()
            input[4][2]()
        
        inputsRendered = []
        y = 350

        for exercise in filteredList:
            exerciseNameImage = renderImage(win, 350, y, "./assets/input-big.png")
            exerciseNameTxt = renderTxt(win, 350, y, "#000", exercise[3], 20)

            exerciseSerie = renderInput(win, 700, y, 10, 20, "", "#fff", "#000", True, exercise[4])            
            exerciseRep = renderInput(win, 860, y, 10, 20, "", "#fff", "#000", True, exercise[5])

            enterImage = renderImage(win, 1600, y, "./assets/trash.png")

            inputsRendered.append([
                exercise[2],
                [exerciseNameImage, exerciseNameTxt],
                exerciseSerie,
                exerciseRep,
                enterImage,
            ])
                                    
            y += 70

    renderExercices(filteredExercices)

    def undraw ():
        global inputsRendered

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

        titleName[1]()
        titleSerie[1]()
        titleRep[1]()

        for input in inputsRendered:
            input[1][0][2]()
            input[1][1][1]()
            input[2][2]()
            input[3][2]()
            input[4][2]()
    
    def interactions(mouseclick):
        global arrowLeft
        global arrowRight
        global paginationExercises
        global inputsRendered
        global exercisesList
        global exercisesA
        global exercisesB
        global exercisesC
        global folderTabA
        global folderTabB
        global folderTabC
        global filteredExercices

        if mouseclick:
            print("exercisesList",exercisesList)

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

            clickedSave = checkClick(mouseclick, buttonSave[1])

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
                # cont = 0
                # for i in range(0, len(inputsRendered)//3):
                #     exer = inputsRendered[cont][0].getText()
                #     cont+=1
                #     serie = inputsRendered[cont][0].getText()
                #     cont+=1
                #     rep = inputsRendered[cont][0].getText()
                #     cont+=1
                #     print(str(userViewing)+";"+exer+";"+serie+";"+rep)
            
            if clickedTabB:
                tabClicked(win, "B")
                filteredExercices = pagination(1, exercisesB)
                renderExercices(filteredExercices)

            if clickedTabC:
                tabClicked(win, "C")
                filteredExercices = pagination(1, exercisesC)
                renderExercices(filteredExercices)

            if clickedSave:
                saveWorkout(exercisesList, userViewing)

            for exercise in inputsRendered:
                clicked = checkClick(mouseclick, exercise[4][1])

                if clicked:
                    tmpExercisesList = []
                    for exerc in exercisesList:
                        if(exerc[2] != exercise[0]):
                            tmpExercisesList.append(exerc)

                    exercisesList = tmpExercisesList

                    if folderTabA:
                        tmpArr = filterExercises("A", tmpExercisesList)
                        exercisesA = tmpArr
                        filteredExercices = pagination(paginationExercises, tmpArr)
                    if folderTabB:
                        tmpArr = filterExercises("B", tmpExercisesList)
                        exercisesB = tmpArr
                        filteredExercices = pagination(paginationExercises, tmpArr)
                    if folderTabC:
                        tmpArr = filterExercises("C", tmpExercisesList)
                        exercisesC = tmpArr
                        filteredExercices = pagination(paginationExercises, tmpArr)

                    renderExercices(filteredExercices)
                    break               

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
        