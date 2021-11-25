from parts.tabla import Tabla_de_simbolos
from parts.textAnalizer import lineReader

tablaDeSimbolos = Tabla_de_simbolos()
lineReader("codeFile/texto.txt", tablaDeSimbolos.diccionario)
print(f"{tablaDeSimbolos.diccionario}")










