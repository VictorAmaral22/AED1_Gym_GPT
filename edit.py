def treinoSearch(idUser):
    treinos = open("./data/treinos.csv", "r", newline='', encoding="utf-8")
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

    with open("./data/treinos.csv", "r", encoding="utf-8") as treinosFile:
        treinosList = treinosFile.readlines()

    with open("./data/treinos.csv", "w", newline='', encoding="utf-8") as treinosInsert:
        toChange = ['Teste', 'Test1', 'Test2', 'Test4']

        for line in treinosList:
            contain = False
            for word in toChange:
                if word in line:
                    contain = True
                    break
            if not contain:
                treinosInsert.write(line)
            else:
                print(line)  
                
        newChange = ["2;C;Funf1;4;30","2;C;Funf2;4;30","2;C;Funf3;4;30","2;C;Funf4;4;30"]
        
    with open("./data/treinos.csv", "a", newline='', encoding="utf-8") as treinosInsert:
        for i in newChange:
            treinosInsert.write(i+"\n")
        
    if new != "":
        return True
    else: 
        return False
    
treinoSearch("2")