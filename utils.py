def csvLinesFormatter (csvLines):
    tmpLines = []

    for line in csvLines:
        tmpLines.append(line.strip().split(";"))
    
    return tmpLines