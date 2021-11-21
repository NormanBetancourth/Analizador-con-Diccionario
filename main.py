from parts.textAnalizer import lineReader
from parts.tabla import Tabla_de_simbolos
#
# t = Tabla_de_simbolos()
#
# t.add( "numero", 19, "int")
# t.add( "caracter", 'c', "char")
#
# print(t)
tablaDeSimbolos = Tabla_de_simbolos()
lineReader("codeFile/texto.txt", tablaDeSimbolos.diccionario)

print(f"{tablaDeSimbolos.diccionario}")




