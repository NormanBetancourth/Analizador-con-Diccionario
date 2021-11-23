import bugChecker.VariableCkecker
from parts.funcion import Funcion
from parts.tabla import Tabla_de_simbolos



def lineReader(file, diccionario):
    f = open(file, encoding="utf8")
    index = 0
    openedNewScope = False
    pila = []
    TablaAuxiliar = Tabla_de_simbolos()
    FuncionAux = None
    for linea in f:  # n -> cada linea
        lienaCruda = linea.split("\n")
        cantidad = len(lienaCruda)
        lienaCruda[0].strip("\n")
        index += 1
        bandera = False

        if openedNewScope and len(lienaCruda) > 0:
            # while este abierto el cuerpo de la funcion ..



            palabras = lienaCruda[0].split(" ")
            palabras = [x for x in palabras if x != ""]

            for x in palabras:
                if "{" in x:
                    pila.append("{")
                if "}" in x:
                    if pila[len(pila) - 1] == "{":
                        pila.pop()
                    else:
                        pila.append("{")





            if "{" not in palabras and "}" not in palabras and len(palabras) > 0:

                if any("while" in x for x in palabras) or any("if" in x for x in palabras):
                    #print(f"======> {palabras}")
                    pass
                else:
                    if "return" in palabras and FuncionAux:

                        bugChecker.VariableCkecker.returnAnalizer(palabras, index, TablaAuxiliar.diccionario, FuncionAux.type)
                    else:
                        bugChecker.VariableCkecker.analizer(palabras, index, TablaAuxiliar.diccionario)
                        if FuncionAux:
                            FuncionAux.updateDict(TablaAuxiliar.diccionario)

            if len(pila) == 0:
                openedNewScope = False
                if FuncionAux:
                    diccionario[FuncionAux.key] = FuncionAux
                    print(FuncionAux)
                FuncionAux = None
                pila = []



        if len(lienaCruda) > 0 and lienaCruda[0] != "{" and lienaCruda[0] != "}" and openedNewScope == False:

            palabras = lienaCruda[0].split(" ")
            palabras = [x for x in palabras if x != ""]

            if len(palabras) > 0:

                if "(" in lienaCruda[0] and ")" in lienaCruda[0] and "while" not in linea[0] and "if" not in linea[0]:

                    # entra y en las proximas iteraciones va a quedarse enciclada
                    lowTail = lienaCruda[0].index("(")
                    hiTail = lienaCruda[0].index(")")

                    stringAux = lienaCruda[0][lowTail + 1:hiTail].split(",")
                    funcSTR = lienaCruda[0][:lowTail]

                    TablaAuxiliar = Tabla_de_simbolos()
                    FuncionAux = bugChecker.VariableCkecker.funcionAnalizer(funcSTR, index, diccionario,TablaAuxiliar.diccionario)


                    for kj in stringAux:
                        palabras = kj.split(" ")
                        palabras = [x for x in palabras if x != ""]
                        bugChecker.VariableCkecker.analizer(palabras, index, TablaAuxiliar.diccionario)

                    pila.append("{")
                    openedNewScope = True







                else:
                    # print(palabras)
                    bugChecker.VariableCkecker.analizer(palabras, index, diccionario)

    f.close()
