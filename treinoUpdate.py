def update(email):
    arq = open("arq2.txt", "r")
    arq3 = open("users.csv", "r")
    lines3 = arq3.readlines()
    lines = arq.readlines()

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

    cont = 0

    for i in lines:
        if ("ID_"+id) in i:
            print(i)
            break
        cont += 1
        

    del lines[cont]

    new_arq = open("arq2.txt", "w+")

    for line in lines:
        new_arq.write(line)

    id = "ID_"+id

    insert = id+";"

    while True:
        ex = str(input("Insira o nome do exercício: "))
        if ex == "0" or ex == 0:
            break
        ser = str(input("Insira a quantidade de series: "))
        rep = str(input("Insira a quantidade de repetições: "))
        insert += ex+ ";"+ ser + ";"+ rep + ";"

    insert = insert.rstrip(insert[-1])

    print(insert)

    arq2 = open("arq2.txt", "a")
    arq2.write(insert+"\n")

    new_arq.close()