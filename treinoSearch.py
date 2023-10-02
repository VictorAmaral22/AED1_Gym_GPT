def treinoSearch(email):
    arq = open("arq2.txt", "r")
    arq3 = open("users.csv", "r")
    lines = arq.readlines()
    lines3 = arq3.readlines()

    id = ""
            
    for profiles in lines3:
        if email in profiles:
            for word in profiles:
                if word == ';':
                    break
                id += word
    
    if id == "":
        print("Usuário não encontrado.") 
        exit()       

    for i in lines:
        if ("ID_"+id) in i:
            find = i

    for i in lines:
        if find in i:    
            temp = i.split(";")
            del temp[0]

    cont = 1

    new = ""

    for i in temp:
        new += i+";"
        if cont%3 == 0 and cont != len(temp):
            new = new.rstrip(new[-1])
            new += "\n"
        cont+=1
            
    workout = open("arq.txt", "w")
    workout.write(new.rstrip(new[-1]))