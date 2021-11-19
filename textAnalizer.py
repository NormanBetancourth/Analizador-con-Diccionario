def lineReader(file):
    #O(n²)
    f = open(file, encoding="utf8")
    index =0
    for linea in f:# n -> cada linea
        lienaCruda = linea.split("\n")
        cantidad = len(lienaCruda)
        lienaCruda[0].strip("\n")


        index += 1
        if len(lienaCruda) > 0 and lienaCruda[0] != "{" and lienaCruda[0] != "}":

            palabras = lienaCruda[0].split(" ")
            if "(" in lienaCruda[0] and ")" in lienaCruda[0]:

                #entra cuando se crea un nuevo scope
                if  "if" in palabras or  "while" in palabras:
                    #print("es un condicional o ciclo")
                    pass
                else:
                    #print("es una funcion")
                    pass
            else:
                #print(lienaCruda[0])

                print(palabras)


    f.close()