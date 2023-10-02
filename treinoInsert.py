def treinoInsert(email):
    arq = open("users.csv", 'r')
    arq2 = open("treinosAluno.csv", 'r')
    lines2 = arq2.readlines()
    lines = arq.readlines()

    test = ""

    for i in lines:
        if email in i:
            for word in i:
                if word == ';':
                    break
                test += word
            
    for k in lines2:
        if "ID_"+test in k:
            print("Este usuário ja possuí um treino!")
            exit()
            
    id = "ID_"+test

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

    arq2 = open("treinosAluno.csv", "a")
    arq2.write(insert+"\n")