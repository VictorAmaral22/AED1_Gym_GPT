import webbrowser
import os
from utils import csvLinesFormatter

def treinoInsert(email):
    arq = open("./data/users.csv", 'r')
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

def createHTML():
    arq = open("./data/ficha.csv", "r")
    ficha = arq.readlines()
    treinoA = []
    treinoB = []
    treinoC = []
    for exerc in ficha:
        temp = "".join(exerc.split("\n")).split(';')
        if temp[1] == "A":
            treinoA.append(temp)
        if temp[1] == "B":
            treinoB.append(temp) 
        if temp[1] == "C":
            treinoC.append(temp) 

    header = '''<!DOCTYPE html>
        <html lang="pt-br">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="style.css">
            <title>Ficha de treino</title>
        </head>
        <body>
    '''
    
    content = '''
        <h1>Treino A</h1>
        <table>
            <thead>
                <th>Exericio</td>
                <th>Séries</td>
                <th>Repetições</td>
            </thead>'''
    for treino in treinoA:
        content += "<tr>\n"
        for exerc in treino[2:]:
            content += f"<td>{exerc.strip()}</td>\n"
        content += "</tr>\n"
    content += "</table>"

    content += '''
        <h1>Treino B</h1>
        <table>
            <thead>
                <th>Exericio</td>
                <th>Séries</td>
                <th>Repetições</td>
            </thead>'''
    for treino in treinoB:
        content += "<tr>\n"
        for exerc in treino[2:]:
            content += f"<td>{exerc.strip()}</td>\n"
        content += "</tr>\n"
    content += "</table>"

    content += '''
        <h1>Treino C</h1>
        <table>
            <thead>
                <th>Exericio</td>
                <th>Séries</td>
                <th>Repetições</td>
            </thead>'''
    for treino in treinoC:
        content += "<tr>\n"
        for exerc in treino[2:]:
            content += f"<td>{exerc.strip()}</td>\n"
        content += "</tr>\n"
    content += "</table>"
        
    footer = '''
        </body>
    </html>'''

    data = header+content+footer

    html = open("index.html", "w")
    html.write(data)
    webbrowser.open('file://' + os.path.realpath("index.html"))

def treinoSearch(idUser):
    treinos = open("./data/treinos.csv", "r")
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
            
    workout = open("./data/ficha.csv", "w")
    workout.write(new)

    if new != "":
        return True
    else: 
        return False
    
def update(email):
    arq = open("treinosAluno.csv", "r")
    arq3 = open("./data/users.csv", "r")
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
        if id in i:
            print(i)
            break
        cont += 1
        

    del lines[cont]

    new_arq = open("treinosAluno.csv", "w+")

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

    arq2 = open("treinosAluno.csv", "a")
    arq2.write(insert+"\n")

    new_arq.close()

def getRoutineExercises (day):
    # day = "A", "B" ou "C"
    arq = open("./data/lista-exercicios.csv", "r")
    arq.readline()
    lines = csvLinesFormatter(arq.readlines())

    exercises = []

    for exerc in lines:
        if exerc[2] == day:
            exercises.append(exerc)

    return exercises