arq = open("arq2.txt", "r")
arq3 = open("arq3.txt", "r")
lines = arq.readlines()
lines3 = arq3.readlines()

search = "c@gmail"

for profiles in lines3:
    if search in profiles:
        find = "ID_"+profiles[0]

for i in lines:
    if find in i:    
        temp = i.split(";")
        del temp[0]

cont = 1

new = ""

for i in temp:
    new += i+";"
    if cont%3 == 0 and cont != len(temp):
        new = new.rstrip(new[-1])
        new += "\n"
    cont+=1
        
print(new.rstrip(new[-1]))

workout = open("arq.txt", "w")
workout.write(new.rstrip(new[-1]))