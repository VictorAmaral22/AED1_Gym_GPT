from utils import csvLinesFormatter

def VerifyLogin (email, password, type):
    arq = open('./data/users.csv', 'r')
    lines = arq.readlines()
    login = False

    for i in lines:
        data = i.split(";")
        if email == data[3] and password == data[4] and data[2] == type:
            login = data[0]

    arq.close()

    return login

def userInsert(name, role, email, password, height, weight, age):
    with open("./data/users.csv", 'r') as x:
        cont = len(x.readlines())
    x.close()

    lines = open("./data/users.csv", 'r')
    lines = lines.readlines()
    validate = True

    for i in lines:
        if email in i:
            validate = False

    if validate:
        infos = ""
        infos = str(cont)+";"+name+";"+role+";"+email+";"+password+";"+height+";"+weight+";"+age+"\n"
        validate = cont
        arq = open("./data/users.csv", "a")
        arq.write(infos)

    return validate

def getUsersWithNoWorkouts ():
    usersArq = open("./data/users.csv", "r")
    workoutsArq = open("./data/treinos.csv", "r")
    usersArq.readline()
    workoutsArq.readline()

    users = csvLinesFormatter(usersArq.readlines())
    workouts = csvLinesFormatter(workoutsArq.readlines())

    # print(users)
    # print(workouts)

    usersList = []

    for user in users:
        if user[2] == "Cliente":
            hasWorkout = False

            for exercice in workouts:
                if exercice[0] == user[0]:
                    hasWorkout = True
                    break

            if not hasWorkout:
                usersList.append(user)

    # print(usersList)
    return usersList