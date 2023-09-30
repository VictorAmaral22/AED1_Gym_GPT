def VerifyLogin (email, password, type):
    arq = open('arq3.txt', 'r')
    lines = arq.readlines()
    login = False

    for i in lines:
        data = i.split(";")
        if email == data[3] and password == data[4] and data[2] == type:
            login = True

    arq.close()

    return login