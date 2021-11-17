# from tabla import Tabla_de_simbolos
#
# t = Tabla_de_simbolos()
#
# t.add( "numero", 19, "int")
# t.add( "caracter", 'c', "char")
#
# print(t)
def lineReader(file):
    #O(n²)
    f = open(file, encoding="utf8")
    index =0
    for linea in f:# n -> cada linea
        lienaCruda = linea.split("\n")
        cantidad = len(lienaCruda)
        lienaCruda[0].strip("\n")


        index += 1
        if len(lienaCruda) > 0:
            print(f"Linea: {index}")
            print(lienaCruda[0])
            palabras = lienaCruda[0].split(" ")
            if "(" in lienaCruda[0] and ")" in lienaCruda[0]:
                #entra cuando se crea un nuevo scope
                if  "if" in palabras or  "while" in palabras:
                    print("es un condicional o ciclo")
                else:
                    print("es una funcion")
            else:
                print("code normal")


    f.close()


lineReader("texto.txt")