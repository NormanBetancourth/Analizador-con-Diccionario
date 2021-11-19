# Analiza si una sentencia (linea de texto es valida)
# Documentacion y tipos de errores ->
# https://mint-mine-d87.notion.site/Errores-98f348b9da8d4a1e9f134cfccdd79d92

dataTypes = ["int", "float", "string"]
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
        # variable no declarada
        print(f"Error de sintaxis: {errorTypes[1]} en la linea {linea}")
        return

    # variable declarada
    key = linea[0]
    if key in diccionario:
        if len(linea) <= 2:
            # error de asignacion incorrecta
            print(f"Error de sintaxis: {errorTypes[2]} en la linea {linea}")
            return
        if linea[2] not in diccionario:  # estamos asignando a un valor, no a una variable
            tipoDato = diccionario[key].type
            if linea[1] == "=":
                # no coincide el tipo
                if tipoDato == "int" and linea[2].isnumeric() == False:
                    print(f"Error de sintaxis: {errorTypes[2]} en la linea {linea}")
                    return
                else:
                    diccionario[key].value = linea[2]

                # no coincide el tipo
                if tipoDato == "float":
                    valor = linea[2].replace(".", "").replace("-", "").replace("+", "").replace(" ", "")
                    if valor.isnumeric() == False:
                        print(f"Error de sintaxis: {errorTypes[2]} en la linea {linea}")
                        return
                    else:
                        diccionario[key].value = linea[2]

                # no tiene corchetes
                if tipoDato == "string":
                    string = linea[2]
                    if string[0] == chr(34) or string[len(string) - 1] == chr(34):
                        diccionario[key].value = linea[2]
                    else:
                        print(f"Error de sintaxis: {errorTypes[2]} en la linea {linea}")
                        return
            else:
                print(f"Error de sintaxis: {errorTypes[6]} en la linea {linea}")
                return

        else:  # asignamos a una variable
            if diccionario[key].type != diccionario[linea[2]].type:
                print(f"Error de sintaxis: {errorTypes[2]} en la linea {linea}")
            else:
                diccionario[key].value = diccionario[linea[2]].value


    # variable no declarada, key not in diccionario
    else:
        #el primer valor es de tipo valido
        if key in dataTypes:
            #error de redeclaracion
            if linea[1] in diccionario:
                print(f"Error de sintaxis: {errorTypes[7]} en la linea {linea}")
                return

            #declaracion sola
            if len(linea) > 2:
                if linea[2] != "=":
                    print(f"Error de sintaxis: {errorTypes[6]} en la linea {linea}")
                    return
                #a asignar valores
                else:
                    pass


            #declaracion y asignacion

        else:
            print(f"Error de sintaxis: declaracion de tipo faltante en la linea {linea}")
            return