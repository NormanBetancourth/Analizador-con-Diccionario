import bugChecker.VariableCkecker


def lineReader(file, diccionario):
    #O(n²)
    f = open(file, encoding="utf8")
    index =0
    openedNewScope = False
    pila = []
    for linea in f:# n -> cada linea
        lienaCruda = linea.split("\n")
        cantidad = len(lienaCruda)
        lienaCruda[0].strip("\n")
        index += 1

        if openedNewScope and len(palabras) > 0:
            # while este abierto el cuerpo de la funcion ...
            print(f"campo de scope en la linea {index}")
            palabras = lienaCruda[0].split(" ")
            palabras = [x for x in palabras if x != ""]

            doPop = False
            for x in palabras:
                if "{" in x:
                    pila.append("{")
                if "}" in x:
                    if pila[len(pila) - 1] == "{":
                        pila.pop()
                    else:
                        pila.append("{")

            if len(pila) == 0:
                print("-----------se cierra la pila------------")
                openedNewScope = False







        if len(lienaCruda) > 0 and lienaCruda[0] != "{" and lienaCruda[0] != "}" and openedNewScope == False:

            palabras = lienaCruda[0].split(" ")
            palabras = [x for x in palabras if x != ""]



            if len(palabras) >0:

                if "(" in lienaCruda[0] and ")" in lienaCruda[0] and "while" not in linea[0] and "if" not in linea[0]  :

                    #entra y en las proximas iteraciones va a quedarse enciclada
                    openedNewScope = True
                    pila.append("{")
                    # entra cuando se crea un nuevo scope
                    if "if" in palabras or "while" in palabras:
                        #condicional o while
                        print(palabras)
                    else:
                        print(palabras)
                        #funcion

                else:
                    #print(palabras)
                    bugChecker.VariableCkecker.analizer(palabras, index, diccionario)


    f.close()