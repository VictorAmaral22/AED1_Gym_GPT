def VerifyLogin (email, password, type):
    arq = open('users.csv', 'r')
    lines = arq.readlines()
    login = False

    for i in lines:
        data = i.split(";")
        if email == data[3] and password == data[4] and data[2] == type:
            login = data[0]

    arq.close()

    return login