from render_functions import checkClick, renderImage, renderInput, renderTxt
from graphics import Text, Point
from crudTreinos import getUserExercises, treinoInsert, getAllExercises

folderTabA = False
folderTabB = False
folderTabC = False
folderTabNew = False
arrowLeft = False
arrowRight = False
paginationExercises = 1
inputsRendered = []
inputsRenderedNew = []
exercisesList = []
exercisesA = []
exercisesB = []
exercisesC = []
allExercises = []
buttonAdd = False
buttonSave = False

def tabClicked (win, tab):
        global folderTabA
        global folderTabB
        global folderTabC
        global folderTabNew
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
        if folderTabNew:
            folderTabNew[2]()
            folderTabNew = False
        
        if tab == "A":
            folderTabA = renderImage(win, 215, 192, "./assets/treino-a-active.png")
            page = 1
        if tab == "B":            
            folderTabB = renderImage(win, 460, 192, "./assets/treino-b-active.png")
            page = 1
        if tab == "C":
            folderTabC = renderImage(win, 705, 192, "./assets/treino-c-active.png")
            page = 1
        if tab == "new":
            folderTabNew = renderImage(win, 459, 192, "./assets/treinos-folder.png")
            page = 1

def renderExercices (win, filteredList, add=False):
    global inputsRendered
    global inputsRenderedNew

    for input in inputsRendered:
        input[1][0][2]()
        input[1][1][1]()
        input[2][2]()
        input[3][2]()
        input[4][2]()
    
    for input in inputsRenderedNew:
        input[1][0][2]()
        input[1][1][1]()
        input[2][2]()
    
    inputsRendered = []
    inputsRenderedNew = []
    y = 350

    for exercise in filteredList:
        if not add:
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
        else:
            exerciseNameImage = renderImage(win, 350, y, "./assets/input-big.png")
            exerciseNameTxt = renderTxt(win, 350, y, "#000", exercise[1], 20)
            enterImage = renderImage(win, 600, y, "./assets/plus.png")

            inputsRenderedNew.append([
                exercise[0],
                [exerciseNameImage, exerciseNameTxt],
                enterImage
            ])

        y += 70

def filterExercises (workout, list):
    filtered = []
    for exercise in list:
        if exercise[1] == workout:
            filtered.append(exercise)

    return filtered

def pagination (win, winW, winH, pageExerc, exercices):
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

def updateExercises (win, winW, winH, userViewing):
    global inputsRendered
    global exercisesList
    global exercisesA
    global exercisesB
    global exercisesC
    global paginationExercises
    global filteredExercices

    for input in inputsRendered:
        for exercise in exercisesList:
            if exercise[2] == input[0]:
                exercise[4] = input[2][0].getText()
                exercise[5] = input[3][0].getText()

    if folderTabA:
        tmpArr = filterExercises("A", exercisesList)
        exercisesA = tmpArr
        filteredExercices = pagination(win, winW, winH, paginationExercises, tmpArr)
    if folderTabB:
        tmpArr = filterExercises("B", exercisesList)
        exercisesB = tmpArr
        filteredExercices = pagination(win, winW, winH, paginationExercises, tmpArr)
    if folderTabC:
        tmpArr = filterExercises("C", exercisesList)
        exercisesC = tmpArr
        filteredExercices = pagination(win, winW, winH, paginationExercises, tmpArr)

    renderExercices(win, filteredExercices)
    treinoInsert(userViewing, exercisesList)

def CreateWorkout (win, winW, winH, idUser, page, leavePage, userViewing):
    global folderTabA
    global folderTabB
    global folderTabC
    global folderTabNew
    global inputsRendered
    global exercisesList
    global exercisesA
    global exercisesB
    global exercisesC
    global allExercises
    global buttonAdd
    global buttonSave

    allExercises = getAllExercises()
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
    buttonAdd = renderImage(win, winW-350, 270, "./assets/plus.png")
    buttonSave = renderImage(win, 350, winH-60, "./assets/save-workout.png")

    filteredExercices = []
    
    exercisesA = filterExercises("A", exercisesList)
    exercisesB = filterExercises("B", exercisesList)
    exercisesC = filterExercises("C", exercisesList)

    filteredExercices = pagination(win, winW, winH, 1, exercisesA)   

    renderExercices(win, filteredExercices)

    def undraw ():
        global inputsRendered

        bgImage[2]()
        logo[2]()
        folderExercices[2]()
        folderTop[2]()
        buttonAdd[2]()
        buttonReturn[2]()
        buttonSave[2]()
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

        for input in inputsRenderedNew:
            input[1][0][2]()
            input[1][1][1]()
            input[2][2]()
    
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
        global folderTabNew
        global filteredExercices
        global allExercises
        global buttonAdd
        global buttonSave

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
            clickedTabNew = checkClick(mouseclick, buttonAdd[1])
            
            clickedSave = checkClick(mouseclick, [
                Point(225.0, 916.0),
                Point(474.0, 960.0)
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
                filteredExercices = pagination(win, winW, winH, 1, exercisesA)
                renderExercices(win, filteredExercices)
            
            if clickedTabB:
                tabClicked(win, "B")
                filteredExercices = pagination(win, winW, winH, 1, exercisesB)
                renderExercices(win, filteredExercices)

            if clickedTabC:
                tabClicked(win, "C")
                filteredExercices = pagination(win, winW, winH, 1, exercisesC)
                renderExercices(win, filteredExercices)
            
            if clickedTabNew:
                tabClicked(win, "new")
                
                ids = []
                for exercise in exercisesList:
                    ids.append(exercise[2])

                tmpAllExercises = []
                for exercise in allExercises:
                    if exercise[0] not in ids:
                        tmpAllExercises.append(exercise)

                allExercises = tmpAllExercises
                        
                filteredExercices = pagination(win, winW, winH, 1, tmpAllExercises)
                renderExercices(win, filteredExercices, True)
                buttonSave[2]()
                titleSerie[1]()
                titleRep[1]()

            if clickedSave and not folderTabNew:
                updateExercises(win, winW, winH, userViewing)

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
                        filteredExercices = pagination(win, winW, winH, paginationExercises, tmpArr)
                    if folderTabB:
                        tmpArr = filterExercises("B", tmpExercisesList)
                        exercisesB = tmpArr
                        filteredExercices = pagination(win, winW, winH, paginationExercises, tmpArr)
                    if folderTabC:
                        tmpArr = filterExercises("C", tmpExercisesList)
                        exercisesC = tmpArr
                        filteredExercices = pagination(win, winW, winH, paginationExercises, tmpArr)

                    renderExercices(win, filteredExercices)
                    break    

            for exercise in inputsRenderedNew:
                clicked = checkClick(mouseclick, exercise[2][1])

                if clicked:
                    exerciseToAdd = False
                    for exerc in allExercises:
                        if(exerc[0] == exercise[0]):
                            exerciseToAdd = exerc
                            break
                    
                    exercisesList.append([
                        userViewing, exerciseToAdd[2], exerciseToAdd[0], exerciseToAdd[1], "4", "12"
                    ])
                    
                    paginationExercises = 1
                    
                    if exerciseToAdd[2] == "A":
                        tabClicked(win, "A")
                        tmpArr = filterExercises("A", exercisesList)
                        exercisesA = tmpArr
                        tmpFiltered = pagination(win, winW, winH, paginationExercises, tmpArr)
                        filteredExercices = tmpFiltered
                        renderExercices(win, tmpFiltered)
                    if exerciseToAdd[2] == "B":
                        tabClicked(win, "B")
                        tmpArr = filterExercises("B", exercisesList)
                        exercisesB = tmpArr
                        tmpFiltered = pagination(win, winW, winH, paginationExercises, tmpArr)
                        filteredExercices = tmpFiltered
                        renderExercices(win, tmpFiltered)
                    if exerciseToAdd[2] == "C":
                        tabClicked(win, "C")
                        tmpArr = filterExercises("C", exercisesList)
                        exercisesC = tmpArr
                        tmpFiltered = pagination(win, winW, winH, paginationExercises, tmpArr)
                        filteredExercices = tmpFiltered
                        renderExercices(win, tmpFiltered)

                    buttonSave[3]()
                    titleSerie[2]()
                    titleRep[2]()
                    allExercises = getAllExercises()
                    
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
                if folderTabNew:
                    exercices = allExercises

                filteredExercices = pagination(win, winW, winH, paginationExercises, exercices)
                if folderTabNew:
                    renderExercices(win, filteredExercices, True)
                else:
                    renderExercices(win, filteredExercices)
                
            return [pageNew, tmpLeavePage, userToRedirect]

    return [
        interactions,
        undraw,
    ]
        