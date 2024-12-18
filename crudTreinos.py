import webbrowser
import os
from utils import csvLinesFormatter

def treinoInsert(id, newExercises):
    arq = open("./data/treinos.csv", 'r', newline='', encoding="utf-8")
    heading = arq.readline()
    lines = arq.readlines()
    lines = csvLinesFormatter(lines)

    tmpLines = []
    for row in lines:
        if row[0] != id:
            tmpLines.append(";".join(row))

    for row in newExercises:
        tmpLines.append(";".join(row))
    
    tmpLines = "\n".join(tmpLines)

    arq2 = open("./data/treinos.csv", "w", newline='', encoding="utf-8")
    arq2.write(heading+tmpLines+"\n")
    arq2.close()

def createHTML():
    arq = open("./data/ficha.csv", "r", newline='', encoding="utf-8")
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
        for exerc in treino[3:]:
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
        for exerc in treino[3:]:
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
        for exerc in treino[3:]:
            content += f"<td>{exerc.strip()}</td>\n"
        content += "</tr>\n"
    content += "</table>"
        
    footer = '''
        </body>
    </html>'''

    data = header+content+footer

    html = open("index.html", "w", newline='', encoding="utf-8")
    html.write(data)
    webbrowser.open('file://' + os.path.realpath("index.html"))

def treinoSearch(idUser):
    treinos = open("./data/treinos.csv", "r", newline='', encoding="utf-8")
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
            
    workout = open("./data/ficha.csv", "w", newline='', encoding="utf-8")
    workout.write(new)

    if new != "":
        return True
    else: 
        return False
    
def update(email):
    arq = open("treinosAluno.csv", "r", newline='', encoding="utf-8")
    arq3 = open("./data/users.csv", "r", newline='', encoding="utf-8")
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

            break
        cont += 1
        

    del lines[cont]

    new_arq = open("treinosAluno.csv", "w+", newline='', encoding="utf-8")

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

    arq2 = open("treinosAluno.csv", "a", newline='', encoding="utf-8")
    arq2.write(insert+"\n")

    new_arq.close()

def getRoutineExercises (day):
    # day = "A", "B" ou "C"
    arq = open("./data/lista-exercicios.csv", "r", newline='', encoding="utf-8")
    arq.readline()
    lines = csvLinesFormatter(arq.readlines())

    exercises = []

    for exerc in lines:
        if exerc[2] == day:
            exercises.append(exerc)

    return exercises

def getAllExercises ():
    exercises = []
    arq = open("./data/lista-exercicios.csv", "r", newline='', encoding="utf-8")
    arq.readline()
    exercises = csvLinesFormatter(arq.readlines())
    
    return exercises

def getUserExercises (idUser):
    hasWorkout = treinoSearch(idUser)
    exercises = []

    if hasWorkout:
        arq = open("./data/ficha.csv", "r", newline='', encoding="utf-8")
        exercises = csvLinesFormatter(arq.readlines())
    return exercises