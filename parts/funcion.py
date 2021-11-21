from parts.tabla import Tabla_de_simbolos


class Funcion:
    def __init__(self, type, key, parametros):
        self.parametros = parametros
        self.key = key
        self.type = type
        self.tabla_de_simbolos = Tabla_de_simbolos()
        for i in parametros:
            self.tabla_de_simbolos.agregar(i)
