def userInsert(name, role, email, password, height, weight, age):
    with open("users.csv", 'r') as x:
        cont = len(x.readlines())
    x.close()

    lines = open("users.csv", 'r')
    lines = lines.readlines()
    validate = True

    for i in lines:
        if email in i:
            validate = False

    if validate:
        infos = ""
        infos = str(cont)+";"+name+";"+role+";"+email+";"+password+";"+height+";"+weight+";"+age+"\n"
        validate = cont
        arq = open("users.csv", "a")
        arq.write(infos)

    return validate