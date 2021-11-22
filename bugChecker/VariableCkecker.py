# Analiza si una sentencia (linea de texto es valida)
# Documentacion y tipos de errores ->
# https://mint-mine-d87.notion.site/Errores-98f348b9da8d4a1e9f134cfccdd79d92
from parts.Variable import Variable
from parts.funcion import Funcion

dataTypes = ["int", "float", "string"]
symbols = ["+", "-", "=", "/", "*"]
errorTypes = {1: "variable sin declaracion previa",
              2: "la asignacion es incorrecta",
              3: "valor esperado despues de tipo de dato",
              4: "valor esperado despues del '=' ",
              5: "palabra clave reservada",
              6: "se esperaba un salto de linea",
              7: " redeclaracion de la variable"
              }


def analizerVariablesPreDDeclaradas(linea, numeroLinea, diccionario, key):
    if len(linea) <= 2:
        # error de asignacion incorrecta
        print(f"Error de sintaxis: {errorTypes[2]} en la linea {numeroLinea}")
        return

    if linea[1] == "=":
        tipoDato = diccionario[key].type

        if tipoDato == "int":
            bandera = True
            for i in range(2, len(linea)):
                if linea[i] not in diccionario:
                    if linea[i] not in symbols:
                        valor = linea[i].replace("-", "").replace("+", "")
                        if not valor.isnumeric():
                            bandera = False
                            break
                        else:
                            if linea[i - 1] not in symbols:
                                bandera = False
                                break
                    else:
                        if i == len(linea) - 1:
                            bandera = False
                            break
                else:  # si esta en el diccionario
                    if diccionario[linea[i]].type != "int":
                        bandera = False
                        break
                    else:
                        if linea[i - 1] not in symbols:
                            bandera = False
                            break
            if not bandera:
                print(f"Error de sintaxis: error de asignacion en la linea {numeroLinea}")
                return
            else:
                diccionario[key].value = linea[2]
                return

        if tipoDato == "float":
            bandera = True
            for i in range(2, len(linea)):
                if linea[i] not in diccionario:
                    if linea[i] not in symbols:
                        valor = linea[i].replace(".", "").replace("-", "").replace("+", "")
                        if not valor.isnumeric():
                            bandera = False
                            break
                        else:
                            if linea[i - 1] not in symbols:
                                bandera = False
                                break
                    else:
                        if i == len(linea) - 1:
                            bandera = False
                            break
                else:  # si esta en el diccionario
                    if diccionario[linea[i]].type == "string":
                        bandera = False
                        break
                    else:
                        if linea[i - 1] not in symbols:
                            bandera = False
                            break
            if not bandera:
                print(f"Error de sintaxis: error de asignacion en la linea {numeroLinea}")
                return
            else:
                diccionario[key].value = linea[2]
                return

        if tipoDato == "string":
            bandera = True
            for i in range(2, len(linea)):
                if linea[i] not in diccionario:
                    if linea[i] != "+":
                        string = linea[i]
                        if string[0] != chr(34) or string[len(string) - 1] != chr(34):
                            bandera = False
                            break
                        else:
                            if linea[i - 1] not in symbols:
                                bandera = False
                                break
                    else:
                        if linea[i - 1] in symbols:
                            bandera = False
                            break
                        else:
                            if i == len(linea) - 1:
                                bandera = False
                                break
                else:  # si esta en el diccionario
                    if diccionario[linea[i]].type != "string":
                        bandera = False
                        break
            if not bandera:
                print(f"Error de sintaxis: error de asignacion en la linea {numeroLinea}")
                return
            else:
                diccionario[key].value = linea[2]
                return

    else:
        # caso de que no sea valor y sea una var que no esta en el diccionario
        print(f"Error de sintaxis: se esperaba un '=' en la linea {numeroLinea}")


def analizerVariablesNODeclaradas(linea, numeroLinea, diccionario, key, tipoDato):
    if linea[1] in diccionario:  # redeclaracion de variable
        print(f"Error de sintaxis: redeclaracion de la variable {linea[1]} en la linea {numeroLinea}")
        return
    else:  # creamos nueva variable
        if len(linea) > 2:  # declaracion y asignacion (int x = value)

            # evita -> tipo tipo = ...
            if linea[1] in dataTypes:
                print(f"Error de sintaxis: mal uso palabra reservada {linea[1]} en la linea {numeroLinea}")
                return

            # evita -> int var var ...
            if linea[2] != "=":
                print(f"Error de sintaxis: se esperaba un '=' despues de {linea[2]} en la linea {numeroLinea}")
                return
            else:

                if tipoDato == "int":

                    bandera = True
                    for i in range(3, len(linea)):
                        if linea[i] not in diccionario:
                            if linea[i] not in symbols:
                                valor = linea[i].replace("-", "").replace("+", "")
                                if not valor.isnumeric():
                                    bandera = False
                                    break
                                else:
                                    if linea[i - 1] not in symbols:
                                        bandera = False
                                        break
                            else:
                                if i == len(linea) - 1:
                                    bandera = False
                                    break
                        else:  # si esta en el diccionario
                            if diccionario[linea[i]].type != "int":
                                bandera = False
                                break
                            else:
                                if linea[i - 1] not in symbols:
                                    bandera = False
                                    break
                    if not bandera:
                        print(f"Error de sintaxis: error de asignacion en la linea {numeroLinea}")
                        return
                    else:
                        diccionario[key] = Variable(key, linea[3], tipoDato)
                        return

                if tipoDato == "float":

                    bandera = True
                    for i in range(3, len(linea)):
                        if linea[i] not in diccionario:
                            if linea[i] not in symbols:
                                valor = linea[i].replace(".", "").replace("-", "").replace("+", "")
                                if not valor.isnumeric():
                                    bandera = False
                                    break
                                else:
                                    if linea[i - 1] not in symbols:
                                        bandera = False
                                        break
                            else:
                                if i == len(linea) - 1:
                                    bandera = False
                                    break
                        else:  # si esta en el diccionario
                            if diccionario[linea[i]].type == "string":
                                bandera = False
                                break
                            else:
                                if linea[i - 1] not in symbols:
                                    bandera = False
                                    break
                    if not bandera:
                        print(f"Error de sintaxis: error de asignacion en la linea {numeroLinea}")
                        return
                    else:
                        diccionario[key] = Variable(key, linea[3], tipoDato)
                        return

                if tipoDato == "string":
                    bandera = True
                    for i in range(3, len(linea)):

                        if linea[i] not in diccionario:
                            if linea[i] != "+":
                                string = linea[i]
                                if string[0] != chr(34) or string[len(string) - 1] != chr(34):
                                    bandera = False
                                    break
                                else:
                                    if linea[i - 1] not in symbols:
                                        bandera = False
                                        break
                            else:
                                if linea[i - 1] in symbols:
                                    bandera = False
                                    break
                                else:
                                    if i == len(linea) - 1:
                                        bandera = False
                                        break
                        else:  # si esta en el diccionario
                            if diccionario[linea[i]].type != "string":
                                bandera = False
                                break
                    if not bandera:
                        print(f"Error de sintaxis: error de asignacion en la linea {numeroLinea}")
                        return
                    else:
                        diccionario[key] = Variable(key, linea[3], tipoDato)
                        return

        else:
            # declaracion sola(int x)
            if len(linea) == 2:
                if linea[1] in symbols:
                    print(f"Error de sintaxis: ({linea[1]}) en la linea {numeroLinea}")
                    return
                if linea[1] in dataTypes:
                    print(f"Error de sintaxis: uso de palabra reservada {linea[1]} en la linea {numeroLinea}")
                    return
                if linea[1] in diccionario:
                    print(
                        f"Error de sintaxis: redeclaracion de la variable {linea[1]} en la linea {numeroLinea}")
                    return
                else:
                    var = Variable(key, None, tipoDato)
                    diccionario[key] = var


def analizer(linea, numeroLinea, diccionario):  # la linea viene separada por espacios en un array
    if linea[0] not in dataTypes and linea[0] not in diccionario:
        # variable no declarada (no es tipo de dato valido ni existe la  variable)
        print(f"Error de sintaxis: no hay ninguna declaracion de la variable {linea[0]} en la linea {numeroLinea}")
        return

    key = linea[0]
    # variable pre declarada
    if key in diccionario:
        analizerVariablesPreDDeclaradas(linea, numeroLinea, diccionario, key)

    # declarar nueva variable, key not in diccionario
    else:
        tipoDato = key
        key = linea[1]
        if tipoDato in dataTypes:  # el primer valor es de tipo valido
            analizerVariablesNODeclaradas(linea, numeroLinea, diccionario, key, tipoDato)
        else:
            print(f"Error de sintaxis en la linea {numeroLinea}")
            return


def funcionAnalizer(linea, numeroLinea, diccionario, parametros):
    datta = ["int", "float", "string", "void"]
    symbolos = ["+", "-", "=", "/", "*"]

    palabras = linea.split(" ")
    palabras = [x for x in palabras if palabras != ""]
    #print(palabras)

    ddataType = palabras[0]
    key = palabras[1]


    if ddataType in datta == False:
        print(f"Error de sintaxis: tipo de dato no valido {palabras[0]} en la linea {numeroLinea}")
        return None
    else:
        if key in diccionario:
            print(f"Error de sintaxis: la funcion {palabras[1]} ya ha sido definida previamente  (linea {numeroLinea})")
        else:
            if key not in datta and key not in symbolos:
                #print(f"Key = {key} - tipo = {ddataType}")
                car = Funcion(ddataType, key, parametros)
                return car
            else:
                print(f"Error de sintaxis: uso incorrecto de palabra reservada {key}  (linea {numeroLinea})")


def returnAnalizer(palabras, index, diccionario, type):

    if palabras[0] != "return" :
        print(f"Error de sintaxis: de {palabras[0]} en la linea {index}")
        return
    else:
        if len(palabras) == 1:
            if type != "void":
                print(f"Error de sintaxis: debe retornar un valor de tipo {type}  (linea {index})")
                return
        else:
            newKey = palabras[1]
            if newKey not in symbols:

                if type == "void":
                    print(f"Error de sintaxis: la funcion no retorna nada {palabras[0]} en la linea {index}")
                    return
                if type == "float":
                    bandera = True
                    for i in range(1, len(palabras)):
                        if palabras[i] not in dataTypes and palabras[i] != "void":
                            if palabras[i] not in diccionario:
                                if palabras[i] not in symbols:
                                    valor = palabras[i].replace(".", "").replace("-", "").replace("+", "")
                                    print(valor)
                                    if not valor.isnumeric():
                                        bandera = False
                                        break
                                    else:
                                        if palabras[i - 1] not in symbols:
                                            bandera = False
                                            break
                                else:
                                    if i == len(palabras) - 1:
                                        bandera = False
                                        break
                            else:  # si esta en el diccionario
                                if diccionario[palabras[i]].type == "string":
                                    bandera = False
                                    break
                                else:
                                    if palabras[i - 1] not in symbols and i > 1:
                                        bandera = False
                                        break
                        else:
                            print(f"Error de sintaxis: return no valido en la linea {index}")
                            return
                    if not bandera:
                        print(f"Error de sintaxis: return invalido en la linea {index}")
                        return


                if type == "int":
                    bandera = True
                    for i in range(1, len(palabras)):
                        if palabras[i] not in dataTypes and palabras[i] != "void":
                            if palabras[i] not in diccionario:
                                if palabras[i] not in symbols:
                                    valor = palabras[i].replace("-", "").replace("+", "")
                                    print(valor)
                                    if not valor.isnumeric():
                                        bandera = False
                                        break
                                    else:
                                        if palabras[i - 1] not in symbols:
                                            bandera = False
                                            break
                                else:
                                    if i == len(palabras) - 1:
                                        bandera = False
                                        break
                            else:  # si esta en el diccionario
                                if diccionario[palabras[i]].type != "int":
                                    bandera = False
                                    break
                                else:
                                    if palabras[i - 1] not in symbols and i > 1:
                                        bandera = False
                                        break
                        else:
                            print(f"Error de sintaxis: return no valido en la linea {index}")
                            return
                    if not bandera:
                        print(f"Error de sintaxis: return invalido en la linea {index}")
                        return


                if type == "string":
                    pass






            else:
                print(f"Error de sintaxis: en la linea {index}")
                return





