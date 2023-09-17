name = "Vito"
age = "21"
height = "174"
weight = "85"
password = "1234"

infos = name+";"+age+";"+height+";"+weight+";"

treino = "Workout: "

workout = {
    "Dia 1": ['Peito','Ombros','Triceps'],
    "Dia 2": ['Costas', 'Biceps'],
    "Dia 3": ['Pernas'],
    "Dia 4": ['Descanso']
}

treino += "Dia 1: "

for i in workout['Dia 1']:
     treino += i+" "
treino += "| Dia 2: "
for i in workout['Dia 2']:
     treino += i+" "
treino += "| Dia 3: "
for i in workout['Dia 3']:
     treino += i+" "
treino += "| Dia 4: "
for i in workout['Dia 4']:
     treino += i+" "
treino += "\n"

data = infos + treino

print(data)

# arq = open("arq.txt", "a")
# arq.write(data)