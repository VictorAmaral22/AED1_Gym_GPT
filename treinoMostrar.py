arq = open("arq.txt", "r")
line = arq.readlines()

header = '''<head>
    <link rel="stylesheet" href="style.css">
</head>
<html>
    <body>
        <table>\n'''

content = ""

content += '''<thead>
<th>Exericio</td>
<th>Repeticoes</td>
<th>Carga</td>
</thead>\n'''

for i in line :
    temp = i.split(';')
    
    content += "<tr>\n"
    
    for l in temp:
        content += f"<td>{l.strip()}</td>\n"
        
    content += "</tr>\n"
     
footer = '''</table>
    </body>
</html>'''

data = header+content+footer

html = open("index.html", "w")
html.write(data)