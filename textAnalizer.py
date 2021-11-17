def lineReader(file):
    file = open(file, "r")
    for i in file:
        a = i.split(' ', '\n')
        print(a)
    file.close()


lineReader("texto.txt")