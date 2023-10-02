def treinoSearch(idUser):
    treinos = open("treinos.csv", "r")
    treinos.readline()
    treinosList = treinos.readlines()

    ficha = []
    for exerc in treinosList:
        formated = exerc.split(";")

        if formated[0] == str(idUser):
            formated[-1] = "".join(formated[-1].split("\n"))
            ficha.append(formated)

    new = ""

    for i in ficha:
        new += ";".join(i)+"\n"
            
    workout = open("ficha.csv", "w")
    workout.write(new)

    if new != "":
        return True
    else: 
        return False
        

# treinoSearch(2)