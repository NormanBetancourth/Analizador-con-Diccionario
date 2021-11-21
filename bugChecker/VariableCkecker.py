# Analiza si una sentencia (linea de texto es valida)
# Documentacion y tipos de errores ->
# https://mint-mine-d87.notion.site/Errores-98f348b9da8d4a1e9f134cfccdd79d92
from Variable import Variable

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


def analizer(linea, numeroLinea, diccionario):  # la linea viene separada por espacios en un array
    if linea[0] not in dataTypes and linea[0] not in diccionario:
        # variable no declarada (no es tipo de dato valido ni existe la  variable)
        print(f"Error de sintaxis: {errorTypes[1]} en la linea {numeroLinea}")
        return

    # variable declarada
    key = linea[0]
    if key in diccionario:
        if len(linea) <= 2:
            # error de asignacion incorrecta
            print(f"Error de sintaxis: {errorTypes[2]} en la linea {numeroLinea}")
            return

        if linea[1] == "=":
            if linea[2] in diccionario: #asignamos una variable a otra variable (var 2 esta en el diccionario)
                if diccionario[key].type != diccionario[linea[2]].type:
                    print(f"Error de sintaxis: {errorTypes[2]} en la linea {numeroLinea}")
                    return
                else:
                    diccionario[key].value = diccionario[linea[2]].value
                    return

            else:# estamos asignando a un valor, no a una variable
                tipoDato = diccionario[key].type
                # no coincide el tipo
                if tipoDato == "int" and linea[2].isnumeric() == False:
                    print(f"Error de sintaxis: el tipo de dato no coincide ({tipoDato}) en la linea {numeroLinea}")
                    return
                else:
                    diccionario[key].value = linea[2]

                # no coincide el tipo
                if tipoDato == "float":
                    valor = linea[2].replace(".", "").replace("-", "").replace("+", "").replace(" ", "")
                    if not valor.isnumeric():
                        print(f"Error de sintaxis: el tipo de dato no cioncide ({tipoDato}) en la linea {numeroLinea}")
                        return
                    else:
                        diccionario[key].value = linea[2]
                        return

                # no tiene ""
                if tipoDato == "string":
                    string = linea[2]
                    if string[0] == chr(34) and string[len(string) - 1] == chr(34):
                        diccionario[key].value = linea[2]
                        return
                    else:
                        print(f"Error de sintaxis: el tipo de dato no coincide ({tipoDato}) en la linea {numeroLinea}")
                        return
                else:
                    # caso de que no sea valor y sea una var que no esta en el diccionario
                    print(f"Error de sintaxis: la variable {linea[2]} no ha sido declarada en la linea {numeroLinea}")



    # declarar nueva variable, key not in diccionario
    else:
        tipoDato = key
        key = diccionario[1]
        if tipoDato in dataTypes:#el primer valor es de tipo valido
            if linea[1] in diccionario: #redeclaracion de variable
                print(f"Error de sintaxis: redeclaracion de la variable {linea[1]} en la linea {numeroLinea}")
                return
            else:# creamos nueva variable
                if len(linea) > 2:#declaracion y asignacion (int x = value)

                    #evita -> tipo tipo = ...
                    if linea[1] in dataTypes:
                        print(f"Error de sintaxis: mal uso palabra reservada {linea[1]} en la linea {numeroLinea}")
                        return

                    #evita -> int var var ...
                    if linea[2] != "=":
                        print(f"Error de sintaxis: se esperaba un '=' despues de {linea[1]} en la linea {numeroLinea}")
                        return
                    else:#si viene el = en buen orden
                        # 1) = variable
                        if linea[3] in diccionario:
                            pass
                        else:
                            # 2) = valor
                            # Coincidir tipo de variable con valor
                            if tipoDato == "int" and linea[3].isnumeric() == False:
                                print(f"Error de sintaxis: el tipo de dato no coincide ({tipoDato}) en la linea {numeroLinea}")
                                return
                            else:
                                diccionario[key] = Variable(key, linea[3], tipoDato)

                            if tipoDato == "float":
                                valor = linea[3].replace(".", "").replace("-", "").replace("+", "").replace(" ",
                                                                                                            "")  # quitamos simbolos o puntos
                                if not valor.isnumeric():
                                    print(f"Error de sintaxis: el tipo de dato no cioncide ({tipoDato}) en la linea {numeroLinea}")
                                    return
                                else:
                                    diccionario[key] = Variable(key, linea[3], tipoDato)
                                    return

                            # no tiene ""
                            if tipoDato == "string":
                                string = linea[3]
                                if string[0] == chr(34) and string[len(string) - 1] == chr(34):
                                    diccionario[key]= Variable(key, linea[3], tipoDato)
                                    return
                                else:
                                    print(f"Error de sintaxis: el tipo de dato no coincide ({tipoDato}) en la linea {numeroLinea}")
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
                            print(f"Error de sintaxis: redeclaracion de la variable {linea[1]} en la linea {numeroLinea}")
                            return
                        else:
                            var = Variable(linea[1], None, key)
                            diccionario[linea[1]] = var




        else:
            print(f"Error de sintaxis en la linea {numeroLinea}")
            return