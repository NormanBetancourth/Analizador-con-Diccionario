import bugChecker.VariableCkecker


def lineReader(file, diccionario):
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
                    pass
                    #print("es un condicional o ciclo")

                else:
                    pass
                    #print("es una funcion")

            else:
                print(palabras)
                bugChecker.VariableCkecker.analizer(palabras, index, diccionario)




    f.close()