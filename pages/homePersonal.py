from render_functions import checkClick, renderImage, renderInput, renderTxt
from graphics import Text, Point
from crudUsers import getUsersWithNoWorkouts, getUsersWithWorkouts

folderTabNoWorkout = False
folderTabWorkout = False
arrowLeft = False
arrowRight = False
paginationUsers = 1
inputsRendered = []

def tabClicked (win, tab):
        global folderTabNoWorkout
        global folderTabWorkout
        global page
        
        if folderTabNoWorkout:
            folderTabNoWorkout[2]()
            folderTabNoWorkout = False
        if folderTabWorkout:
            folderTabWorkout[2]()
            folderTabWorkout = False
        
        if tab == "NoWorkout":
            folderTabNoWorkout = renderImage(win, 327, 190, "./assets/users-no-workout-tab.png")
            page = 1
        if tab == "Workout":            
            folderTabWorkout = renderImage(win, 796, 190, "./assets/users-w-workout-tab.png")
            page = 1

def HomePersonal (win, winW, winH, idUser, page, leavePage):
    global folderTabNoWorkout
    
    bgImage = renderImage(win, winW/2, winH/2, "./assets/background.png")
    logo = renderImage(win, 110, 40, "./assets/logo-small.png")
    buttonReturn = renderImage(win, 30, 40, "./assets/arrow-left.png")
    title = renderTxt(win, 500, 40, "#fff", "Escolha um cliente para gerenciar", 30)

    folderUsers = renderImage(win, winW/2, winH/2+100, "./assets/exercices_folder.png")
    folderTop = renderImage(win, 563, 190, "./assets/users-tab.png")
    folderTabNoWorkout = renderImage(win, 327, 190, "./assets/users-no-workout-tab.png")

    titleNome = renderTxt(win, 180, 270, "#fff", "Nome", 20)
    titleEmail = renderTxt(win, 620, 270, "#fff", "Email", 20)
    titleHeight = renderTxt(win, 1070, 270, "#fff", "Altura", 20)
    titleWeight = renderTxt(win, 1240, 270, "#fff", "Peso", 20)
    titleAge = renderTxt(win, 1420, 270, "#fff", "Idade", 20)

    usersWithNoWorkouts = getUsersWithNoWorkouts()
    usersWithWorkouts = getUsersWithWorkouts()
    
    def pagination (pageUsers, users):
        global arrowLeft
        global arrowRight
        itemsPerPage = 8
        limit = pageUsers * itemsPerPage
        nextLimit = (pageUsers+1) * itemsPerPage
        start = limit - itemsPerPage
        
        if arrowLeft:
            arrowLeft[2]()
            arrowLeft = False
        if arrowRight:
            arrowRight[2]()
            arrowRight = False

        if pageUsers != 1:
            arrowLeft = renderImage(win, winW/2-100, winH-60, "./assets/pagination-left.png")

        if len(users[(nextLimit-itemsPerPage):nextLimit]) > 0:
            arrowRight = renderImage(win, winW/2+100, winH-60, "./assets/pagination-right.png")

        return users[start:limit]

    filteredUsers = pagination(1, usersWithNoWorkouts)

    def renderUsers (filteredList):
        global inputsRendered

        for input in inputsRendered:
            for img in input[0]:
                img[2]()
            for txt in input[1]:
                txt[1]()
            input[2][2]()

        inputsRendered = []
        y = 350

        for user in filteredList:
            nameImage = renderImage(win, 350, y, "./assets/input-big.png")
            nameTxt = renderTxt(win, 350, y, "#000", user[1], 20)
            
            emailImage = renderImage(win, 800, y, "./assets/input-big.png")
            emailTxt = renderTxt(win, 800, y, "#000", user[3], 20)

            heightImage = renderImage(win, 1110, y, "./assets/input-small.png")
            heightTxt = renderTxt(win, 1110, y, "#000", user[5], 20)

            weightImage = renderImage(win, 1285, y, "./assets/input-small.png")
            weightTxt = renderTxt(win, 1285, y, "#000", user[6], 20)

            ageImage = renderImage(win, 1460, y, "./assets/input-small.png")
            ageTxt = renderTxt(win, 1460, y, "#000", user[7], 20)            
            
            enterImage = renderImage(win, 1600, y, "./assets/open.png")

            inputsRendered.append([
                [nameImage, emailImage, heightImage, weightImage, ageImage],
                [nameTxt, emailTxt, heightTxt, weightTxt, ageTxt],
                enterImage
            ])

            y += 70

    renderUsers(filteredUsers)

    def undraw ():
        bgImage[2]()
        logo[2]()
        buttonReturn[2]()
        title[1]()
        folderUsers[2]()
        folderTop[2]()
        titleNome[1]()
        titleEmail[1]()
        titleHeight[1]()
        titleWeight[1]()
        titleAge[1]()

        if folderTabNoWorkout:
            folderTabNoWorkout[2]()
        if folderTabWorkout:
            folderTabWorkout[2]()
        if arrowLeft:
            arrowLeft[2]()
        if arrowRight:
            arrowRight[2]()

        for input in inputsRendered:
            for img in input[0]:
                img[2]()
            for txt in input[1]:
                txt[1]()
            input[2][2]()
        

    def interactions(mouseclick):
        global arrowLeft
        global arrowRight
        global paginationUsers
        global inputsRendered

        if mouseclick:
            exit = checkClick(mouseclick, buttonReturn[1])
            pageNew = page
            tmpLeavePage = leavePage
            userToRedirect = False

            if exit:
                undraw()
                pageNew = "initial"
                tmpLeavePage = True

            clickedTabNoWorkout = checkClick(mouseclick, [
                Point(94.0, 160.0),
                Point(562.0, 224.0)
            ])
            clickedTabWorkout = checkClick(mouseclick, [
                Point(566.0, 160.0),
                Point(1032.0, 224.0)
            ])

            if clickedTabNoWorkout:
                tabClicked(win, "NoWorkout")
                filteredExercices = pagination(1, usersWithNoWorkouts)
                renderUsers(filteredExercices)
            
            if clickedTabWorkout:
                tabClicked(win, "Workout")
                filteredExercices = pagination(1, usersWithWorkouts)
                renderUsers(filteredExercices)

            paginationLeft = False
            if arrowLeft:
                paginationLeft = checkClick(mouseclick, arrowLeft[1])

            paginationRight = False
            if arrowRight:
                paginationRight = checkClick(mouseclick, arrowRight[1])


            if paginationLeft or paginationRight:
                if paginationLeft:
                    paginationUsers -= 1
                if paginationRight:
                    paginationUsers += 1

                exercices = []
                if folderTabNoWorkout:
                    exercices = usersWithNoWorkouts
                if folderTabWorkout:
                    exercices = usersWithWorkouts

                filteredExercices = pagination(paginationUsers, exercices)
                renderUsers(filteredExercices)         
            
            c = 0
            for user in inputsRendered:
                clicked = checkClick(mouseclick, user[2][1])

                if clicked:
                    undraw()
                    pageNew = "create-workout"
                    tmpLeavePage = True

                    if folderTabNoWorkout:
                        userToRedirect = usersWithNoWorkouts[c][0]
                    if folderTabWorkout:
                        userToRedirect = usersWithWorkouts[c][0]


                c += 1
            
            return [pageNew, tmpLeavePage, userToRedirect]

    return [
        interactions,
        undraw,
    ]
        