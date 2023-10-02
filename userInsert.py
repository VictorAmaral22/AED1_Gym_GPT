def userInsert(name, role, email, password, height, weight, age):
    with open("users.csv", 'r') as x:
        cont = len(x.readlines())
    x.close()

    lines = open("users.csv", 'r')
    lines = lines.readlines()

    for i in lines:
        if email in i:
            print("O usuário deste email ja está cadastrado!")
            exit()

    infos = ""

    infos = str(cont)+";"+name+";"+role+";"+email+";"+password+";"+height+";"+weight+";"+age+"\n"

    print(infos)

    arq = open("users.csv", "a")
    arq.write(infos)