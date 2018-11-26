name = input("Enter your name:")
names = ""

for x in range(len(name)):
    char = name[x]

    if char == "A":
       names += "B"
    elif char == "B":
        names += "C"
    elif char == "C":
        names += "D"
    elif char == "D":
        names += "E"
    elif char == "E":
        names += "F"
    elif char == "F":
        names += "G"
    elif char == "G":
        names += "H"
    elif char == "H":
        names += "I"
    elif char == "I":
        names += "J"
    elif char == "J":
        names += "K"
    elif char == "K":
        names += "L"
    elif char == "L":
        names += "M"
    elif char == "M":
        names += "N"
    elif char == "N":
        names += "O"
    elif char == "O":
        names += "P"
    elif char == "P":
        names += "Q"
    elif char == "Q":
        names += "R"
    elif char == "R":
        names += "S"
    elif char == "S":
        names += "T"
    elif char == "T":
        names += "U"
    elif char == "U":
        names += "V"
    elif char == "V":
        names+= "W"
    elif char == "W":
        names += "X"
    elif char == "X":
        names += "Y"
    elif char == "Y":
        names += "Z"
    elif char == "Z":
        random += "A"
    else:
        names+= char

print(names)
