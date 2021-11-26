import bugChecker.VariableCkecker
from parts.Condicional_Iterable import CondiIterable
from parts.funcion import Funcion
from parts.tabla import Tabla_de_simbolos


def lineReader(file, diccionario):
    f = open(file, encoding="utf8")

    # objetos auxiliares para las funciones
    debeReturn = False
    openedNewScope = False
    pila = []
    FuncionAux = None

    TablaAuxiliar = Tabla_de_simbolos()
    ObjectCondicionalFijo = None #if/ while inicial fijo

    index = 0
    # objetos auxiliares para if o while
    ScopeCondicional = False
    pilaScopeCondicional = []

    pilaAnidados = []
    # pila para ir guardando los ifs o whiles anidados y la pila con los {}
    # en una lista [if/while , pila de {}] => [ObjectCondicionalFijo, pilaScopeCondicional]

    for linea in f:  # n -> cada linea
        # limpiamos los elementos que no nos interesan de la linea de texto
        lienaCruda = linea.split("\n")
        cantidad = len(lienaCruda)
        lienaCruda[0].strip("\n")
        index += 1
        bandera = False

        if openedNewScope and len(lienaCruda) > 0:
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

            # condicional para cuando se abra un while
            if ScopeCondicional and len(palabras) > 0:
                # para ifs o whiles

                for x in palabras:
                    if "{" in x:
                        pilaScopeCondicional.append("{")
                    if "}" in x:
                        if pilaScopeCondicional[len(pilaScopeCondicional) - 1] == "{":
                            pilaScopeCondicional.pop()
                        else:
                            pilaScopeCondicional.append("{")


                if any("while" in x for x in palabras) or any("if" in x for x in palabras):

                    if any("while" in x for x in palabras):
                        typeCondicion = "while"
                    else:
                        typeCondicion = "if"

                    tablaD = ObjectCondicionalFijo.tabla_de_simbolos
                    aux = [ObjectCondicionalFijo, pilaScopeCondicional]
                    pilaAnidados.append(aux)
                    pilaScopeCondicional = ["{"]
                    # limpiamos la linea de texto
                    lowtailaux = lienaCruda[0].index("(")
                    hitailAux = lienaCruda[0].index(")")
                    parametters = lienaCruda[0][lowtailaux + 1:hitailAux]


                    # analizamos los parametros del if/while
                    bugChecker.VariableCkecker.parametterAnalizer(parametters, index,
                                                                  ObjectCondicionalFijo.tabla_de_simbolos.diccionario)
                    ObjectCondicionalFijo = CondiIterable(typeCondicion, tablaD.diccionario)

                else:
                    if "{" not in palabras and "}" not in palabras:
                        if "return" in palabras and FuncionAux:
                            # caso para analizar el return de una funcion, que este exista y que coincida con tipos, etc
                            debeReturn = False
                            bugChecker.VariableCkecker.returnAnalizer(palabras, index, ObjectCondicionalFijo.tabla_de_simbolos.diccionario,
                                                                       FuncionAux.type)
                        else:
                            print(f"~~~~~~~~~~~~~~~~~~~~~~~~{ObjectCondicionalFijo} linea ({index})")
                            # si no => es un caso de variable normal
                            bugChecker.VariableCkecker.analizer(palabras, index, ObjectCondicionalFijo.tabla_de_simbolos.diccionario)
                            print(f"~~~~~~~~~~~~~~~~~~~~~~~~{ObjectCondicionalFijo} linea ({index})")


                if len(pilaScopeCondicional) == 0 and len(pilaAnidados) > 0:
                    aux = pilaAnidados.pop()
                    ObjectCondicionalFijo = aux[0]
                    pilaScopeCondicional = aux[1]
                    pilaScopeCondicional.pop()
                    print(f"pppppppppppppppp{ObjectCondicionalFijo}")


                if len(pilaScopeCondicional) == 0 and len(pilaAnidados) == 0:
                    print(f"Salio del condicional en la linea {index}")
                    ScopeCondicional = False



            else:
                if len(palabras) > 0:
                    # condicional que abre el while
                    if any("while" in x for x in palabras) or any("if" in x for x in palabras):
                        print(f"======> {lienaCruda[0]}")
                        condition = ""
                        if any("while" in x for x in palabras):
                            condition = "while"
                        else:
                            condition = "if"
                        #limpiamos la linea de texto
                        lowtail = lienaCruda[0].index("(")
                        hitail = lienaCruda[0].index(")")
                        parametrosCondicion = lienaCruda[0][lowtail + 1:hitail]

                        #actualizamos las variables de la funcion
                        if FuncionAux:
                            FuncionAux.updateDict(TablaAuxiliar.diccionario)
                        #analizamos los parametros del if/while
                        bugChecker.VariableCkecker.parametterAnalizer(parametrosCondicion, index, FuncionAux.tabla_de_simbolos.diccionario)

                        ObjectCondicionalFijo = CondiIterable(condition, FuncionAux.tabla_de_simbolos.diccionario)



                        # activamos la condicion de condicional
                        ScopeCondicional = True
                        # metemos el objeto a la pila  para ver en que momento cierra
                        pilaScopeCondicional.append("{")

                    else:
                        if "{" not in palabras and "}" not in palabras:
                            if "return" in palabras and FuncionAux:
                                # caso para analizar el return de una funcion, que este exista y que coincida con tipos, etc
                                debeReturn = False
                                bugChecker.VariableCkecker.returnAnalizer(palabras, index, TablaAuxiliar.diccionario,
                                                                          FuncionAux.type)
                            else:
                                # si no => es un caso de variable normal
                                bugChecker.VariableCkecker.analizer(palabras, index, TablaAuxiliar.diccionario)
                                if FuncionAux:
                                    # si la funcion auxiliar != None => actualize los objetos que se sacaron del
                                    # archivo y metalos a la tabla de simbolos de la funcion actual
                                    FuncionAux.updateDict(TablaAuxiliar.diccionario)


            # ver cuando se cierra la pila de {}, si es asi,
            # el cuerpo de la funcion ha terminado
            if len(pila) == 0:
                if debeReturn:
                    print(f"La funcion debe retornar un valor (linea {index - 1})")

                openedNewScope = False
                if FuncionAux:
                    diccionario[FuncionAux.key] = FuncionAux
                    print(f"-->{FuncionAux}")
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

                    if "void" not in funcSTR:
                        debeReturn = True
                    FuncionAux = bugChecker.VariableCkecker.funcionAnalizer(funcSTR, index, diccionario,
                                                                            TablaAuxiliar.diccionario)

                    if len(stringAux) > 0 and stringAux[0] != "":
                        for kj in stringAux:
                            palabras = kj.split(" ")
                            palabras = [x for x in palabras if x != ""]
                            if len(palabras) > 0:
                                bugChecker.VariableCkecker.analizer(palabras, index, TablaAuxiliar.diccionario)

                    pila.append("{")
                    openedNewScope = True

                else:
                    # print(palabras)
                    bugChecker.VariableCkecker.analizer(palabras, index, diccionario)

    f.close()
