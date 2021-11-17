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
    for linea in f:
        lienaCruda = linea.split("\n")
        cantidad = len(lienaCruda)
        lienaCruda = lienaCruda[:cantidad-1]
        index += 1
        if len(lienaCruda) > 0:
            print(f"Linea: {index}")
            print(lienaCruda[0])
            print('\n')
            if "(" in lienaCruda[0] and ")" in lienaCruda[0]:
                print("es un nuevo scope")

        # if len(lienaCruda) > 0:
        #     palabra = lienaCruda[0].split(" ")
        #     for p in palabra:
        #         if len(p) > 0:
        #             print(p)

    f.close()


lineReader("texto.txt")