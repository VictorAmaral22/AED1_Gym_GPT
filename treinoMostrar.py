import webbrowser
import os

def createHTML():
    arq = open("ficha.csv", "r")
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

    header = '''<head>
        <link rel="stylesheet" href="style.css">
    </head>
    <html>
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