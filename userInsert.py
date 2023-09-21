with open("arq3.txt", 'r') as x:
    cont = len(x.readlines())
x.close()

infos = ""

name = "Vito"
role = "Cliente"
email = "c@gmail"
password = "154894"
height = "179"
weight = "65"
age = "21"

infos = str(cont+1)+";"+name+";"+role+";"+email+";"+password+";"+height+";"+weight+";"+age+"\n"

print(infos)

arq = open("arq3.txt", "a")
arq.write(infos)