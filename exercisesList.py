from utils import csvLinesFormatter

def getExercises ():
    exercisesArq = open("./data/lista-exercicios.csv", "r", newline='', encoding="utf-8")
    exercisesArq.readline()
    
    exercises = csvLinesFormatter(exercisesArq.readlines())
    
    exercisesList = []

    for i in exercises:
        exercisesList.append(i)
        
    return exercisesList
        
getExercises()