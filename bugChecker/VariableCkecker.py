# Analiza si una sentencia (linea de texto es valida)
# Documentacion y tipos de errores ->
# https://mint-mine-d87.notion.site/Errores-98f348b9da8d4a1e9f134cfccdd79d92
from parts.Variable import Variable

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
        print(f"Error de sintaxis: no hay ninguna declaracion de la variable {linea[0]} en la linea {numeroLinea}")
        return

    # variable declarada
    key = linea[0]
    if key in diccionario:
        if len(linea) <= 2:
            # error de asignacion incorrecta
            print(f"Error de sintaxis: {errorTypes[2]} en la linea {numeroLinea}")
            return

        if linea[1] == "=":
            # --------------------------------------------------------------------------------------------------------------------------------

            # if linea[2] in diccionario: #asignamos una variable a otra variable (var 2 esta en el diccionario)
            #     if diccionario[key].type == "int" and diccionario[linea[2]].type == "float" or  diccionario[key].type == "float" and diccionario[linea[2]].type == "int" :
            #         diccionario[key].value = diccionario[linea[2]].value
            #         return
            #     if diccionario[key].type != diccionario[linea[2]].type:
            #         print(f"Error de sintaxis: no se puede pasar de {diccionario[key].type} a {diccionario[linea[2]].type} en la linea {numeroLinea}")
            #         return

            # vamos a recorrer los demas elementos del array (coincidir dataType)
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
                    print(linea[i])
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

    # declarar nueva variable, key not in diccionario
    else:
        tipoDato = key
        key = linea[1]
        if tipoDato in dataTypes:  # el primer valor es de tipo valido
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
                        # si viene el = en buen orden
                        # 1) = variable
                        # if linea[3] in diccionario:
                        #     keyVariable2 = linea[3]
                        #     if tipoDato == diccionario[keyVariable2].type:
                        #         diccionario[key] = Variable(key, diccionario[keyVariable2].value, tipoDato)
                        #     else:
                        #         print(
                        #             f"Error de sintaxis: no se puede asignar {tipoDato} a {diccionario[keyVariable2].type} en la linea {numeroLinea}")

                        if tipoDato == "int":
                            print(linea)
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

                        #     # 2) = valor
                        #     # Coincidir tipo de variable con valor
                        # if tipoDato == "int":
                        #     valor = linea[3].replace("-", "").replace("+", "")
                        #     if not valor.isnumeric():
                        #         print(f"Error de sintaxis: error de asignacion en la linea {numeroLinea}")
                        #         return
                        #     else:
                        #         diccionario[key] = Variable(key, linea[3], tipoDato)
                        #         return

                        if tipoDato == "float":
                            print(linea)
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
                                print(linea[i])
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
        else:
            print(f"Error de sintaxis en la linea {numeroLinea}")
            return