with open("arq3.txt", 'r') as x:
    cont = len(x.readlines())
x.close()
    
arq = open("arq3.txt", 'r')
arq2 = open("arq2.txt", 'r')
lines2 = arq2.readlines()
lines = arq.readlines()

search = "c@gmail"

for i in lines:
    if search in i:  
        test = i.split(";")
        test = test[0]

for k in lines2:
    if "ID_"+test in k:
        print("Este usuário ja possuí um treino!")
        exit()
        
id = "ID_"+str(cont)


insert = id+";"

while True:
    ex = str(input("Insira o nome do exercício: "))
    if ex == "0" or ex == 0:
        break
    rep = str(input("Insira a quantidade de series e repetiçoes (ex: 3x10): "))
    carga = str(input("Insira a carga em Kilograma (ex: 10Kg): "))
    insert += ex+ ";"+ rep + ";"+ carga + ";"

insert = insert.rstrip(insert[-1])
insert += "\n"

print(insert)

arq2 = open("arq2.txt", "a")
arq2.write(insert)